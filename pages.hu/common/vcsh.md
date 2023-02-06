# vcsh

> Verziókezelő rendszer az otthoni könyvtárhoz, amely Git tárolókat használ. További információ: <https://github.com/RichiH/vcsh>.

- Egy (üres) adattár inicializálása:

`vcsh init {{repository_name}}`

- Adattár klónozása egy egyéni könyvtárnévbe:

`vcsh clone {{git_url}} {{repository_name}}`

- Az összes kezelt adattár listázása:

`vcsh list`

- Git parancs végrehajtása egy kezelt adattárban:

`vcsh {{repository_name}} {{git_command}}`

- Az összes kezelt adattár push/pullolása távoli tárolókba/ távoli tárolókból:

`vcsh {{push|pull}}`

- Egyéni `.gitignore` fájl írása egy kezelt tárolóhoz:

`vcsh write-gitignore {{repository_name}}`
