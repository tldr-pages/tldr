# mogrify

> Edit and transform an image by overwriting the original file.
> More information: <https://manned.org/mogrify>.

- Join images into a single multi-image file:

`mogrify -adjoin {{path/to/file1 path/to/file2 ...}}`

- Set the background color:

`mogrify -background color {{path/to/file}}`

- Set the image format type:

`mogrify -format type {{path/to/file}}`

- Surround the image with a border:

`mogrify -border geometry {{path/to/file}}`

- Flip the image vertically:

`mogrify -flip {{path/to/file}}`
