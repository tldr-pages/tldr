# git check-ignore

> Analizați și depanați Git ignorați/excludeți („.gitignore”) fișiere.
> Mai multe informaţii: <https://git-scm.com/docs/git-check-ignore>

- Verificați dacă un fișier sau un director este ignorat:

`git check-ignore {{path/to/file_or_directory}}`

- Verificați dacă mai multe fișiere sau directoare sunt ignorate:

`git check-ignore {{path/to/file}} {{path/to/directory}}`

- Folosește nume de cai, câte unul pe linie, de la stdin:

`git check-ignore --stdin < {{path/to/file_list}}`

- Nu verificați indexul (folosit pentru a depana de ce traseele au fost urmărite și nu ignorate):

`git check-ignore --no-index {{path/to/files_or_directories}}`

- Includeți detalii despre modelul de potrivire pentru fiecare cale:

`git check-ignore --verbose {{path/to/files_or_directories}}`
