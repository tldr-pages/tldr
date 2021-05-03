# xh

> Friendly and fast tool for sending HTTP requests.
> More information: <https://github.com/ducaale/xh>.

- Send a GET request:

`xh {{httpbin.org/get}}`

- Send a POST request with a JSON body (key-value pairs are added to a top-level JSON object - e.g. `{"name": "john", "age": 25}`):

`xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- Send a GET request with query parameters (e.g. `first_param=5&second_param=true`):

`xh get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- Send a GET request with a custom header:

`xh get {{httpbin.org/get}} {{header-name:header-value}}`

- Make a GET request and save the response body to a file:

`xh --download {{httpbin.org/json}} --output {{path/to/file}}`
