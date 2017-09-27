# wget

> Download files from the Web.
> Supports HTTP, HTTPS, and FTP.

- Download the contents of an URL to a file (named "foo" in this case):

`wget {{https://example.com/foo}}`

- Download a single web page and all its resources (scripts, stylesheets, images, etc.):

`wget --page-requisites --convert-links {{https://example.com/somepage.html}}`

- Download a full website, with 3-second intervals between requests:

`wget --mirror --page-requisites --convert-links --wait=3 {{https://example.com}}`

- Download the contents of an URL via authenticated FTP:

`wget --ftp-user={{username}} --ftp-password={{password}} {{ftp://example.com}}`

- Limit download speed to 200 kB/s:

`wget --limit-rate={{200k}} {{https://example.com}}`

- Continue an incomplete download:

`wget -c {{https://example.com}}`

- Retry a given number of times if the download doesn't succeed at first:

`wget -t {{number_of_retries}} {{https://example.com}}`
