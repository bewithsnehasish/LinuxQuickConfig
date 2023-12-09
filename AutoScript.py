import subprocess
import os

def install_software(software_name):
    try:
        subprocess.run(["sudo", "apt", "install", software_name], check=True)
        print(f"Successfully installed {software_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {software_name}. Error: {e}")

def open_download_page(software_url):
    try:
        subprocess.run(["xdg-open", software_url], check=True)
        print(f"Opened download page for {software_url}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open download page. Error: {e}")


# 1. Install Software
install_software("firefox")

# 2. Open Download Page
open_download_page("https://www.mozilla.org/en-US/firefox/new/")

# 3. Extract Archive and Move
archive_path = "path/to/your/archive.tar.gz"
destination_path = "path/to/your/destination/folder"