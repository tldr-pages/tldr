# lwp-request

> Simple command-line HTTP client.
> Built with libwww-perl.
> More information: <https://metacpan.org/pod/lwp-request>.

- Make a simple GET request:

`lwp-request -m GET {{http://example.com/some/path}}`

- Upload a file with a POST request:

`lwp-request -m POST {{http://example.com/some/path}} < {{path/to/file}}`

- Make a request with a custom user agent:

`lwp-request -H 'User-Agent: {{user_agent}} -m {{METHOD}} {{http://example.com/some/path}}`

- Make a request with HTTP authentication:

`lwp-request -C {{username}}:{{password}} -m {{METHOD}} {{http://example.com/some/path}}`

- Make a request and print request headers:

`lwp-request -U -m {{METHOD}} {{http://example.com/some/path}}`

- Make a request and print response headers and status chain:

`lwp-request -E -m {{METHOD}} {{http://example.com/some/path}}`
