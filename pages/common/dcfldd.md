# dcfldd

> Enhanced version of dd for forensics and security.
> More information: <http://dcfldd.sourceforge.net/>.

- Copy a disk to a raw image file and hash the image using SHA256:

`dcfldd if=/dev/{{disk_device}} of={{path/to/file.img}} hash=sha256 hashlog={{path/to/file.hash}}`

- Copy a disk to a raw image file, hashing each 1 GB chunk:

`dcfldd if=/dev/{{disk_device}} of={{path/to/file.img}} hash={{sha512|sha384|sha256|sha1|md5}} hashlog={{path/to/file.hash}} hashwindow={{1G}}`
