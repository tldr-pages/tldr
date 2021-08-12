# rm

> Eliminați fișiere sau directoare.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/rm>

- Eliminați fișierele din locații arbitrare:

`rm {{path/to/file}} {{path/to/another/file}}`

- Eliminați recursiv un director și toate subdirectoarele sale:

`rm -r {{path/to/directory}}`

- Eliminați forțat un director, fără a solicita confirmarea sau afișarea mesajelor de eroare:

`rm -rf {{path/to/directory}}`

- Eliminați interactiv mai multe fișiere, cu o solicitare înainte de fiecare eliminare:

`rm -i {{file(s)}}`

- Eliminați fișierele în modul verbose, tipăriți un mesaj pentru fiecare fișier eliminat:

`rm -v {{path/to/directory/*}}`
