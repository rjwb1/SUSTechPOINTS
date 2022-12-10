import json
import os
import math
import csv
import sys

dataset_dir = sys.argv[1]

root_dir = dataset_dir + "label"
tgt_dir = dataset_dir +  "labels/"
train_dir = dataset_dir + "ImageSets/"

train_f = open(train_dir + "train.txt", "w")

for f in sorted(os.listdir(root_dir)):
    fpath = os.path.join(root_dir, f)
    tpath = tgt_dir + os.path.splitext(f)[0] + ".txt"
    if os.path.splitext(f)[1] == ".json":
        with open(fpath, "r") as fin:
            objs = json.load(fin)
        # format: [x y z dx dy dz heading_angle category_name]
        labels = []
        if objs:
            train_f.write(os.path.splitext(f)[0] + "\n")    
        else:
            print(fpath + " is empty, skipping!")
        for o in objs:
            label = [o["psr"]["position"]["x"], o["psr"]["position"]["y"], o["psr"]["position"]["z"], o["psr"]["scale"]["x"], o["psr"]["scale"]["y"], o["psr"]["scale"]["z"], o["psr"]["rotation"]["z"], "Person"]
            labels.append(label)     
        with open(tpath, "w") as fout:
            writer = csv.writer(fout, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(labels)    
train_f.close()
