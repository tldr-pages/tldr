# jp2a

> Convert JPEG images to ASCII.
> More information: <https://csl.name/jp2a/>.

- Read JPEG image from a file and print in ASCII:

`jp2a {{path/to/image.jpeg}}`

- Read JPEG image from a URL and print in ASCII:

`jp2a {{www.example.com/image.jpeg}}`

- Colorize the ASCII output:

`jp2a --colors {{path/to/image.jpeg}}`

- Specify characters to be used for the ASCII output:

`jp2a --chars='{{..-ooxx@@}}' {{path/to/image.jpeg}}`

- Write the ASCII output into a file:

`jp2a --output={{path/to/output_file.txt}} {{path/to/image.jpeg}}`

- Write the ASCII output in HTML file format, suitable for viewing in web browsers:

`jp2a --html --output={{path/to/output_file.html}} {{path/to/image.jpeg}}`
