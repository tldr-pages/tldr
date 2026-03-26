# oha

> HTTP load generator inspired by rakyll/hey with real-time TUI animation.
> More information: <https://github.com/hatoo/oha>.

- Send 200 requests to a URL with 50 concurrent connections:

`oha "{{https://example.com}}"`

- Send requests for a specific duration:

`oha {{[-z|--duration]}} {{30s}} "{{https://example.com}}"`

- Send a specific number of requests:

`oha -n {{1000}} "{{https://example.com}}"`

- Send requests with a specific HTTP method and header:

`oha {{[-m|--method]}} {{POST}} -H "{{Content-Type: application/json}}" "{{https://example.com/api}}"`

- Send requests with a request body:

`oha {{[-m|--method]}} {{POST}} -d '{{{"key": "value"}}}' "{{https://example.com/api}}"`

- Limit the rate of requests per second:

`oha -q {{100}} "{{https://example.com}}"`

- Disable the real-time TUI and output results directly:

`oha --no-tui "{{https://example.com}}"`

- Output results in JSON format:

`oha --no-tui {{[-o|--output]}} {{path/to/results.json}} --output-format {{json}} "{{https://example.com}}"`
