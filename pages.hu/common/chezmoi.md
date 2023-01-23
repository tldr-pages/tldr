# Chezmoi

> Go nyelven írt többgépes dotfile-kezelő. További információ: <https://chezmoi.io>.

- Inicializálja a chezmoi-t a gépén:

`chezmoi init`

- Mondd meg a chezmoi-nak, hogy kezeljen egy dotfile-t:

`chezmoi add {{path/to/file}}`

- Egy követett dotfile forrásállapotának szerkesztése:

`chezmoi edit {{path/to/file}}`

- Nézze meg a chezmoi által végrehajtott változtatásokat:

`chezmoi diff`

- Alkalmazza a változtatásokat:

`chezmoi -v apply`

- A chezmoi beállítása egy másik gépen a meglévő dotfile-ok letöltésével egy Git-tárból:

`chezmoi init {{https://example.com/path/to/repository.git}}`

- A legfrissebb módosítások lekérése egy távoli tárolóból:

`chezmoi update`
