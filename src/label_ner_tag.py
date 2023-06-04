"""
entity_tag
    0: B-GPE,
    1: I-GPE,
    2: B-PER,
    3: I-PER,
    4: B-DATE,
    5: I-DATE,
    6: B-ORG,
    7: I-ORG,
    8: B-CARDINAL,
    9: I-CARDINAL,
    10: B-NORP,
    11: I-NORP,
    12: B-LOC,
    13: I-LOC,
    14: B-TIME,
    15: I-TIME,
    16: B-FAC,
    17: I-FAC,
    18: B-MONEY,
    19: I-MONEY,
    20: B-ORDINAL,
    21: I-ORDINAL,
    22: B-EVENT,
    23: I-EVENT,
    24: B-WFA,
    25: I-WFA,
    26: B-QUANTITY,
    27: I-QUANTITY,
    28: B-PERCENT,
    29: I-PERCENT,
    30: B-LANGUAGE,
    31: I-LANGUAGE,
    32: B-PRODUCT,
    33: I-PRODUCT,
    34: B-LAW,
    35: I-LAW,
    36: O
"""
from ckiptagger import POS, NER
import pandas

ner_tag_binder = {'GPE': 0, 'PERSON': 2, 'DATE': 4, 'ORG': 6, 'CARDINAL': 8, 'NORP': 10, 'LOC': 12, 'TIME': 14,
                  'FAC': 16, 'MONEY': 18, 'ORDINAL': 20, 'EVENT': 22, 'WORK_OF_ART': 24, 'QUANTITY': 26, 'PERCENT': 28,
                  'LANGUAGE': 30, 'PRODUCT': 32, 'LAW': 34}


data = pandas.read_csv('../Datasets/self_create_datasets_with_diff_tags/Train_data_pos_tags.csv')['Paragraph'].tolist()
token_data = pandas.read_csv('../Datasets/self_create_datasets_with_diff_tags/News_data_token.csv')['Paragraph'].tolist()
pos = POS('../Datasets/data')
ner = NER('../Datasets/data')

for ind, element in enumerate(data):
    pos_list = pos([element])
    ner_list = ner([element], pos_list)
    temp = [36 for i in range(len(element))]
    for index, el in enumerate(ner_list[0]):
        temp[el[0]] = ner_tag_binder[el[2]]
        for i in range(el[0] + 1, el[1]):
            temp[i] = ner_tag_binder[el[2]] + 1

    df = pandas.DataFrame({'Id': [ind], 'Tokens': [token_data[ind]], 'NER_tag': [temp.__str__()]})
    df.to_csv('../Datasets/Train_data_ner_tags.csv', encoding='utf-8', index_label=False, index=False,
              columns=df.keys(), header=False, mode='a')
    print(f'current running at index {ind}')
