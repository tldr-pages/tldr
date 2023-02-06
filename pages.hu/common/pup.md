# pup

> Parancssori HTML elemző eszköz. További információ: <https://github.com/ericchiang/pup>.

- Nyers HTML-fájl átalakítása tisztított, behúzott és színezett formátumba:

`cat {{index.html}} | pup --color`

- HTML szűrése az elemtagok neve alapján:

`cat {{index.html}} | pup '{{tag}}'`

- HTML szűrése id alapján:

`cat {{index.html}} | pup '{{div#id}}'`

- HTML szűrése attribútumérték szerint:

`cat {{index.html}} | pup '{{input[type="text"]}}'`

- A szűrt HTML-elemek és gyermekeik összes szövegének kinyomtatása:

`cat {{index.html}} | pup '{{div}} text{}'`

- HTML nyomtatása JSON-ként:

`cat {{index.html}} | pup '{{div}} json{}'`
