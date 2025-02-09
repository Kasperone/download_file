#!/usr/bin/env python3

import requests

def download(url):
    get_response = requests.get(url)
    if get_response.status_code == 200:
        file_name = url.split("/")[-1]
        with open(file_name, "wb") as out_file:
            out_file.write(get_response.content)
    else:
        print(f"Failed to retrieve the file. Status code: {get_response.status_code}")

download("https://www.page.com/images/image.jpg")
