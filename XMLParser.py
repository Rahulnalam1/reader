import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import json  

def extract_and_clean_html(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    return ' '.join(soup.get_text().split())

def extract_all_financial_data(xml_path, output_path):

    tree = ET.parse(xml_path)
    root = tree.getroot()


    all_financial_data = {}


    for element in root.iter():
        tag = element.tag.split('}')[-1]  
        text = element.text.strip() if element.text else 'Not found'

        if '<' in text and '>' in text:
            text = extract_and_clean_html(text)
        all_financial_data[tag] = text


    with open(output_path, 'w') as file:
        json.dump(all_financial_data, file, indent=4)


xml_path = 'snap.xml'
output_path = 'summary.json'


extract_all_financial_data(xml_path, output_path)