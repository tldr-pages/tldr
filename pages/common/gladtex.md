# gladtex

> A LaTeX formula preprocessor for HTML files. Converts LaTeX formulas to images.
> More information: <https://humenda.github.io/GladTeX/manpage.html/>.

- Convert to html:

`gladtex {{path/to/input.htex}}`

- Save the converted file to a specific location:

`gladtex {{path/to/input.htex}} -o {{path/to/output.html}}`

- Save the generated images to a specific location:

`gladtex {{path/to/input.htex}} -d {{path/to/image_output_directory}}`

- Set image resolution (in dpi, default is 100):

`gladtex {{path/to/input.htex}} -r {{resolution}}`

- Keep latex files after conversion:

`gladtex {{input_file.htex}} -k`

- Set background and foreground color of the images:

`gladtex {{input_file.htex}} -b {{background_color}} -f {{foreground_color}}`

- Convert Markdown to HTML using `pandoc` and `gladtex`:

`pandoc -s -t html --gladtex {{file.md}} | gladtex -o {{file.html}}`
