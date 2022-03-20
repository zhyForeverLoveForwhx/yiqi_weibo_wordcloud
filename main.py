# This is a sample python to get some weibo msg
import requests
from bs4 import BeautifulSoup
import json
import File_opration as FOP
import date_analysis as DAS

def Main():
    # FOP.gettxt("DateBase/%23疫情%23_result.csv", "2020-02-01", "2020-03-02")
    DAS.get_wordcloud_pic(filename='test3')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    Main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
