# քերծվածք

> Վեբ սկանավորման շրջանակ:.
> Լրացուցիչ տեղեկություններ. <https://docs.scrapy.org/en/latest/topics/commands.html#using-the-scrapy-tool>:.

- Ստեղծել նախագիծ.:

`scrapy startproject {{project_name}}`

- Ստեղծեք սարդ (նախագծի գրացուցակում).:

`scrapy genspider {{spider_name}} {{website_domain}}`

- Խմբագրել սարդը (նախագծի գրացուցակում).:

`scrapy edit {{spider_name}}`

- Գործարկել spider-ը (նախագծի գրացուցակում).:

`scrapy crawl {{spider_name}}`

- Վերցրեք վեբ էջը, ինչպես տեսնում է Scrapy-ն, և տպեք աղբյուրը `stdout`-ում:

`scrapy fetch {{url}}`

- Բացեք վեբ էջը լռելյայն դիտարկիչում, ինչպես տեսնում է Scrapy-ը (անջատեք JavaScript-ը լրացուցիչ հավատարմության համար).:

`scrapy view {{url}}`

- Բացեք Scrapy shell-ը URL-ի համար, որը թույլ է տալիս փոխազդել էջի աղբյուրի հետ Python shell-ում (կամ IPython-ի առկայության դեպքում).:

`scrapy shell {{url}}`
