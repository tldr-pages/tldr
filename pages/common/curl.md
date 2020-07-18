# curl

> Transfers data from or to a server.
> Supports most protocols, including HTTP, FTP, and POP3.
> More information: <https://curl.haxx.se>.

- Download the contents of an URL to a file:

`curl {{http://example.com}} -o {{filename}}`

- Download a file, saving the output under the filename indicated by the URL:

`curl -O {{http://example.com/filename}}`

- Download a file, following [L]ocation redirects, and automatically [C]ontinuing (resuming) a previous file transfer:

`curl -O -L -C - {{http://example.com/filename}}`

- Send form-encoded data (POST request of type `application/x-www-form-urlencoded`). Use `-d @file_name` or `-d @'-'` to read from STDIN:

`curl -d {{'name=bob'}} {{http://example.com/form}}`

- Send a request with an extra header, using a custom HTTP method:

`curl -H {{'X-My-Header: 123'}} -X {{PUT}} {{http://example.com}}`

- Send data in JSON format, specifying the appropriate content-type header:

`curl -d {{'{"name":"bob"}'}} -H {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- Pass a user name and password for server authentication:

`curl -u myusername:mypassword {{http://example.com}}`

- Pass client certificate and key for a resource, skipping certificate validation:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
