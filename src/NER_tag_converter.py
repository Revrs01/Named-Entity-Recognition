def convert(key):
    tag_name = {0: 'B-GPE', 1: 'I-GPE', 2: 'B-PER', 3: 'I-PER', 4: 'B-DATE', 5: 'I-DATE', 6: 'B-ORG',
                7: 'I-ORG', 8: 'B-CARDINAL', 9: 'I-CARDINAL', 10: 'B-NORP', 11: 'I-NORP', 12: 'B-LOC', 13: 'I-LOC',
                14: 'B-TIME', 15: 'I-TIME', 16: 'B-FAC', 17: 'I-FAC', 18: 'B-MONEY', 19: 'I-MONEY', 20: 'B-ORDINAL',
                21: 'I-ORDINAL', 22: 'B-EVENT', 23: 'I-EVENT', 24: 'B-WFA', 25: 'I-WFA', 26: 'B-QUANTITY',
                27: 'I-QUANTITY', 28: 'B-PERCENT', 29: 'I-PERCENT', 30: 'B-LANGUAGE', 31: 'I-LANGUAGE',
                32: 'B-PRODUCT', 33: 'I-PRODUCT', 34: 'B-LAW', 35: 'I-LAW', 36: 'O'}

    return tag_name[key]
