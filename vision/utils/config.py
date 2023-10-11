import multiprocessing as mp

# for help, run:
# python3 help.py

# config file path
CONFIG_FILE_PATH = "~/.oci/config"
# config file profile
CONFIG_PROFILE = "DEFAULT"
# identifier
REGION_IDENTIFIER = "ap-tokyo-1"
# service_endpoint
SERVICE_ENDPOINT_DP = f"https://dlsprod-dp.{REGION_IDENTIFIER}.oci.oraclecloud.com"
SERVICE_ENDPOINT_OBJECT_STORAGE = f"https://objectstorage.{REGION_IDENTIFIER}.oraclecloud.com"
# ocid of the DLS Dataset
DATASET_ID = "ocid1.datalabelingdataset.oc1.ap-tokyo-1.amaaaaaassl65iqaasy2csxqr7jhdubh2na3uqv4fovk5wzzifphs7zfqckq"
# the no of processes to be used for parallel execution by default is set to maximum no of processors in the system
NO_OF_PROCESSORS = mp.cpu_count()
# Type of Annotation
# Possible values for ANNOTATION_TYPE "BOUNDING_BOX", "CLASSIFICATION"
ANNOTATION_TYPE = "BOUNDING_BOX"
##############################################################################################################
# If ANNOTATION_TYPE is "CLASSIFICATION" edit classification_config.py
# If ANNOTATION_TYPE is "BOUNDING_BOX" edit bounding_box__config.py
# Prefix will be a label name, or label name prefix
REMOVE_LABEL_PRIFIX = "car"
# Prefix of upload files
OBJECT_STORAGE_PREFIX = ""
# Files present inside this directory will be uploaded to the object storage bucket
DATASET_DIRECTORY_PATH = f"/home/shukawam/work/notebooks/vision/car_detection/car_detection_dataset/training_images"
# Object storage bucket name where the dataset will be uploaded
OBJECT_STORAGE_BUCKET_NAME = "car-detection-dataset"
# Namespace of the object storage bucket
OBJECT_STORAGE_NAMESPACE = "orasejapan"
