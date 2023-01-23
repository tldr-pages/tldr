# puppet apply

> A Puppet manifesztek helyi alkalmazása. További információ: <https://puppet.com/docs/puppet/7/man/apply.html>.

- Manifesztum alkalmazása:

`puppet apply {{path/to/manifest}}`

- A puppet kód végrehajtása:

`puppet apply --execute {{code}}`

- Egy adott modul és hiera config fájl használata:

`puppet apply --modulepath {{path/to/directory}} --hiera_config {{path/to/file}} {{path/to/manifest}}`
