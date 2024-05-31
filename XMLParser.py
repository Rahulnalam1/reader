import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re
import json  # Import the json module

def extract_and_clean_html(html_content):
    # Use BeautifulSoup to parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract text and remove extra whitespace
    return ' '.join(soup.get_text().split())

def extract_all_financial_data(xml_path, output_path):
    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Dictionary to store all financial data
    all_financial_data = {}

    # Extract information from all elements
    for element in root.iter():
        tag = element.tag.split('}')[-1]  # Remove namespace if present
        text = element.text.strip() if element.text else 'Not found'
        # Check if the text contains HTML and clean it
        if '<' in text and '>' in text:
            text = extract_and_clean_html(text)
        all_financial_data[tag] = text

    # Write the financial data to a JSON file
    with open(output_path, 'w') as file:
        json.dump(all_financial_data, file, indent=4)

# Specify the path to the XML file and the output JSON file
xml_path = '/Users/rahulnalam/Downloads/Academia/Projects/reader/snap.xml'
output_path = '/Users/rahulnalam/Downloads/Academia/Projects/reader/summary.json'

# Call the new function
extract_all_financial_data(xml_path, output_path)

