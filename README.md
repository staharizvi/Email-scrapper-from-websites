# Business Email Scraper

This Python script extracts email addresses from business websites listed in an Excel file. It first tries to scrape the homepage for emails and, if not found, it searches the "Contact Us" or "About Us" pages for email addresses. The results are saved in a CSV file.

## Features

- Scrapes business websites for emails.
- Supports searching "Contact" or "About" pages for hidden emails.
- Outputs results to a CSV file.

## Requirements

The script requires the following Python libraries:

- `pandas`: For reading the Excel file containing business information.
- `requests`: For sending HTTP requests to the websites.
- `beautifulsoup4`: For parsing the HTML content of web pages.
- `lxml`: A fast parser used by BeautifulSoup to handle HTML.

You can install all dependencies using the provided `requirements.txt` file.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/staharizvi/Email-scrapper-from-websites.git
    cd business-email-scraper
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your Excel file (e.g., `business_info.xlsx`) to the project directory. The Excel file should contain columns for business name and website, with at least the following headers:
    - **Name** (Business name)
    - **Website** (Website URL)

## Usage

1. Run the script to extract emails:
    ```bash
    python email_scraper.py
    ```

2. The script will process each website listed in your Excel file, scrape for email addresses, and save the results to `business_emails.csv` in the project directory.

### Excel File Format

Ensure that your Excel file (`business_info.xlsx`) has the following columns:

| Name             | Website          |
|------------------|------------------|
| Business Name 1  | example.com       |
| Business Name 2  | example2.com      |

### CSV Output

The script will save the emails it finds to a CSV file (`business_emails.csv`) with the following format:

| Business Name    | Website         | Email               |
|------------------|-----------------|---------------------|
| Business Name 1  | example.com     | info@example.com     |
| Business Name 2  | example2.com    | contact@example2.com |

## License

This project is licensed under the MIT License.
