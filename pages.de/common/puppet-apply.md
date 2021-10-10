# puppet apply

> Wende ein Puppet-Manifest lokal an.
> Weitere Informationen: <https://puppet.com/docs/puppet/7/man/apply.html>.

- Wende ein Manifest an:

`puppet apply {{pfad/zu/manifest}}`

- Führe Puppetcode aus:

`puppet apply --execute {{code}}`

- Benutze ein bestimmtes Modulverzeichnis und Hiera-Konfigurationsdatei:

`puppet apply --modulepath {{pfad/zu/ordner}} --hiera_config {{pfad/zu/datei}} {{pfad/zu/manifest}}`
