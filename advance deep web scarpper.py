import requests
from bs4 import BeautifulSoup
from googlesearch import search
from urllib.parse import urlparse

def search_and_store_unique_website_names(query, num_results=10):
    website_names = set()

    try:
        for result in search(query, num_results=num_results):
            parsed_url = urlparse(result)
            website_name = parsed_url.netloc 
            website_names.add(website_name) 
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return website_names

def extract_and_save_data(website_name):
    
    filename = website_name.replace(".com", "").replace("https://", "").replace("www.","")

   
    try:
        response = requests.get("https://" + website_name)
        if response.status_code == 200:
           
            soup = BeautifulSoup(response.text, 'html.parser')

            
            plain_text = soup.get_text()

            with open(filename, "w", encoding="utf-8") as fd:
                fd.write(plain_text)
            print(f"Data from {website_name} saved to {filename}")
        else:
            print(f"Failed to retrieve data from {website_name}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching data from {website_name}: {str(e)}")

search_word = input("Enter the word to search: ")


website_names_set = search_and_store_unique_website_names(search_word)


for website_name in website_names_set:
    extract_and_save_data(website_name)
