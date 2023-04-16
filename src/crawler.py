import re
import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_title():
    result = str()
    find_news_title = str(driver.find_element(By.CLASS_NAME, 'fncnews-content').get_attribute('innerHTML'))
    reg = re.compile('(?<=<h1>).+?(?=</h1>)')
    for match in re.finditer(reg, find_news_title):
        result += find_news_title[match.start():match.end()].replace('\n', '')
    return result


def get_time():
    result = str()
    find_news_time = driver.find_element(By.CLASS_NAME, 'info').find_element(By.CLASS_NAME, 'small-gray-text')
    reg = re.compile('.+[0-9/:]+')
    for match in re.finditer(reg, find_news_time.text):
        result += find_news_time.text[match.start():match.end()]
    return result


def get_paragraph():
    result = str()
    find_news_paragraph = driver.find_element(By.CLASS_NAME, 'raw-style').find_elements(By.TAG_NAME, 'p')
    for match in find_news_paragraph:
        if match.text == '💬神器來了！隨時關心大小事💬 ':
            continue
        result += match.text.strip()
    return result


# initialization, read csv, get URL as list
csv_file_dataframe = pandas.read_csv('test.csv')
url_list = csv_file_dataframe['URL'].values.tolist()

# activate webdriver
driver = webdriver.Chrome()

for count in range(9664, len(url_list)):
    try:
        # send request to the link and get the page HTML
        driver.get(url_list[count])
        time.sleep(3)
        # filter out Title, time, paragraph
        # export to csv
        df = pandas.DataFrame(
            {'Title': [get_title()], 'Time': [get_time()], 'Paragraph': [get_paragraph()], 'URL': [url_list[count]]})
        print(f'running {count + 1} url in csv')
        df.to_csv('title_time_paragraph.csv', mode='a', header=False, columns=df.keys(), index=False, encoding='utf-8',
                  index_label=False)
    except:
        print(f'stop at line {count + 1} in url csv file')
        break