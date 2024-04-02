import pandas as pd
from sklearn.model_selection import train_test_split
import os

def find_label(img_name, img_labels):
    name_column = 'scan_name'

    found_row = img_labels[img_labels[name_column] == img_name]
    return found_row['status'].item()

def get_indexes_for_patient_ids(patient_ids):
    return img_labels[img_labels['patient_id'].isin(patient_ids)].index.tolist()

## TODO: get list of image paths and labels

img_labels = pd.read_csv('data\per_scan_data.csv')

all_slices_path = r'\\fsmresfiles.fsm.northwestern.edu\fsmresfiles\Ophthalmology\Mirza_Images\AMD\dAMD_GA\all_slices_3'
all_slices = os.listdir(all_slices_path)

all_imgs = [item for item in all_slices if item.endswith('.jpg')]

labels = []
for i in range(len(all_imgs)):
    img_name = all_imgs[i]

    label = find_label(img_name, img_labels)
    if label == True:
        labels.append(1)
    else:
        labels.append(0)

## TODO: random split into train and test sets

patient_ids = img_labels['patient_id'].unique()

# splitting randomly
trainval_patients, test_patients = train_test_split(patient_ids, test_size=0.2, random_state=42)
train_patients, val_patients = train_test_split(trainval_patients, test_size=0.25, random_state=42)

# indexes for each set
train_indexes = get_indexes_for_patient_ids(train_patients)
val_indexes = get_indexes_for_patient_ids(val_patients)
test_indexes = get_indexes_for_patient_ids(test_patients)

# use indexes to select images and labels for each set
X_train = all_imgs.iloc[train_indexes]
y_train = labels.iloc[train_indexes]

X_val = all_imgs.iloc[val_indexes]
y_val = labels.iloc[val_indexes]

X_test = all_imgs.iloc[test_indexes]
y_test = labels.iloc[test_indexes]

## TODO: split by patient into train and test sets









