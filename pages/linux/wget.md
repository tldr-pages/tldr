# wget

> Wget is a computer program that retrieves content from web servers. It supports downloading via HTTP, HTTPS, and FTP protocols.

* Download a file form the internet, knowing the IP and location of the file.

`wget {{http://exemple.com/cats.jpg}}`

* Download Wget's source code from the GNU ftp site.

`wget {{ftp://ftp.gnu.org/pub/gnu/wget/wget-latest.tar.gz}}`

* Download the title page of example.com, along with the images and style sheets needed to display the page, and convert the URLs inside it to refer to locally available content.

`wget -p -k {{http://www.example.com/}}`
