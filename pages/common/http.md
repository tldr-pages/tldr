# http

> HTTPie: HTTP client, aims to be easier to use than cURL.
> More information: <https://httpie.org>.

- Download a URL to a file:

`http --download {{example.org}}`

- Send form-encoded data:

`http --form {{example.org}} {{name='bob'}} {{profile_picture@'bob.png'}}`

- Send JSON object:

`http {{example.org}} {{name='bob'}}`

- Specify an HTTP method:

`http {{HEAD}} {{example.org}}`

- Include an extra header:

`http {{example.org}} {{X-MyHeader:123}}`

- Pass a username and password for server authentication:

`http --auth {{username:password}} {{example.org}}`

- Specify raw request body via stdin:

`cat {{data.txt}} | http PUT {{example.org}}`
