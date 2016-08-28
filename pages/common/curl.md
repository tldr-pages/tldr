# curl

> Transfers data from or to a server.
> Supports most protocols including HTTP, FTP, POP.

- Download a URL to a file:

`curl {{http://example.com}} -o {{filename}}`

- Download file using remote name:

`curl -O {{http://example.com/filename}}`

- Automatically continue/resume previous file transfer:

`curl -O -C - {{http://example.com/filename}}`

- Send form-encoded data:

`curl --data {{name=bob}} {{http://example.com/form}}`

- Send JSON data:

`curl -X POST -H "Content-Type: application/json" -d {{'{"name":"bob"}'}} {{http://example.com/login}}`

- Specify an HTTP method:

`curl -X {{DELETE}} {{http://example.com/item/123}}`

- Head request:

`curl --head {{http://example.com}}`

- Include an extra header:

`curl -H "{{X-MyHeader: 123}}" {{http://example.com}}`

- Pass a user name and password for server authentication:

`curl -u myusername:mypassword {{http://example.com}}`

- Pass client certificate and key for a secure resource:

`curl -v -key {{key.pem}} -cacert {{ca.pem}} -cert {{client.pem}} -k {{https://example.com}}`
