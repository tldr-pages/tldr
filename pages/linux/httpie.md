# httpie

> A human-friendly CLI HTTP tool.

- GET method (default method with no request data):

`http {{https://api.github.com/users}}`

- POST method (default method with request data):

`http {{example.org}} {{hello=World}}`

- POST method with redirected input:

`http {{example.org}} < {{file.json}}`

- PUT method:

`http PUT {{httpbin.org/put}} {{API-Key:foo hello=world}}`

- DELETE method:

`http DELETE {{example.org/todos/7}}`

- Show the whole HTTP exchange (request and response):

`http -v {{example.org}}`

- Download file:

`http --download {{example.org}}`
