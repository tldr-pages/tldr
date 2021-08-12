# mkvmerge

> Fuzionare şi extragere fluxuri multimedia.
> Mai multe informaţii: <https://mkvtoolnix.download/doc/mkvmerge.html>

- Afișează informații despre un fișier Matroska:

`mkvmerge --identify {{path/to/file.mkv}}`

- Extragerea audio de la piesa 1 a unui anumit fișier:

`mkvextract tracks {{path/to/file.mkv}} {{1}}:{{path/to/output.webm}}`

- Extrageți subtitrarea din piesa 3 a unui anumit fișier:

`mkvextract tracks {{path/to/file.mkv}} {{3}}:{{path/to/subs.srt}}`
