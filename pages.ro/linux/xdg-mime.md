# xdg-mime

> Interogați și gestionați tipurile MIME în conformitate cu standardul XDG.
> Mai multe informaţii: <https://portland.freedesktop.org/doc/xdg-mime.html>

- Afișează tipul MIME al unui fișier:

`xdg-mime query filetype {{path/to/file}}`

- Afișați aplicația implicită pentru deschiderea imaginilor PNG:

`xdg-mime query default {{image/png}}`

- Afișați aplicația implicită pentru deschiderea unui anumit fișier:

`xdg-mime query default $(xdg-mime query filetype {{path/to/file}})`

- Setați imv ca aplicație implicită pentru deschiderea imaginilor PNG și JPEG:

`xdg-mime default {{imv.desktop}} {{image/png}} {{image/jpeg}}`
