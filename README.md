US Company Revenue Scraper

This project pulls a table from a Wikipedia page that lists the largest companies in the United States by revenue.

What the script does

Sends a request to the Wikipedia page
Locates the table with company information
Extracts data such as company name, revenue, profit, employees, industry, and headquarters
Saves everything into a CSV file named wikipedia.csv
Requirements

Python 3
Libraries: requests, beautifulsoup4, and pandas
You can install the required libraries with:

pip install requests beautifulsoup4 pandas



Data Source

Wikipedia: (https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)
