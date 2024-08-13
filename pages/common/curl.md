# curl

> Transfers data from or to a server.
> Supports most protocols, including HTTP, HTTPS, FTP, SCP, etc.
> More information: <https://curl.se/docs/manpage.html>.

- Make an HTTP GET request and dump the contents in `stdout`:

`curl {{https://example.com}}`

- Make an HTTP GET request, fo[L]low any `3xx` redirects, and [D]ump the reply headers and contents to `stdout`:

`curl --location --dump-header - {{https://example.com}}`

- Download a file, saving the [O]utput under the filename indicated by the URL:

`curl --remote-name {{https://example.com/filename.zip}}`

- Send form-encoded [d]ata (POST request of type `application/x-www-form-urlencoded`). Use `--data @file_name` or `--data @'-'` to read from `stdin`:

`curl -X POST --data {{'name=bob'}} {{http://example.com/form}}`

- Send a request with an extra header, using a custom HTTP method and over a pro[x]y (such as BurpSuite), ignoring insecure self-signed certificates:

`curl -k --proxy {{http://127.0.0.1:8080}} --header {{'Authorization: Bearer token'}} --request {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Send data in JSON format, specifying the appropriate Content-Type [H]eader:

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- Pass client certificate and key for a resource, skipping certificate validation:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`

- Resolve a hostname to a custom IP address, with [v]erbose output (similar to editing the `/etc/hosts` file for custom DNS resolution):

`curl --verbose --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
