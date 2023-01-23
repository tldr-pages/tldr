# quarto

> Pandoc-ra épülő nyílt forráskódú tudományos és műszaki publikációs rendszer. További információ: <https://quarto.org/>.

- Új projekt létrehozása:

`quarto create-project {{path/to/destination_directory}} --type {{book|default|website}}`

- Új blog weboldal létrehozása:

`quarto create-project {{path/to/destination_directory}} --type {{website}} --template {{blog}}`

- Bemeneti fájl(ok) különböző formátumokba történő renderelése:

`quarto render {{path/to/file.{{qmd|rmd|ipynb}}}} --to {{html|pdf|docx}}`

- Dokumentum vagy weboldal renderelése és előnézete:

`quarto preview {{path/to/destination_directory|path/to/file}}`

- Dokumentum vagy projekt közzététele a Quarto Pub, a Github Pages, az RStudio Connect vagy a Netlify oldalon:

`quarto publish {{quarto-pub|gh-pages|connect|netlify}}`
