# քառորդ

> Pandoc-ի վրա կառուցված բաց կոդով գիտական և տեխնիկական հրատարակչական համակարգ:.
> Լրացուցիչ տեղեկություններ. <https://quarto.org/docs/reference/projects/options.html>:.

- Ստեղծեք նոր նախագիծ.:

`quarto create-project {{path/to/destination_directory}} --type {{book|default|website}}`

- Ստեղծեք նոր բլոգի կայք.:

`quarto create-project {{path/to/destination_directory}} --type {{website}} --template {{blog}}`

- Ներկայացրեք մուտքային ֆայլ(ներ)ը տարբեր ձևաչափերի.:

`quarto render {{path/to/file.[qmd|rmd|ipynb]}} --to {{html|pdf|docx}}`

- Ներկայացրեք և նախադիտեք փաստաթուղթը կամ կայքէջը.:

`quarto preview {{path/to/destination_directory|path/to/file}}`

- Հրապարակեք փաստաթուղթ կամ նախագիծ Quarto Pub-ում, Github Pages-ում, RStudio Connect-ում կամ Netlify-ում.:

`quarto publish {{quarto-pub|gh-pages|connect|netlify}}`
