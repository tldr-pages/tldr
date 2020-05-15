# identify

> Command line utility of Image Magick project to describe the format and characteristics of one or more image files.
> More information: <https://imagemagick.org/script/identify.php>.

- Collect dimensions of all jpeg files under current directory:

`identify -format "%f,%w,%h\n" *.{{jpg}} > {{filelist.csv}}`
