# identify

> Describe the format and characteristics of one or more image files.
> Part of ImageMagick.
> More information: <https://imagemagick.org/script/identify.php>.

- Describe the format and basic characteristics of an image:

`identify {{path/to/image}}`

- Describe the format and verbose characteristics of an image:

`identify -verbose {{path/to/image}}`

- Collect dimensions of all JPEG files in the current directory and save them into a CSV file:

`identify -format "{{%f,%w,%h\n}}" {{*.jpg}} > {{path/to/filelist.csv}}`
