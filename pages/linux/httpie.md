# httpie

> A user friendly command line HTTP tool.

- Send a GET request (default method with no request data):

`http {{https://api.github.com/users}}`

- Send a POST request (default method with request data):

`http {{example.org}} {{hello=World}}`

- Send a POST request with redirected input:

`http {{example.org}} < {{file.json}}`

- Send a PUT request with a given json body:

`http PUT {{httpbin.org/put}} {{hello=world}}`

- Send a DELETE request with a giben header:

`http DELETE {{example.org/todos/7}} {{API-Key:foo}}`

- Show the whole HTTP exchange (both request and response):

`http -v {{example.org}}`

- Download a file:

`http --download {{example.org}}`
