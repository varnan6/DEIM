import json

train = json.load(open("/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear Marine Debris Dataset/annotations/instances_train.json"))
val = json.load(open("/home/rbu/Comparison_Paper_Object_Detection/Dataset/Seaclear Marine Debris Dataset/annotations/instances_val.json"))

train_ids = {img["id"] for img in train["images"]}
val_ids = {img["id"] for img in val["images"]}

overlap = train_ids & val_ids
print("Overlapping images:", len(overlap))