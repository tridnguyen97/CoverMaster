import re
import requests
import threading
from mutagen.mp3 import MP3
from datetime import datetime
from mutagen.id3 import ID3, APIC, error


class Controller():

    def soundcloud_Download():
        req = requests.get(inputValue).content.decode('utf-8')

        search = re.search(r'<meta property=\"og:image\" content=\"(.*?)\">', req).group(1)
        file_size_request = requests.get(search, stream=True)
        files = [("jpeg files","*.jpg")]
        filelocation = asksaveasfilename(filetypes = files, defaultextension = files)
        block_size = 1024
        with open(filelocation, 'wb') as f:
            for data in file_size_request.iter_content(block_size):
                f.write(data)
            message = "Done","Image downloaded successfully"
        return message


    def spotify_Download():
        req = requests.get(inputValue).content.decode('utf-8')

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
            files = [("jpeg files","*.jpg")]
            filelocation = asksaveasfilename(filetypes = files, defaultextension = files)
            filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
            file_size = int(file_size_request.headers['Content-Length'])
            block_size = 1024
            with open(filelocation, 'wb') as f:
                for data in file_size_request.iter_content(block_size):
                    f.write(data)
                message = "Done","Image downloaded successfully"
            return message
