#Lib of https://scrapy.org/ 
import scrapy

#Realizar a instalação local com "pip install scrapy"

class VPSetSpyder(scrapy.Spider):

    #Nome para o Scrapy
    name = "vp_spider"

    #Site a serem usados 
    start_urls = ["http://folhavponline.com.br/"]

    def parse(self, response):
