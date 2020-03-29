# steghide

> Steganography tool for JPEG, BMP, WAV and AU file formats.
> More information: <https://github.com/StefanoDeVuono/steghide>.

- Embed data in a PNG image:

`steghide embed --coverfile {{path/to/image.png}} --embedfile {{path/to/data.txt}} --passphrase "{{s3cr3t}}"`

- Extract data from a WAV audio file:

`steghide extract --stegofile {{path/to/sound.wav}} --passphrase "{{s3cr3t}}"`

- Display file information, trying to detect an embedded file:

`steghide info {{path/to/file.jpg}}`

- Embed data in a JPG image, compressing it at its maximum:

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --passphrase "{{s3cr3t}}" --compress {{9}}`

- Get the list of supported encryption algorithms and modes:

`steghide encinfo`

- Embed data in a JPG image, encrypted with Blowfish in ECB mode:

`steghide embed --coverfile {{path/to/image.jpg}} --embedfile {{path/to/data.txt}} --passphrase "{{s3cr3t}}" --encryption {{blowfish}} {{ecb}}`
