# curl

> Transfers data from or to a server
> Supports most protocols including HTTP, FTP, POP

- Download a URL to a file

`curl "{{URL}}" -o {{filename}}`

- send form-encoded data

`curl --data {{name=bob}} {{http://localhost/form}}`

- send JSON data

`curl -X POST -H "Content-Type: application/json" -d {{'{"name":"bob"}'}} {{http://localhost/login}}`

- specify an HTTP method

`curl -X {{DELETE}} {{http://localhost/item/123}}`

- head request

`curl --head {{http://localhost}}`

- include an extra header

`curl --header "{{X-MyHeader: 123}}" {{http://localhost}}`

- pass a user name and password for server authentication

`curl -u myusername:mypassword {{http://localhost}}`
