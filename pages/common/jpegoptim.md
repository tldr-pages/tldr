# jpegoptim

> Optimise JPEG images.
> More information: <https://manned.org/jpegoptim>.

- Optimise a set of JPEG images, retaining all associated data:

`jpegoptim {{image1.jpeg image2.jpeg image3.jpeg ...}}`

- Optimise JPEG images, stripping all non-essential data:

`jpegoptim {{[-s|--strip-all]}} {{image1.jpeg image2.jpeg image3.jpeg ...}}`

- Force the output images to be progressive:

`jpegoptim --all-progressive {{image1.jpeg image2.jpeg image3.jpeg ...}}`

- Force the output images to have a fixed maximum filesize:

`jpegoptim {{[-S|--size]}} {{250k}} {{image1.jpeg image2.jpeg image3.jpeg ...}}`
