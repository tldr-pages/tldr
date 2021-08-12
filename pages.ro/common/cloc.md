# cloc

> Numărați și calculați diferențele de linii de cod sursă și comentarii.
> Mai multe informaţii: <https://github.com/AlDanial/cloc>

- Numără toate liniile de cod într-un director:

`cloc {{path/to/directory}}`

- Numărați toate liniile de cod dintr-un director, afișând o bară de progres în timpul procesului de numărare:

`cloc --progress=1 {{path/to/directory}}`

- Comparați 2 structuri de directoare și numărați diferențele dintre ele:

`cloc --diff {{path/to/directory/one}} {{path/to/directory/two}}`

- Ignorați fișierele ignorate de VCS, cum ar fi fișierele specificate în `.gitignore`:

`cloc --vcs git {{path/to/directory}}`

- Numără toate liniile de cod într-un director, afișând rezultatele pentru fiecare fișier în loc de fiecare limbă:

`cloc --by-file {{path/to/directory}}`
