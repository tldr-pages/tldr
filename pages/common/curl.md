# curl

> Transfers data from or to a server.
> Supports most protocols, including HTTP, FTP, and POP3.
> More information: <https://curl.se>.

- Download the contents of a URL to a file:

`curl {{http://example.com}} --output {{path/to/file}}`

- Download a file, saving the output under the filename indicated by the URL:

`curl --remote-name {{http://example.com/filename}}`

- Download a file, following location redirects, and automatically continuing (resuming) a previous file transfer and return an error on server error:

`curl --fail --remote-name --location --continue-at - {{http://example.com/filename}}`

- Send form-encoded data (POST request of type `application/x-www-form-urlencoded`). Use `--data @file_name` or `--data @'-'` to read from STDIN:

`curl --data {{'name=bob'}} {{http://example.com/form}}`

- Send a request with an extra header, using a custom HTTP method:

`curl --header {{'X-My-Header: 123'}} --request {{PUT}} {{http://example.com}}`

- Send data in JSON format, specifying the appropriate content-type header:

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- Pass a username and password for server authentication:

`curl --user myusername:mypassword {{http://example.com}}`

- Pass client certificate and key for a resource, skipping certificate validation:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
