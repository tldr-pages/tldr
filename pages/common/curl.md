# curl

> Transfers data from or to a server.
> Supports most protocols including HTTP, FTP, POP.

- Download a URL to a file:

`curl "{{URL}}" -o {{filename}}`

- Send form-encoded data:

`curl --data {{name=bob}} {{http://localhost/form}}`

- Send JSON data:

`curl -X POST -H "Content-Type: application/json" -d {{'{"name":"bob"}'}} {{http://localhost/login}}`

- Specify an HTTP method:

`curl -X {{DELETE}} {{http://localhost/item/123}}`

- Head request:

`curl --head {{http://localhost}}`

- Include an extra header:

`curl -H "{{X-MyHeader: 123}}" {{http://localhost}}`

- Pass a user name and password for server authentication:

`curl -u myusername:mypassword {{http://localhost}}`

- Pass client certificate and key for a secure resource:

`curl -v -key {{key.pem}} -cacert {{ca.pem}} -cert {{client.pem}} -k {{https://localhost}}`
