# fmt

> Reformat a text file by joining its paragraphs and limiting the line width to a number of characters (75 by default).
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html>.

- Reformat a file:

`fmt {{path/to/file}}`

- Reformat a file producing output lines of (at most) `n` characters:

`fmt {{[-w|--width]}} {{n}} {{path/to/file}}`

- Reformat a file without joining lines shorter than the given width together:

`fmt {{[-s|--split-only]}} {{path/to/file}}`

- Reformat a file with uniform spacing (1 space between words and 2 spaces between paragraphs):

`fmt {{[-u|--uniform-spacing]}} {{path/to/file}}`
