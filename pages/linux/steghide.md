# steghide

> Steganography tool for JPEG, BMP, WAV and AU file formats.
> More information: <https://github.com/StefanoDeVuono/steghide>.

- Embed data in a PNG, prompting for a passphrase:

`steghide embed --coverfile {{path/to/image.png}} --embedfile {{path/to/data.txt}}`

- Extract data from a WAV audio file:

`steghide extract --stegofile {{path/to/sound.wav}}`

- Display file information, trying to detect an embedded file:

`steghide info {{path/to/file.jpg}}`

- Embed data in a JPEG image, using maximum compression:

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --compress {{9}}`

- Get the list of supported encryption algorithms and modes:

`steghide encinfo`

- Embed encrypted data in a JPEG image, e.g. with Blowfish in CBC mode:

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --encryption {{blowfish|...}} {{cbc|...}}`
