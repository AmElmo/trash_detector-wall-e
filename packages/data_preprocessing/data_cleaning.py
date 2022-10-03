
import json
import pandas as pd
import copy


# Function to build the matching dictionary used to match categories between JSON files

final_categories = {
    0: 'Paper',
    1: 'Plastic',
    2: 'Glass',
    3: 'Metal',
    4: 'Organic',
    5: 'E-Waste',
    6: 'Non-recyclable'
}

def build_matching_dictionary(json_path,list_matching_cat):
    with open(json_path) as f:
        data_drinking_class = json.load(f)

    # Instantiate lists
    categories_drinking_class = []
    list_ids = []

    # Build lists

    for x in range(len(data_drinking_class['categories'])):
        categories_drinking_class.append(data_drinking_class['categories'][x]['name'])


    for category in list_matching_cat:
        list_ids.append([int(k) for k, v in final_categories.items() if v == category][0])


    # Concatenate into one central Dataframe

    matching_cat_drinking_class = pd.DataFrame(list_matching_cat, columns=['Matching category name'])
    categories_drinking_class = pd.DataFrame(categories_drinking_class, columns=['Original category name'])
    list_ids = pd.DataFrame(list_ids,columns=['Matching Category ID'])

    dict_drinking_class = pd.concat([categories_drinking_class, matching_cat_drinking_class, list_ids], axis=1)

    return dict_drinking_class


# Function to change categories for each annotations with matching ones

def change_annotations(original_json_path,matching_dictionary):

    # Open JSON file and make copy

    with open(original_json_path) as f:
        original_json = json.load(f)

    new_json = copy.deepcopy(original_json)

    # Iterate over copy and change category in "annotations"

    for annotation in new_json['annotations']:
        annotation_cat_id = annotation['category_id']
        annotation['category_id'] = matching_dictionary[matching_dictionary.index == annotation_cat_id]['Matching Category ID'].item()

    return new_json


# Function to overwrite the old categories with new ones

def overwrite_categories(json_file):

    json_file['categories'] = []

    for index, category in final_categories.items():
        json_file['categories'].append({
            "supercategory": category,
            "id": index,
            "name": category
    })

    return json_file


# Function to change image names to reflect new directory ("batch_xx")

def change_image_names(json_file,batch_number):

    for img in json_file["images"]:
        img['file_name'] = "batch_" + str(batch_number) + "/" + img['file_name']

    return json_file
