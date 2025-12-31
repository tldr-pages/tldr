# scanimage

> Scan images with the Scanner Access Now Easy API.
> More information: <http://sane-project.org/man/scanimage.1.html>.

- List available scanners to ensure the target device is connected and recognized:

`scanimage {{[-L|--list-devices]}}`

- Scan an image and save it to a file:

`scanimage --format {{pnm|tiff|png|jpeg|pdf|...}} > {{path/to/new_image}}`

- Specify the device to scan from:

`scanimage {{[-d|--device]}} {{device_name}} > {{path/to/new_image}}`

- Specify resolution for the scanned image (default resolution is 75dpi):

`scanimage --resolution {{300}} > {{path/to/new_image}}`
