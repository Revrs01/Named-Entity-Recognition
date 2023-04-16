import pandas
from jieba import posseg as pseg

data_index_counter = 5239
for i in range(5241, 9583):
    # read 10 lines a time
    paragraph = pandas.read_csv('../Datasets/News_data.csv')['Paragraph'][i]

    # initialize
    tokenized_string = list()
    tag_string = list()

    # Tokenization & POS-tagging
    try:
        for tokenized, tag in pseg.cut(paragraph):
            tokenized_string.append(tokenized)
            tag_string.append(tag)

        print(f'current at index {i}, storage at index {data_index_counter}')
    except:
        continue

    # create new dataframe
    dataframe = pandas.DataFrame(
        {'Index': [data_index_counter], 'Paragraph': [paragraph], 'Tokenized': [tokenized_string.__str__()],
         'POS-Tag': [tag_string.__str__()]})

    # append to existing file
    dataframe.to_csv('../Datasets/Train_data.csv',
                     mode='a', index_label=False, index=False, encoding='utf-8', columns=dataframe.keys(), header=False)
    data_index_counter += 1
