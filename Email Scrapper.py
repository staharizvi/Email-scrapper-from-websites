import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import csv
from urllib.parse import urljoin

# Load the Excel sheet
df = pd.read_excel('business_info.xlsx')

# Function to clean the website URLs by removing unwanted characters
def clean_url(url):
    return re.sub(r'[^\x00-\x7F]+', '', url).strip()

# Function to extract email from a given page URL
def extract_email_from_page(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Search for 'mailto' links
            mailtos = soup.select('a[href^=mailto]')
            if mailtos:
                return mailtos[0]['href'].replace('mailto:', '')

            # Find all visible emails using regex
            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.text)
            return emails[0] if emails else None
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Function to find "Contact" or "About" pages and extract email
def search_for_contact_pages(base_url):
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Search for potential contact or about links
            contact_links = soup.find_all('a', href=True)
            for link in contact_links:
                href = link['href'].lower()
                if 'contact' in href or 'about' in href:
                    contact_page_url = urljoin(base_url, href)
                    email = extract_email_from_page(contact_page_url)
                    if email:
                        return email
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {base_url}: {e}")
        return None

# List to store results
results = []

# Iterate over the rows in the DataFrame
for index, row in df.iterrows():
    business_name = row['Name']
    website_url = row['Website']

    if pd.notnull(website_url):
        cleaned_url = clean_url(website_url)
        url_with_http = f"http://{cleaned_url}"

        # Try to extract email from the homepage first
        email = extract_email_from_page(url_with_http)

        # If no email found, look for "Contact" or "About" pages
        if not email:
            email = search_for_contact_pages(url_with_http)

        results.append({
            'Business Name': business_name,
            'Website': cleaned_url,
            'Email': email
        })

# Save the results to a CSV file
with open('business_emails.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Business Name', 'Website', 'Email'])
    writer.writeheader()
    writer.writerows(results)

print("Emails extracted and saved to 'business_emails.csv'")
