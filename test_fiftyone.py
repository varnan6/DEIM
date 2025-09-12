import fiftyone as fo
import fiftyone.types as fot

# Paths
VAL_IMAGES_DIR = "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/images/val_data"
VAL_ANN_FILE   = "/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear_Marine_Debris_Dataset/annotations/instances_val.json"

# Load dataset
dataset = fo.Dataset.from_dir(
    dataset_dir=VAL_IMAGES_DIR,
    dataset_type=fot.COCODetectionDataset,
    labels_path=VAL_ANN_FILE,
    name="seaclear_val"
)

# Launch FiftyOne app
fo.launch_app(dataset, port=6789)

# Keep Python script alive so the server stays running
input("FiftyOne server running on http://127.0.0.1:6789. Press Enter to exit.\n")
