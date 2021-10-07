# puppet apply

> Wende ein Puppet-Manifest lokal an.
> Weitere Informationen: <https://puppet.com/docs/puppet/7/man/apply.html>.

- Wende das Manifest an:

`puppet apply {{pfad/zum/manifest}}`

- Führe Puppetcode von der Kommandozeile aus:

`puppet apply --execute {{code}}`

- Nutze ein spezifisches Modulverzeichnis und Hiera-Konfigurationsdatei:

`puppet apply --modulepath {{pfad/zum/ordner}} --hiera_config {{pfad/zur/datei}} {{pfad/zum/manifest}}`
