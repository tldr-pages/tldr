# webpack

> Bundați fișierele js ale unui proiect web și alte materiale într-un singur fișier de ieșire.
> Mai multe informaţii: <https://webpack.js.org>

- Creați un singur fișier de ieșire dintr-un fișier punct de intrare:

`webpack {{app.js}} {{bundle.js}}`

- Încărcați fișiere css prea din fișierul js (acesta folosește încărcătorul css pentru fișierele `.css`):

`webpack {{app.js}} {{bundle.js}} --module-bind 'css=css'`

- Treceți un fișier de configurare (cu ex. scriptul de intrare și numele fișierului de ieșire) și arătați progresul compilării:

`webpack --config {{webpack.config.js}} --progress`

- Recompilarea automată a modificărilor la fișierele de proiect:

`webpack --watch {{app.js}} {{bundle.js}}`
