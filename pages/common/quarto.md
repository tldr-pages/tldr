# quarto

> An open-source scientific and technical publishing system built on Pandoc.
> More information: <https://quarto.org/>.

- Create a new project:

`quarto create-project {{path/to/destination_directory}} --type {{book|default|website}}`

- Create a new blog website:

`quarto create-project {{path/to/destination_directory}} --type {{website}} --template {{blog}}`

- Render input file(s) to different formats:

`quarto render {{path/to/file.{{qmd|rmd|ipynb}}}} --to {{html|pdf|docx}}`

- Render and preview a document or a website:

`quarto preview {{path/to/destination_directory|path/to/file}}`

- Publish a document or project to Quarto Pub, Github Pages, RStudio Connect or Netlify:

`quarto publish {{quarto-pub|gh-pages|connect|netlify}}`
