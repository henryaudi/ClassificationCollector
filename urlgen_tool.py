from datetime import datetime

import pandas as pd
import requests

def read_csv(file):
    """
    Return the "Form"s into a DataFrame series.
    :param file: the path to the csv file
    :return: DataFrame series of the "unique" form names
    """
    df = pd.read_csv(file)
    return df['Form'].unique()

def generate_urls_by_year(forms):
    """
    Generate the urls for the given forms series ranging from
    2012-2023, store url and year by form into a dictionary.
    :param forms: series of form names
    :return: dictionary that stores form as entry, year and url
             as its value
    """
    base_url = "https://www.irs.gov/pub/irs-prior/"
    years = range(2012, 2024)
    urls = {}

    for form in forms:
        form_urls = []
        for year in years:
            url = f"{base_url}i{form[1:]}--{year}.pdf"
            form_urls.append((year, url))
        urls[form] = form_urls

    return urls

def check_urls_and_collect_data(urls_with_year):
    """
    Collect the status code of each given url by years corresponding to the
    certain form.
    :param urls_with_year: input dictionary that contains url and years as
           entry values
    :return: dictionary that stores form as entry, year, status code, and url
             as its value
    """
    data_with_status = {}

    for form, year_urls in urls_with_year.items():
        form_data = []
        for year, url in year_urls:
            try:
                response = requests.get(url, allow_redirects=True)
                status_code = response.status_code
                print(f"Form {form}-{year} was fetched with status code {status_code}")
            except requests.ConnectionError:
                status_code = None
                print(f"Failed to fetch form {form}")
            form_data.append((year, status_code, url))
        data_with_status[form] = form_data

    return data_with_status

def write_to_csv(forms, data_with_status):
    """
    Output the data into csv file for individual forms spanning from year 2012-2023.
    :param forms: list of strings, where each string represents the name of
                  an IRS form (e.g., 'f1040')
    :param data_with_status: A dictionary where each key is a form name and
                             the value is a list of tuples. Each tuple contains
                             three elements: the year of the form (int), the
                             HTTP status code (int) and the URL (str) of the
                             form's instructions.
    """
    # Create current time stamp.
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")

    for form in forms:
        form_data = data_with_status[form]
        df = pd.DataFrame(form_data, columns=['Year', 'HTTP status code', 'URL'])
        df.insert(0, 'Form', form)
        filename = f"urlgen_out_{timestamp}_{form}.csv"
        df.to_csv(filename, index=False)

file = "tax_form_names_01.csv"
forms = read_csv(file)
urls_with_year = generate_urls_by_year(forms)
data_with_status = check_urls_and_collect_data(urls_with_year)
write_to_csv(forms, data_with_status)