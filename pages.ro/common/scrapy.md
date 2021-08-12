# scrapy

> cadru de accesare cu crawlere web.
> Mai multe informaţii: <https://scrapy.org>

- Crearea unui proiect:

`scrapy startproject {{project_name}}`

- Creați un păianjen (în directorul proiectului):

`scrapy genspider {{spider_name}} {{website_domain}}`

- Editează păianjenul (în directorul proiectului):

`scrapy edit {{spider_name}}`

- Rulați păianjen (în directorul proiectului):

`scrapy crawl {{spider_name}}`

- Fetch o pagină web ca scrapy vede și sursa de imprimare în stdout:

`scrapy fetch {{url}}`

- Deschideți o pagină web în browserul implicit așa cum o vede scrapy (dezactivați JavaScript pentru fidelitate suplimentară):

`scrapy view {{url}}`

- Deschideți shell scrapy pentru URL, care permite interacțiunea cu sursa paginii în shell python (sau ipython dacă este disponibil):

`scrapy shell {{url}}`
