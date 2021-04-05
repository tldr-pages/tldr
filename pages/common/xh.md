# xh

> Friendly and fast tool for sending HTTP requests.
> More information: <https://github.com/ducaale/xh>.

- Send a GET request:

`xh {{httpbin.org/get}}`

- Send a POST request with JSON body (each key specified is added to the top-level JSON object e.g. `{"name": "john", "age": 25}`):

`xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- Send a GET request with query parameters (e.g. `id=5&sort=true`):

`xh get {{httpbin.org/get}} {{id==5}} {{sort==true}}`

- Send a GET request with a custom header:

`xh get {{httpbin.org/get}} {{header-name:header-value}}`

- Send a PUT request and pipe the result to less:

`xh put {{httpbin.org/put}} {{id:=49}} {{age:=25}} | less`

- Make a GET request and save the response body to a file:

`xh --download {{httpbin.org/json}} --output {{path/to/file}}`
