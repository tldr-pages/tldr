# jpegoptim

> Optimise JPEG images.

- Optimise a set of JPEG images, retaining all associated data:

`jpegoptim {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- Optimise JPEG images, stripping all non-essential data:

`jpegoptim --strip-all {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- Force the output images to be progressive:

`jpegoptim --all-progressive {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- Force the output images to be fixed max size:

`jpegoptim --size={{250k}} {{image1.jpeg}} {{image2.jpeg}} {{imageN.jpeg}}`

- Recursive folder optimization:

`find {{.}} -name "{{*.jpg}}" -exec jpegoptim --strip-all --all-progressive --size={{250k}} {} \;`
