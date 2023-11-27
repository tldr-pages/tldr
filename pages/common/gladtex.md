# gladtex

> A LaTeX formula preprocessor for HTML files.
> It converts LaTeX formulas to images.
> More information: <https://manned.org/gladtex.1>.

- Convert to html:

`gladtex {{path/to/input.htex}}`

- Save the converted file to a specific location:

`gladtex {{path/to/input.htex}} -o {{path/to/output.html}}`

- Save the generated images to a specific [d]irectory:

`gladtex {{path/to/input.htex}} -d {{path/to/image_output_directory}}`

- Set image [r]esolution (in dpi, default is 100):

`gladtex {{path/to/input.htex}} -r {{resolution}}`

- [k]eep LaTeX files after conversion:

`gladtex {{path/to/input.htex}} -k`

- Set [b]ackground and [f]oreground color of the images:

`gladtex {{path/to/input.htex}} -b {{background_color}} -f {{foreground_color}}`

- Convert Markdown to HTML using `pandoc` and `gladtex`:

`pandoc -s -t html --gladtex {{path/to/input.md}} | gladtex -o {{path/to/output.html}}`
