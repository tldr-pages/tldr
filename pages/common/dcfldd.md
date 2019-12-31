# dcfldd

> Enhanced version of dd for forensics and security.
> More information: <http://dcfldd.sourceforge.net/>

- Acquire a disk as raw image and hash the image using sha256 algorithm:

`dcfldd if=/dev/{{disk_device}} of={{file.img}} hash=sha256 hashlog={{file.hash}}`

- Acquire disk as raw and hash each 1GB chunk:

`dcfldd if=/dev/{{disk_device}} of={{file.img}} hash={{hash_algorithm}} hashlog={{file.hash}} hashwindow={{1G}}`
