# gphoto2

> Control digital cameras from the command line.
> More information: <http://www.gphoto.org/doc/manual/ref-gphoto2-cli.html>.

- List connected cameras:

`gphoto2 --auto-detect`

- List files on the camera:

`gphoto2 {{[-L|--list-files]}}`

- Download all images:

`gphoto2 {{[-P|--get-all-files]}}`

- Download only new images (skip existing):

`gphoto2 {{[-P|--get-all-files]}} --new`

- Download files 1 through 5:

`gphoto2 {{[-p|--get-file]}} 1-5`

- Delete all files on the camera:

`gphoto2 {{[-D|--delete-all-files]}}`

- Capture an image and download it:

`gphoto2 --capture-image-and-download`

- Show camera information:

`gphoto2 --summary`
