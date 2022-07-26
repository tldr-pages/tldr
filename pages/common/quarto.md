# quarto

> An open-source scientific and technical publishing system built on Pandoc.
> More information: <https://quarto.org/>.

- Create a Quarto project:

`quarto create-project {{path/to/project}}`

- Create a new website project:

`quarto create-project {{destination_directory}} --type website`

- Create a new book project:

`quarto create-project {{destination_directory}} --type book`

- Render an R Markdown file to HTML:

`quarto render {{path/to/file.rmd}} --to html`

- Render a Quarto file to HTML:

`quarto render {{input.qmd}} --to html`

- Render Jupyter notebooks to HTML:

`quarto render {{input.ipynb}} --to html`

- Render document to PDF:

`quarto render {{input.qmd}} --to pdf`

- Render document to Microsoft docx document:

`quarto render {{input.qmd}} --to docx`
