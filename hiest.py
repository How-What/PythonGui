import requests
import re
from PySide6.QtWidgets import QProgressBar

class Hiest:
    
    __baseurl = 'https://flockmod.com/gallery/index.php?q=/post/list/user_id='
    __image_regex = rb'https://flockmod-[^\']*'
    __header_regex = rb'<title>No Images Found</title>'
    __imageurls = []
    __page_number = 1

    def __init__(self, userid, output_path, progress_bar):
        self.__userid = userid
        self.__output_path = output_path
        self.__progress_bar = progress_bar
    
    #main functionalities
    def extract_and_download(self, progressbar):
        while self.__image_found(self.__request_from_site(self.__page_number)):
            page = self.__request_from_site(self.__page_number)
            self.__imageurls += (self.__get_imageurls())


    # helper functions
    def __request_from_site(self, page_number):
        return requests.get(self.__full_url(self._page_number), allow_redirects=False)

    def __get_imageurls(self, html_page):
        imageurl_byte = re.finall(self.__image_regex, html_page)
        decoded_image_urls = []
        thumbs_regex = '/thumbs/'
        for image_byte in imageurl_byte:
            decoded = image_byte.decode('utf-8')
            if(re.search(thumbs_regex, decoded) !=None):
                decoded_image_urls.append(re.sub(thumbs_regex, '/images/', decoded))
            else:
                decoded_image_urls.append(decoded)
        return decoded_image_urls

    def __full_url(self, page_number):
        return '{0}{1}/{2}'.format(self.__baseurl, self.__userid, page_number)
    
    def __image_found(self, html_page):
        # If there are no images html page will contain <title>No Images Found</title>
        return re.search(self.__header_regex, html_page) == None

    #Getter and setters
    def set_userid(self, userid):
        self.__userid = userid
    
    def get_userid(self):
        return self.__userid
    
    def set_output_path(self, output_path):
        self.__output_path = output_path
    
    def get_output_path(self):
        return self.__output_path
    
    def fullpath(self):
        return self.__full_url(self.__userid, self.__page_number)