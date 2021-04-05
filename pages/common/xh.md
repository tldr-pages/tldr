# xh

> XH: Friendly and fast tool for sending HTTP requests.
> More information: <https://github.com/ducaale/xh>.

- Send a GET request:

`xh {{httpbin.org/get}}`

- Send a POST request with JSON body: `{"name": "ahmed", "age": 25}`:

`xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- Send a GET request with querystring id=5&sort=true:

`xh get {{httpbin.org/get}} {{id==5}} {{sort==true}}`

- Send a GET request and include a header named x-api-key with value 12345:

`xh get {{httpbin.org/get}} {{x-api-key:12345}}`

- Send a PUT request and pipe the result to less:

`xh put {{httpbin.org/put}} {{id:=49}} {{age:=25}} | less`

- Download and save to res.json:

`xh -d {{httpbin.org/json}} -o {{res.json}}`
