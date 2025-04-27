# steghide

> Steganography tool for JPEG, BMP, WAV and AU file formats.
> More information: <https://manned.org/steghide>.

- Embed data in a PNG, prompting for a passphrase:

`steghide embed {{[-cf|--coverfile]}} {{path/to/image.png}} {{[-ef|--embedfile]}} {{path/to/data.txt}}`

- Extract data from a WAV audio file:

`steghide extract {{[-sf|--stegofile]}} {{path/to/sound.wav}}`

- Display file information, trying to detect an embedded file:

`steghide info {{path/to/file.jpg}}`

- Embed data in a JPEG image, using maximum compression:

`steghide embed {{[-cf|--coverfile]}} {{path/to/image.jpg}} {{[-ef|--embedfile]}} {{path/to/data.txt}} {{[-z|--compress]}} {{9}}`

- Get the list of supported encryption algorithms and modes:

`steghide encinfo`

- Embed encrypted data in a JPEG image, e.g. with Blowfish in CBC mode:

`steghide embed {{[-cf|--coverfile]}} {{path/to/image.jpg}} {{[-ef|--embedfile]}} {{path/to/data.txt}} {{[-e|--encryption]}} {{blowfish|...}} {{cbc|...}}`
