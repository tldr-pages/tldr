# gallery-dl

> Download image galleries and collections from many different sites.
> More information: <https://github.com/mikf/gallery-dl>

- Download images from the specified URL:

`gallery-dl <url>`

> ===================output options===================

- To set the destination for downloads, use the "-d / --destination" switch.

`gallery-dl -d folder <url>`

- Note that that this switch will still create a subfolder for its respective site. 
- For example downloading from twitter and using "-d folder" will put the downloads in "folder/twitter"

- If you want to avoid that, use "-D / --directory" instead.

> ===================input options===================

- URLs can also be read from a text file with "-i / --input-file"
- To have urls be commented out after downloading, "-I / --input-file-comment" can be used instead. 
- To delete the urls, use "-x / --input-file-delete". Failed urls will not be commented or deleted.

`gallery-dl -i list.txt -i optionallist2.txt`

> ===================login options===================

- Use "-u / --username" to provide the username to login with (or set it in the config file)
- Use "-p / --password" to provide the password to login with

- To use a cookies.txt file, use "-C / --cookies"

`gallery-dl -C cookies.txt <url>`

- To use cookies from a browser, use "--cookies-from-browser"

`gallery-dl --cookies-from-browser firefox`

> ===================selection options===================

- To specify a range to start at, stop at, or go through, use "--range". 
- Note: gallery-dl starts counting at 1, so if you have 70 files downloaded you can specify 70 and gallery-dl will start at pos 70
- Using "--range" to start at 50: (when starting, 50- and 50: will work the same)

`gallery-dl --range 50- <url>`

- Using "--range" to stop at 50: (or "-50" with quotes)

`gallery-dl --range :50 <url>`

- Using "--range" to download 6 - 50: (6-50 is also acceptable)

`gallery-dl --range 6:50 <url>`
