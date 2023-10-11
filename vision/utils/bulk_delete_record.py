import oci
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


def dls_list_records_ocid(compartment_id):
    try:
        # limit parameter has an implicit value of 10 if not included
        anno_response = dls_dp_client.list_records(compartment_id=compartment_id, dataset_id=DATASET_ID,
                                                   is_labeled=False, limit=LIST_RECORDS_LIMIT, page=None)
    except Exception as error:
        anno_response = error
        print(anno_response)
    # manage the json
    data = json.loads(str(anno_response.data))
    # ocid of each record
    ids = [dls_dataset_record["id"] for dls_dataset_record in data["items"]]
    return ids


def bulk_delete_record(compartment_id):
    ids = dls_list_records_ocid(compartment_id=compartment_id)
    for id in ids:
        dls_dp_client.delete_record(id)
        print("delete record {}".format(id))


def main():
    logging.basicConfig(filename="debug.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info(
        "...........starting to bulk delete record.............")
    try:
        response = dls_dp_client.get_dataset(dataset_id=DATASET_ID)
        logger.info("Fetching Dataset")
    except Exception as error:
        response = error
    if response.status == 200:
        logger.info("Fetching Dataset Successful")
        compartment_id = response.data.compartment_id
        bulk_delete_record(compartment_id)
    else:
        print(response)


if __name__ == "__main__":
    main()
