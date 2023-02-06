# scrapy

> Web-crawling keretrendszer. További információ: <https://scrapy.org>.

- Hozzon létre egy projektet:

`scrapy startproject {{project_name}}`

- Hozzon létre egy pókot (a projekt könyvtárban):

`scrapy genspider {{spider_name}} {{website_domain}}`

- Pók szerkesztése (a projektkönyvtárban):

`scrapy edit {{spider_name}}`

- Futtassa a pókot (a projektkönyvtárban):

`scrapy crawl {{spider_name}}`

- A Scrapy által látott weblap lekérdezése és a forrás kinyomtatása a `stdout` címre:

`scrapy fetch {{url}}`

- Nyisson meg egy weboldalt az alapértelmezett böngészőben úgy, ahogy a Scrapy látja (kapcsolja ki a JavaScriptet az extra hűség érdekében):

`scrapy view {{url}}`

- Nyissa meg a Scrapy shell-t az URL-hez, ami lehetővé teszi az interakciót az oldal forrásával egy Python shell-ben (vagy IPythonban, ha van):

`scrapy shell {{url}}`
