# xh

> Friendly and fast tool for sending HTTP requests.
> Note: `xh`, written in rust, serves as an effective drop-in replacement for `http`.
> See also: `http`, `curl`.
> More information: <https://github.com/ducaale/xh#usage>.

- Send a GET request (shows response headers and content):

`xh {{https://postman-echo.com/get}}`

- Send a POST request with a JSON body (key-value pairs are added to a top-level JSON object - e.g. `{"name": "john", "age": 25}`):

`xh post {{https://postman-echo.com/post}} {{name=john}} {{age=25}}`

- Send a GET request with query parameters (e.g. <https://postman-echo.com/response-headers?foo1=bar1&foo2=bar2>):

`xh get {{https://postman-echo.com/response-headers}} {{foo1==bar1}} {{foo2==bar2}}`

- Send a GET request with a custom header:

`xh get {{https://postman-echo.com}} {{header-name:header-value}}`

- Make a GET request and save the response body to a file:

`xh {{[-d|--download]}} {{https://example.com}} {{[-o|--output]}} {{path/to/file}}`

- Construct a request but do not send it (similar to a dry-run):

`xh --offline {{get|delete|...}} {{https://example.com}}`

- Show equivalent `curl` command (this will not send any request):

`xh --{{curl|curl-long}} {{--follow --verbose get https://example.com user-agent:curl}}`
