# wget2

> An improved version of `wget` for downloading files from the web.
> Supports HTTP, HTTPS, and HTTP/2 protocols with enhanced performance.
> By default, `wget2` uses multiple threads for faster downloads.
> More information: <https://manned.org/wget2>.

- Download the contents of a URL to a file using multiple threads (default behavior differs from `wget`):

`wget2 {{https://example.com/foo}}`

- Limit the number of threads used for downloading (default is 5 threads):

`wget2 --max-threads {{10}} {{https://example.com/foo}}`

- Download a single web page and all its resources (scripts, stylesheets, images, etc.):

`wget2 {{[-p|--page-requisites]}} {{[-k|--convert-links]}} {{https://example.com/somepage.html}}`

- Mirror a website, but do not ascend to the parent directory (does not download embedded page elements):

`wget2 {{[-m|--mirror]}} {{[-np|--no-parent]}} {{https://example.com/somepath/}}`

- Limit the download speed and the number of connection retries:

`wget2 --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/somepath/}}`

- Continue an incomplete download (behavior is consistent with `wget`):

`wget2 {{[-c|--continue]}} {{https://example.com}}`

- Download all URLs stored in a text file to a specific directory:

`wget2 {{[-P|--directory-prefix]}} {{path/to/directory}} {{[-i|--input-file]}} {{URLs.txt}}`

- Download a file from an HTTP server using Basic Auth (also works for HTTPS):

`wget2 --user {{username}} --password {{password}} {{https://example.com}}`
