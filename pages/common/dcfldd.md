# dcfldd

> Enhanced version of dd for forensics and security.
> More information: <http://dcfldd.sourceforge.net/>.

- Copy a disk to a raw image file and hash the image using SHA256:

`dcfldd if=/dev/{{disk_device}} of={{file.img}} hash=sha256 hashlog={{file.hash}}`

- Copy a disk to a raw image file, hashing each 1GB chunk:

`dcfldd if=/dev/{{disk_device}} of={{file.img}} hash={{hash_algorithm}} hashlog={{file.hash}} hashwindow={{1G}}`
