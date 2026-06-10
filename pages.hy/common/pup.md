#ձագուկ

> HTML վերլուծության գործիք:.
> Լրացուցիչ տեղեկություններ. <https://github.com/ericchiang/pup>:.

- Վերափոխեք չմշակված HTML ֆայլը մաքրված, մատնանշված և գունավոր ձևաչափի.:

`cat {{index.html}} | pup --color`

- Զտել HTML-ն ըստ տարրի պիտակի անվան՝:

`cat {{index.html}} | pup '{{tag}}'`

- Զտել HTML-ը ID-ով.:

`cat {{index.html}} | pup '{{div#id}}'`

- Զտել HTML-ն ըստ հատկանիշի արժեքի.:

`cat {{index.html}} | pup '{{input[type="text"]}}'`

- Տպեք ամբողջ տեքստը զտված HTML տարրերից և նրանց երեխաներից.:

`cat {{index.html}} | pup '{{div}} text{}'`

- Տպել HTML որպես JSON:

`cat {{index.html}} | pup '{{div}} json{}'`
