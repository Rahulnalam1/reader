import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

def extract_and_clean_html(html_content):
    # Use BeautifulSoup to parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract text and remove extra whitespace
    return ' '.join(soup.get_text().split())

def extract_financial_data(xml_path, output_path):
    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Namespace handling
    namespaces = {'gaap': 'http://fasb.org/us-gaap/2023'}

    # Define the tags for potential financial data components
    tags = {
        'OperatingIncomeLoss': 'gaap:OperatingIncomeLoss',
        'InterestExpense': 'gaap:InterestExpense',
        'IncomeTaxExpenseBenefit': 'gaap:IncomeTaxExpenseBenefit',
        'Depreciation': 'gaap:DepreciationDepletionAndAmortization',
        'AmortizationOfIntangibles': 'gaap:AmortizationOfIntangibleAssets',
        'NetIncomeLoss': 'gaap:NetIncomeLoss',
        'CostOfRevenue': 'gaap:CostOfRevenue',
        'OperatingLeaseCost': 'gaap:OperatingLeaseCost',
        'CommonStockSharesIssued': 'gaap:CommonStockSharesIssued',
        'CommonStockSharesAuthorized': 'gaap:CommonStockSharesAuthorized',
        'StockholdersEquity': 'gaap:StockholdersEquity',
        'Revenue': 'gaap:Revenues',
        'CashAndCashEquivalentsAtCarryingValue': 'gaap:CashAndCashEquivalentsAtCarryingValue',
        'AccountsReceivableNetCurrent': 'gaap:AccountsReceivableNetCurrent',
        'ResearchAndDevelopmentExpense': 'gaap:ResearchAndDevelopmentExpense',
        'IncomeTaxDisclosureTextBlock': 'gaap:IncomeTaxDisclosureTextBlock',
        'ComprehensiveIncomeNoteTextBlock': 'gaap:ComprehensiveIncomeNoteTextBlock'
    }

    # Dictionary to store financial data
    financial_data = {}

    # Extract information
    for key, value in tags.items():
        element = root.find('.//' + value, namespaces)
        if element is not None:
            text = element.text.strip() if element.text else 'Not found'
            # Check if the text contains HTML and clean it
            if '<' in text and '>' in text:
                text = extract_and_clean_html(text)
            financial_data[key] = text
        else:
            financial_data[key] = 'Not found'

    # Write the financial data to a text file
    with open(output_path, 'w') as file:
        for key, value in financial_data.items():
            file.write(f"{key}: {value}\n")

# Specify the path to the XML file and the output text file
xml_path = '/Users/rahulnalam/Downloads/Academia/Projects/reader/snap.xml'
output_path = '/Users/rahulnalam/Downloads/Academia/Projects/reader/snap_summary.txt'

# Call the function
extract_financial_data(xml_path, output_path)

