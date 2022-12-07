# mogrify

> Edit and transform an image by overwriting the original file.
> More information: <https://manned.org/mogrify>.

- Join images into a single multi-image file:

`mogrify -adjoin {{input_file}} {{input_file}}`

- Set background color:

`mogrify -background color {{input_file}}`

- Set image format type:

`mogrify -format type {{input_file}}`

- Surround the image with a border:

`mogrify -border geometry {{input-file}}`

- Flip the image vertically:

`mogrify -flip {{input-file}}`
