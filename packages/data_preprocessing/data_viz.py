import json
import pandas as pd
import seaborn as sns

# Main functions for data visualization of class distribution

final_categories = {
    0: 'Paper',
    1: 'Plastic',
    2: 'Glass',
    3: 'Metal',
    4: 'Organic',
    5: 'E-Waste',
    6: 'Non-recyclable'
}

def draw_class_distribution(file_path):
    with open(file_path) as f:
        final_annotations = json.load(f)

    list_cat_ids = []
    list_categories = []

    for annotation in final_annotations['annotations']:
        list_cat_ids.append(annotation['category_id'])

    for annot in list_cat_ids:
        list_categories.append(final_categories[annot])

    list_cat_ids = pd.DataFrame(list_cat_ids, columns=['List IDs'])
    list_categories = pd.DataFrame(list_categories, columns=['List categories'])

    hist_categories = pd.concat([list_cat_ids,list_categories], axis=1)

    return sns.histplot(data=hist_categories, y='List categories')

def build_table_distribution(file_path):
    with open(file_path) as f:
        final_annotations = json.load(f)

    list_cat_ids = []
    list_categories = []

    for annotation in final_annotations['annotations']:
        list_cat_ids.append(annotation['category_id'])

    for annot in list_cat_ids:
        list_categories.append(final_categories[annot])

    list_cat_ids = pd.DataFrame(list_cat_ids, columns=['List IDs'])
    list_categories = pd.DataFrame(list_categories, columns=['List categories'])

    hist_categories = pd.concat([list_cat_ids,list_categories], axis=1)

    return hist_categories['List categories'].value_counts()

def build_table_distribution_normalize(file_path):
    with open(file_path) as f:
        final_annotations = json.load(f)

    list_cat_ids = []
    list_categories = []

    for annotation in final_annotations['annotations']:
        list_cat_ids.append(annotation['category_id'])

    for annot in list_cat_ids:
        list_categories.append(final_categories[annot])

    list_cat_ids = pd.DataFrame(list_cat_ids, columns=['List IDs'])
    list_categories = pd.DataFrame(list_categories, columns=['List categories'])

    hist_categories = pd.concat([list_cat_ids,list_categories], axis=1)

    return hist_categories['List categories'].value_counts(normalize=True)*100
