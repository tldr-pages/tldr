# gphoto2

> Control digital camera from the command line.
> More information: <http://www.gphoto.org/doc/manual/>.

- List connected cameras:

`gphoto2 --auto-detect`

- List files on the camera:

`gphoto2 --list-files`

- Download all images:

`gphoto2 --get-all-files`

- Download only new images (skip existing):

`gphoto2 --get-all-files --new`

- Download specific files by range:

`gphoto2 --get-file {{1-5}}`

- Delete all files on the camera:

`gphoto2 --delete-all-files`

- Capture an image and download it:

`gphoto2 --capture-image-and-download`

- Show camera information:

`gphoto2 --summary`
