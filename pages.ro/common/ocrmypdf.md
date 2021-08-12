# ocrmypdf

> Generaţi un PDF sau un PDF/A care poate fi căutat dintr-un PDF scanat sau o imagine de text.
> Mai multe informaţii: <https://ocrmypdf.readthedocs.io/en/latest/cookbook.html>

- Creați un nou fișier PDF/A care poate fi căutat dintr-un fișier PDF sau imagine scanat:

`ocrmypdf {{path/to/input_file}} {{path/to/output.pdf}}`

- Înlocuiți un fișier PDF scanat cu un fișier PDF care poate fi căutat:

`ocrmypdf {{path/to/input.pdf}}`

- Săriți paginile unui fișier PDF de intrare format mixt care conține deja text:

`ocrmypdf --skip-text {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Curățați, dezînclinați și rotiți paginile unei scanări slabe:

`ocrmypdf --clean --deskew --rotate-pages {{path/to/input_file}} {{path/to/output.pdf}}`

- Setați metadatele fișierului PDF căutat:

`ocrmypdf --title "{{title}}" --author "{{author}}" --subject "{{subject}}" --keywords "{{keyword; key phrase; ...}}" {{path/to/input_file}} {{path/to/output.pdf}}`

- Ajutor pentru afișare:

`ocrmypdf --help`
