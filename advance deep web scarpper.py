import requests
from bs4 import BeautifulSoup
from googlesearch import search
from urllib.parse import urlparse

# Function to perform a Google search and return a set of website names
def search_and_store_unique_website_names(query, num_results=10):
    website_names = set()

    # Perform the Google search
    try:
        for result in search(query, num_results=num_results):
            parsed_url = urlparse(result)
            website_name = parsed_url.netloc  # Extract the domain name
            website_names.add(website_name)  # Add to the set
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return website_names

# Function to visit each website, extract data, and save to a text file
def extract_and_save_data(website_name):
    # Remove ".com" and "https://" from the website name to create the filename
    filename = website_name.replace(".com", "").replace("https://", "").replace("www.","")

    # Make an HTTP request to the website
    try:
        response = requests.get("https://" + website_name)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract only the plain text from the parsed HTML
            plain_text = soup.get_text()

            # Save the plain text to a file with the generated filename
            with open(filename, "w", encoding="utf-8") as fd:
                fd.write(plain_text)
            print(f"Data from {website_name} saved to {filename}")
        else:
            print(f"Failed to retrieve data from {website_name}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching data from {website_name}: {str(e)}")

# Input the word to search
search_word = input("Enter the word to search: ")

# Perform the search and store unique website names in a set
website_names_set = search_and_store_unique_website_names(search_word)

# Visit each website, extract data, and save to text files
for website_name in website_names_set:
    extract_and_save_data(website_name)
