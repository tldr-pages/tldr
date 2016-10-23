# pdftk

> PDF toolkit.

- Extract range:

`pdftk {{input.pdf}} cat {{1-3 5 6-10}} output {{output.pdf}}`

- Merge PDF:

`pdftk {{file1.pdf}} {{file2.pdf}} ... cat output {{output.pdf}}`

- Separate PDF into individual pages:

`pdftk {{input.pdf}} burst`

- Rotate third page by 90 degrees clockwise:

`pdftk {{input.pdf}} cat {{1-2 3east 4-end}} output {{output.pdf}}`

- Rotate all pages by 180 degrees clockwise:

`pdftk {{input.pdf}} cat {{1-endsouth}} output {{output.pdf}}`
