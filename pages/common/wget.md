# wget

> Download files from the Web.
> Supports HTTP, HTTPS, and FTP.
> More information: <https://www.gnu.org/software/wget>.

- Download the contents of an URL to a file (named "foo" in this case):

`wget {{https://example.com/foo}}`

- Download the contents of an URL to a file (named "bar" in this case):

`wget -O {{bar}} {{https://example.com/foo}}`

- Download a single web page and all its resources with 3-second intervals between requests (scripts, stylesheets, images, etc.):

`wget --page-requisites --convert-links --wait=3 {{https://example.com/somepage.html}}`

- Download all listed files within a directory and its sub-directories (does not download embedded page elements):

`wget --mirror --no-parent {{https://example.com/somepath/}}`

- Limit the download speed and the number of connection retries:

`wget --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}`

- Download a file from an HTTP server using Basic Auth (also works for FTP):

`wget --user={{username}} --password={{password}} {{https://example.com}}`

- Continue an incomplete download:

`wget -c {{https://example.com}}`

- Download all URLs stored in a text file to a specific directory:

`wget -P {{path/to/directory}} -i {{URLs.txt}}`
