import fiftyone as fo
import fiftyone.types as fot

# -------------------------
# Paths
# -------------------------
VAL_IMAGES_DIR = "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/images/val_data"
VAL_ANN_FILE   = "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/annotations/instances_val.json"

TRAIN_IMAGES_DIR = "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/images/train_data"
TRAIN_ANN_FILE   = "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/annotations/instances_train.json"

# -------------------------
# Load datasets
# -------------------------
val_dataset = fo.Dataset.from_dir(
    dataset_dir=VAL_IMAGES_DIR,
    dataset_type=fot.COCODetectionDataset,
    labels_path=VAL_ANN_FILE,
    name="seaclear_val"
)

train_dataset = fo.Dataset.from_dir(
    dataset_dir=TRAIN_IMAGES_DIR,
    dataset_type=fot.COCODetectionDataset,
    labels_path=TRAIN_ANN_FILE,
    name="seaclear_train"
)

# -------------------------
# Launch FiftyOne
# -------------------------
session = fo.launch_app(val_dataset, port=6789)
# fo.launch_app(train_dataset)  # optional
