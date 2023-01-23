# curlie

> A Curlie egy frontend a curl-hez, amely a httpie egyszerűbb használatát teszi lehetővé. További információ: <https://github.com/rs/curlie>.

- GET-kérés küldése:

`curlie {{httpbin.org/get}}`

- POST kérés küldése:

`curlie post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- GET-kérés küldése lekérdezési paraméterekkel (pl. `first_param=5&second_param=true`):

`curlie get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- GET-kérelem küldése egyéni fejléccel:

`curlie get {{httpbin.org/get}} {{header-name:header-value}}`
