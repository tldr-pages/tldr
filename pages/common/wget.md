# wget

> Download files from the Web.
> Supports HTTP, HTTPS, and FTP.

- Download the contents of an URL to a file:

`wget -O {{filename}} {{url}}`

- Limit download speed:

`wget --limit-rate={{200k}} {{url}}`

- Continue an incomplete download:

`wget -c {{url}}`

- Download a full website:

`wget --mirror -p --convert-links -P {{target_folder}} {{url}}`

- FTP download with username and password:

`wget --ftp-user={{username}} --ftp-password={{password}} {{url}}`

- Retry a given number of times if the download doesn't succeed at first:

`wget -t {{number_of_retries}} {{url}}`
