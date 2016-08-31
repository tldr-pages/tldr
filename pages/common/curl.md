# curl

> Transfers data from or to a server.
> Supports most protocols including HTTP, FTP, POP3.

- Download the contents of an URL to a file:

`curl {{http://example.com}} -o {{filename}}`

- Download a file saving the output under the filename indicated by the URL:

`curl -O {{http://example.com/filename}}`

- Download a file, following [L]ocation redirects, and automatically [C]ontinuing/resuming a previous file transfer:

`curl -O -L -C - {{http://example.com/filename}}`

- Send form-encoded data (POST request of type application/x-www-form-urlencoded):

`curl -d {{'name=bob'}} {{http://example.com/form}}`

- Send data, specifying a custom HTTP method, and including an extra header:

`curl -d {{'{"name":"bob"}'}} -X {{PUT}} -H {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- Pass a user name and password for server authentication:

`curl -u myusername:mypassword {{http://example.com}}`

- Pass client certificate and key for a secure resource:

`curl -v -key {{key.pem}} -cacert {{ca.pem}} -cert {{client.pem}} -k {{https://example.com}}`
