# wcurl

> A simple wrapper around `curl` to easily download files.
> See also: `wget`, `curl`.
> More information: <https://curl.se/wcurl/manual.html>.

- Download the contents of a URL to a file indicated by the URL (`index.html` in this case):

`wcurl {{https://example.com/index.html}}`

- Download the contents of a URL to a file with a specified name:

`wcurl {{[-o|--output]}} {{path/to/file}} {{https://example.com/index.html}}`

- Download the contents of a URL, enabling progress bar and defaulting to HTTP/2:

`wcurl --curl-options "--progress-bar --http2" {{https://example.com/index.html}}`

- Resume from an interrupted download:

`wcurl --curl-options "--clobber --continue-at -" {{https://example.com/index.html}}`
