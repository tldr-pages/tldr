# quarto

> An open-source scientific and technical publishing system built on Pandoc.
> More information: <https://quarto.org/>.

- Create a Quarto project:

`quarto create-project {{path/to/project}}`

- Create a new website project:

`quarto create-project {{path/to/destination_directory}} --type {{website}}`

- Create a new book project:

`quarto create-project {{path/to/destination_directory}} --type {{book}}`

- Render an R Markdown file to HTML:

`quarto render {{path/to/file.rmd}} --to {{html}}`

- Render a Quarto file to HTML:

`quarto render {{path/to/file.qmd}} --to {{html}}`

- Render a Jupyter notebook to HTML:

`quarto render {{path/to/file.ipynb}} --to {{html}}`

- Render an R Markdown, Jupyter, or Quarto file to PDF:

`quarto render {{path/to/file}} --to {{pdf}}`

- Render an R Markdown, Jupyter, or Quarto file to a Microsoft `docx` document:

`quarto render {{path/to/file}} --to {{docx}}`
