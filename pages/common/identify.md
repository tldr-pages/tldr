# identify

> Image magick command.

- Collect dimensions of all jpeg files under current directory:

`identify -format "%f,%w,%h\n" *.jpg > filelist.csv`
