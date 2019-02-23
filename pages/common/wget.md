# wget

> Download files from the Web.
> Supports HTTP, HTTPS, and FTP.

- Download the contents of an URL to a file (named "foo" in this case):

`wget {{https://example.com/foo}}`

- Download the contents of an URL to a file (named "bar" in this case):

`wget -O {{bar}} {{https://example.com/foo}}`

- Download a single web page and all its resources (scripts, stylesheets, images, etc.):

`wget --page-requisites --convert-links {{https://example.com/somepage.html}}`

- Download a full website, with 3-second intervals between requests:

`wget --mirror --page-requisites --convert-links --wait=3 {{https://example.com}}`

- Download all listed files within a directory and its sub-directories (does not download embedded page elements):

`wget --mirror --no-parent {{https://example.com/somepath/}}`

- limit the download speed:

`wget --limit-rate={{300k}} {{https://example.com/somepath/}}`

- Set number of retry attempts to download a file:

`wget -tries={{100}} {{https://example.com/somepath/}}`

- Download a file from a password protected site:

`wget --user={{username}} --password={{password}} {{https://example.com}}`

- Download the contents of an URL via authenticated FTP:

`wget --ftp-user={{username}} --ftp-password={{password}} {{ftp://example.com}}`

- Continue an incomplete download:

`wget -c {{https://example.com}}`

- Enable quiet mode to suppress output:

`wget -q {{https://example.com}}`

- Download a file in background:

`wget -b {{https://example.com/foo}}`

- Download a file to a specific directory:

`wget -P {{path/to/directory}} {{https://example.com/foo}}`

- Download all URLs stored in a text file:

`wget -i {{URLs.txt}}`
