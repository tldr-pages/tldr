# genisoimage

> genisoimage is a pre-mastering program to generate ISO9660/Joliet/HFS hybrid filesystems.
> More information: <https://manpages.debian.org/stretch/genisoimage/genisoimage.1.en.html>.

- Create an ISO image:

`genisoimage -o {{minhaimagem.iso} {{caminho/para/a/pasta/}}`

- Create an ISO image with files larger than 4GB:

`genisoimage -o -allow-limited-size {{myimage.iso} {{path/to/directory/}}`
