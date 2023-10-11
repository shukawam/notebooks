import oci
import pandas as pd
import logging
import json
from config import *
from convert_config import *


def init_dls_dp_client(config, service_endpoint, retry_strategy):
    dls_client = oci.data_labeling_service_dataplane.DataLabelingClient(
        config=config, service_endpoint=service_endpoint, retry_strategy=retry_strategy)
    return dls_client


config_file = oci.config.from_file(CONFIG_FILE_PATH, CONFIG_PROFILE)
retry_strategy = oci.retry.DEFAULT_RETRY_STRATEGY
dls_dp_client = init_dls_dp_client(
    config_file, SERVICE_ENDPOINT_DP, retry_strategy)


def parse_record(record: oci.data_labeling_service_dataplane.models.RecordSummary):
    data_flatten = [record.id, record.name]
    return data_flatten


def dls_list_records(compartment_id, page):
    """ This function is used to list all records in the dataset

    Args:
        compartment_id: the ocid of compartment in which dataset is present
    Return:
        a list of name and ocid of records in the dataset
    """
    try:
        anno_response = dls_dp_client.list_records(compartment_id=compartment_id, dataset_id=DATASET_ID,
                                                   is_labeled=False, limit=LIST_RECORDS_LIMIT, page=page)
    except Exception as error:
        anno_response = error
        print(anno_response)
    items = json.loads(str(anno_response.data.items))
    if anno_response.has_next_page:
        page = anno_response.next_page
    else:
        page = None
    return items, page


def yolo2dls(compartment_id):
    input_df = pd.read_csv(BOUNDING_BOXES_PATH)
    items, page = dls_list_records(compartment_id, None)
    items_df = pd.json_normalize(items)
    merged_df = pd.merge(items_df, input_df, left_on='name', right_on='image').drop(
        columns=DROPED_COLUMNS, errors='ignore').rename({'id': 'record_id'}, axis='columns')
    merged_df['x1'] = merged_df['xmin'] / IMG_W
    merged_df['x2'] = merged_df['xmin'] / IMG_W
    merged_df['x3'] = merged_df['xmax'] / IMG_W
    merged_df['x4'] = merged_df['xmax'] / IMG_W
    merged_df['y1'] = merged_df['ymin'] / IMG_H
    merged_df['y2'] = merged_df['ymin'] / IMG_H
    merged_df['y3'] = merged_df['ymax'] / IMG_H
    merged_df['y4'] = merged_df['ymax'] / IMG_H
    merged_df['label'] = [LABEL]*len(merged_df)
    merged_df.drop(columns=['xmin', 'ymin', 'xmax', 'ymax']).to_csv(
        OUTPUT_FILE, index=False)


def main():
    logging.basicConfig(filename="debug.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info(
        "...........starting to convert format to dls format.............")
    try:
        response = dls_dp_client.get_dataset(dataset_id=DATASET_ID)
        logger.info("Fetching Dataset")
    except Exception as error:
        response = error
    if response.status == 200:
        logger.info("Fetching Dataset Successful")
        compartment_id = response.data.compartment_id
        yolo2dls(compartment_id)
    else:
        print(response)


if __name__ == "__main__":
    main()
