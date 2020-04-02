from datetime import datetime
from tqdm import tqdm
import requests
import re

url = input("Enter URL: ")

spotify = re.match(r'^(https:|)[/][/]([^/]+[.])*open.spotify.com', url)
soundCloud = re.match(r'^(https:|)[/][/]([^/]+[.])*soundcloud.com', url)

#Function to check the internet connection
#Got this from https://stackoverflow.com/a/24460981
def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def spotifyDownload():
    req = requests.get(url).content.decode('utf-8')

    search = re.search(r'Spotify is currently not available in your country', req)
    search2 = re.search(r'<meta property=\"og:image\" content=\"(.*?)\" />', req)

    list = []
    regexlist = [search, search2]
    for id,val in enumerate(regexlist):
        if val is not None:
            list.append(id)

    if 0 in list:
        print("Spotify is currently not available in your country. Please use a VPN")
    if 1 in list:
        _y = search2.group(1)
        file_size_request = requests.get(_y, stream=True)
        file_size = int(file_size_request.headers['Content-Length'])
        block_size = 1024 
        filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
        t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
        with open(filename + '.jpg', 'wb') as f:
            for data in file_size_request.iter_content(block_size):
                t.update(len(data))
                f.write(data)
        t.close()
        print("Image downloaded successfully")  

def soundcloudDownload():
    req = requests.get(url).content.decode('utf-8')

    search = re.search(r'<meta property=\"og:image\" content=\"(.*?)\">', req).group(1)
    file_size_request = requests.get(search, stream=True)

    # Getting response of http request without content-length therefore implemented this 
    file_size = len(file_size_request.content)

    block_size = 1024 
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(filename + '.jpg', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    print("Image downloaded successfully")  

if connection() == True:
    try:
        if spotify:
            spotifyDownload()
            quit()
        elif soundCloud:
            soundcloudDownload()
            quit()
        else:
            print("Unknown Error")
            quit()
    except KeyboardInterrupt:
        print("\nProgramme Interrupted")