# asciiart

> Convert images to ASCII.
> More information: <https://github.com/nodanaonlyzuul/asciiart>.

- Read an image from a file and print in ASCII:

`asciiart {{path/to/image.jpg}}`

- Read an image from a URL and print in ASCII:

`asciiart {{www.example.com/image.jpg}}`

- Choose the output width (default is 100):

`asciiart {{[-w|--width]}} {{50}} {{path/to/image.jpg}}`

- Colorize the ASCII output:

`asciiart {{[-c|--color]}} {{path/to/image.jpg}}`

- Choose the output format (default format is text):

`asciiart {{[-f|--format]}} {{text|html}} {{path/to/image.jpg}}`

- Invert the character map:

`asciiart {{[-i|--invert-chars]}} {{path/to/image.jpg}}`
