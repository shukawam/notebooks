# maximum number of DLS Dataset records that can be retrieved from the list_records API operation for labeling
# limit=1000 is the hard limit for list_records
LIST_RECORDS_LIMIT = 1000
# an array where the elements are all of the labels that you will use to annotate records in your DLS Dataset with.
# Each element is a separate label.
LABEL = ['car']
# Path of bounding_boxes_path
BOUNDING_BOXES_PATH = "/home/shukawam/work/notebooks/vision/car_detection/car_detection_dataset/train_solution_bounding_boxes.csv"
# Oath of output file
OUTPUT_FILE = '/home/shukawam/work/notebooks/vision/car_detection/input_data.csv'
COLUMNS = ['record_id', 'x1', 'x2', 'x3',
           'x4', 'y1', 'y2', 'y3', 'y4', 'label']
DROPED_COLUMNS = ['name', 'image', 'compartment_id', 'dataset_id', 'is_labeled', 'lifecycle_state', 'time_created', 'time_updated',
                  'record_metadata.depth', 'record_metadata.height', 'record_metadata', 'record_metadata.record_type', 'record_metadata.width']
IMG_H, IMG_W = (380, 676)
