# curl

> Transfers data from or to a server
> Supports most protocols including HTTP, FTP, POP

- send form-encoded data

`curl --data {{name=bob}} {{http://localhost/form}}`

- send JSON data

`curl -X POST -H "Content-Type: application/json" -d {{'{"name":"bob"}'}} {{http://localhost/login}}`

- specify an HTTP method

`curl -X {{DELETE}} {{http://localhost/item/123}}`

- head request

`curl --head {{http://localhost}}`
