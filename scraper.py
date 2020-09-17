#Lib of https://scrapy.org/ 
import scrapy
#Realizar a instalação local com "pip install scrapy"

#
class VPSetSpyder(scrapy.Spider):

    #Nome para o Scrapy (VP = vila prudente, estou usando um site de noticias local para pegar as informações)
    name = "vp_spider"

    #Site a serem usados 
    start_urls = ["http://folhavponline.com.br/categoria/ultimas-noticias/"]

    def parse(self, response):
        # seletor css para pegar todos elementos da pagina
        SET_SELECTOR = '.media'


        for vp in response.css(SET_SELECTOR):

            # pseudo seletor para pegar o conteudo da minha tag title da noticia
            TITLE_SELECTOR = 'a ::text'

            IMAGE_SELECTOR = 'img ::attr(src)'

            #utilizando xpath para pegar o elemento data de dentro de uma div de @media
            DATE_SELECTOR = '//div[@class="date-created item"]/a/text()'
         

            yield {
                # aqui estamos pegando apenas o primeiro elemento do meu pseudo sseletor 
                'title': vp.css(TITLE_SELECTOR).extract_first(),
                'img': vp.css(IMAGE_SELECTOR).extract_first(),
                'date': vp.xpath(DATE_SELECTOR).extract_first(),
            }

            # aqui assim que concluimos a extração de dados da pagina rastreamos a proxima
            # localizando onde esta o link da proxima pagina o scrapy.request() é um valor 
            # dizendo para o scrapy rastrear esse link, e em callback pedimos para que a
            # resposta seja mandada para parse que é o nosso metodo
            NEXT_PAGE_SELECTOR = '.page-numbers a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            print("AQUIII",next_page)
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )



#Outro meio de procurar uma tag mas em outro bloco de HTML dentro do site:

 # SET_SELECTOR2 = '.date-created.item'
   # for vp2 in response.css(SET_SELECTOR2):
            #         # seletor css para pegar todos elementos de outro bloco da página
            #     DATE_SELECTOR = 'a ::text'


