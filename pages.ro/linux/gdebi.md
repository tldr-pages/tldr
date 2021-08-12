# gdebi

> Instrument simplu pentru a instala fișiere `.deb`.
> Mai multe informaţii: <https://www.commandlinux.com/man-page/man1/gdebi.1.html>

- Instalați pachete locale `.deb` pentru rezolvarea și instalarea dependențelor sale:

`gdebi {{path/to/package.deb}}`

- Afișează versiunea programului:

`gdebi --version`

- Nu afișați informații despre progres:

`gdebi {{path/to/package.deb}} --quiet`

- Setați o opțiune de configurare APT:

`gdebi {{path/to/package.deb}} --option={{APT_OPTS}}`

- Utilizați rădăcină alternativă dir:

`gdebi {{path/to/package.deb}} --root={{path/to/root_dir}}`
