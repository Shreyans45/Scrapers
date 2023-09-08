import requests as req


def scrap(url):
    i = input("DO YOU WANT TO SCRAP ......Y/N: ")
    while i.lower() == "y":
        re = req.get(url)
        if re.status_code == 200:
            text = re.content
            fn = input("Enter file name: ")
            try:
                with open(fn, 'wb') as fd:
                    fd.write(text)
                print("File saved successfully.")
            except Exception as e:
                print("Exception:", str(e))
        else:
            print("Invalid URL or request failed.")

        i = input("DO YOU WANT TO SCRAP AGAIN......Y/N: ")
url = input("Enter URL: ")
scrap(url)
