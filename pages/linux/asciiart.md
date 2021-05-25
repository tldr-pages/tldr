# asciiart

> Convert images to ASCII.
> More information: <https://github.com/nodanaonlyzuul/asciiart>.

- Read an image from a file and print in ASCII:

`asciiart {{path/to/image.jpg}}`

- Read an image from a URL and print in ASCII:

`asciiart {{www.example.com/image.jpg}}`

- Choose the output width (default is 100):

`asciiart -width {{50}} {{path/to/image.jpg}}`

- Colorize the ASCII output:

`asciiart --color {{path/to/image.jpg}}`

- Choose the output format (default format is text):

`asciiart --format {{text|html}} {{path/to/image.jpg}}`

- Invert the character map:

`asciiart --invert-chars {{path/to/image.jpg}}`
