# wget

> Download files from the Web
> Supports HTTP, HTTPS, and FTP

- Download a URL to a file

`wget -O filename "{{URL}}"`

- Limit download speed

`wget --limit-rate=200k {{URL}}`

- Continue an incomplete download 

`wget -c {{URL}}`

- Download a full website

`wget --mirror -p --convert-links -P ./LOCAL-DIR {{URL}}`

- FTP download with username and password

`wget --ftp-user={{USERNAME}} --ftp-password={{PASSWORD}} {{URL}}`
