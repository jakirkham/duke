import json
import pandas as pd
from ontologies.ontology import get_tree_file_name


def gen_label_stub(ontology_path='dbpedia_2016-10', prune=False):

    tree_file_name = get_tree_file_name(ontology_path, prune)
    with open('ontologies/{0}'.format(tree_file_name), 'r') as f:  
        tree = json.load(f)

    classes = list(tree.keys())
    df = pd.DataFrame(classes, columns=['class'])
    df.to_csv('data/class_label_stub.csv', index=False)


def fill_labels(dataset_name='185_baseball'):

    labels_filename = 'data/{0}_labels.csv'.format(dataset_name)
    labels = pd.read_csv(labels_filename)
    return labels.fillna(-1, downcast='infer')
    # labels.to_csv(labels_filename, index=False)


def lines_to_json(dataset_name='185_baseball'):
    with open('data/{0}_positive_examples'.format(dataset_name)) as f:
        lines = f.readlines()
    examples = [s.strip() for s in lines]
    with open('data/{0}_positive_examples.json'.format(dataset_name), 'w') as f:
        json.dump(examples, f)