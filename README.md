# File Downloader

This is a Python script that downloads a file from a given URL and saves it to the local machine. It uses the `requests` library to handle HTTP requests and ensure successful file retrieval. This script is intended for educational purposes to understand file downloading mechanisms in Python.

## Features
- Downloads a file from a specified URL.
- Saves the downloaded file with its original filename.
- Checks for successful HTTP responses before saving.

## Prerequisites
- Python 3.x
- `requests` library (for handling HTTP requests)

## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/file_downloader.git
cd file_downloader
```

Install the required library:

```bash
pip install requests
```

## Usage
Run the script to download a file from a given URL.

```bash
python3 file_downloader.py
```

### Notes:
- Replace `https://www.page.com/images/image.jpg` in the script with the actual URL of the file you want to download.
- Ensure you have an active internet connection before running the script.

## Example Output:

```
Downloading file: image.jpg
Download complete!
```

## Troubleshooting
- Ensure the provided URL is accessible.
- Verify that you have installed the `requests` library.
- Check if the script has write permissions to save files in the current directory.

## License
This project is licensed under the MIT License.

## About
This script is part of the course **Learn Python & Ethical Hacking from Scratch** on Udemy. The course covers Python scripting and its application in ethical hacking, network security, and more.

---

### Disclaimer:
This script is for educational purposes only. Unauthorized downloading of copyrighted materials is illegal and unethical. Use this script only for legitimate purposes.