# http

> HTTPie: HTTP client, a user-friendly cURL replacement.
> More information: <https://httpie.org>.

- Download a URL to a file:

`http -d {{example.org}}`

- Send form-encoded data:

`http -f {{example.org}} {{name='bob'}} {{profile_picture@'bob.png'}}`

- Send JSON object:

`http {{example.org}} {{name='bob'}}`

- Specify an HTTP method:

`http {{HEAD}} {{example.org}}`

- Include an extra header:

`http {{example.org}} {{X-MyHeader:123}}`

- Pass a user name and password for server authentication:

`http -a {{username:password}} {{example.org}}`

- Specify raw request body via `stdin`:

`cat {{data.txt}} | http PUT {{example.org}}`
