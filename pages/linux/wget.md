# wget

Wget is a command-line utility for downloading files from the web.

Wget can be used to download multiple files, resume downloads, download in the background etc using HTTP, HTTPS, and FTP protocols.

- Command Syntax:

`wget [options] [url]`

- Download a file:

`wget http://mirrors.evowise.com/linuxmint/stable/20/linuxmint-20-cinnamon-64bit.iso`

- Resume partially downloaded file:

`wget -c http://mirrors.evowise.com/linuxmint/stable/20/linuxmint-20-cinnamon-64bit.iso`

- Download files in the background:

`wget -b http://mirrors.evowise.com/linuxmint/stable/20/linuxmint-20-cinnamon-64bit.iso`

- Save download file under a different name:

`wget -O LinuxMint20.iso http://mirrors.evowise.com/linuxmint/stable/20/linuxmint-20-cinnamon-64bit.iso`

- Download to a specific directory:

`wget -P /mnt/iso http://mirrors.evowise.com/linuxmint/stable/20/linuxmint-20-cinnamon-64bit.iso`

- Download a file via FTP:

`wget --ftp-user=FTP_USERNAME --ftp-password=FTP_PASSWORD ftp://ftp.example.com/linuxmint-20-cinnamon-64bit.iso`
