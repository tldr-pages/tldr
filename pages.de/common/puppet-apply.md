# puppet apply

> Wende ein Puppet-Manifest lokal an.
> Weitere Informationen: <https://github.com/puppetlabs/puppet/blob/main/references/man/apply.md>.

- Wende ein Manifest an:

`puppet apply {{pfad/zu/manifest}}`

- Führe Puppetcode aus:

`puppet apply --execute {{code}}`

- Benutze ein bestimmtes Modulverzeichnis und Hiera-Konfigurationsdatei:

`puppet apply --modulepath {{pfad/zu/verzeichnis}} --hiera_config {{pfad/zu/datei}} {{pfad/zu/manifest}}`
