# mogrify

> Edit and transform an image by overwriting the original file.
> More information: <https://manned.org/mogrify>.

- Join images into a single multi-image file:

`mogrify -adjoin {{input-file}} {{input-file}}`

- Set background color:

`mogrify -background color {{input-file}}`

- Set image format type:

`mogrify -format type {{input-file}}`

- Surround image with border:

`mogrify -border geometry {{input-file}}`

- Flip image vertically:

`mogrify -flip {{input-file}}`
