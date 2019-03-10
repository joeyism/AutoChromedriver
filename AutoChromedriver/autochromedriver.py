import zipfile
import io
import sys
import os
import stat

import requests

os_driver_map = {
    "linux": "linux64",
    "linux2": "linux64",
    "darwin": "mac64",
    "win32": "win32",
    "cygwin": "win32"
}

def _get_zipfile_url_(version, driveros):
    return "https://chromedriver.storage.googleapis.com/{}/chromedriver_{}.zip".format(version, driveros)

def download_chromedriver(version="2.46", location=None):
    chromedriver_fp = "./chromedriver"
    try:
        driveros = os_driver_map[sys.platform] 
    except:
        raise Exception("Driver not compatible with OS")
    
    zip_file_url = _get_zipfile_url_(version, driveros)
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
    os.chmod(chromedriver_fp, stat.S_IXUSR)

    if location:
        os.rename(chromedriver_fp, os.path.join(location, "chromedriver"))
