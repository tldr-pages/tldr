# identify

> Command-line utility of Image Magick project to describe the format and characteristics of one or more image files.
> More information: <https://imagemagick.org/script/identify.php>.

- Describe the format and basic characteristics of an image:

`identify {{path/to/image}}`

- Describe the format and verbose characteristics of an image:

`identify -verbose {{path/to/image}}`

- Collect dimensions of all JPEG files under current directory:

`identify -format "%f,%w,%h\n" *.{{jpg}} > {{path/to/filelist.csv}}`
