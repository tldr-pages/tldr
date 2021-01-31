# brew bundle

> Bundler für Homebrew, Homebrew Cask und den Mac App Store.
> Mehr Informationen: <https://github.com/Homebrew/homebrew-bundle>.

- Installieren von Paketen welche im Brewfile (im gleichem Pfad) sind:

`brew bundle`

- Installieren von Paketen welche im Brewfile sind (das Brewfile liegt nicht im aktuellen Pfad):

`brew bundle --file={{path/to/file}}`

- Mach eine Liste mit aller installierter Software:

`brew bundle dump`

- Deinstalliert Software die nicht im Brewfile aufgelisted sind:

`brew bundle cleanup --force`

- Prüfe ob eine Software installiert oder updated werden muss:

`brew bundle check`

- Zeige alle Software welche im Brewfile aufgelistet sind:

`brew bundle list --all`
