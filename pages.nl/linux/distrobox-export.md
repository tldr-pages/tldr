# distrobox-export

> Exporteer app/service/binary van container naar host-besturingssysteem.
> Subcommando van `distrobox`. Bekijk ook: `tldr distrobox`.
> Meer informatie: <https://distrobox.it/usage/distrobox-export>.

- Exporteer een app van de container naar de host (het desktop pictogram verschijnt in de applicatielijst van uw hostsysteem):

`distrobox-export --app {{pakket}} --extra-flags "--foreground"`

- Exporteer een binary van de container naar de host:

`distrobox-export --bin {{pad/naar/binary}} --export-path {{pad/naar/binary_on_host}}`

- Exporteer een binary van de container naar de host (bijv.`$HOME/.local/bin`) :

`distrobox-export --bin {{pad/naar/binary}} --export-path {{pad/naar/export}}`

- Exporteer een service van de container naar de host (`--sudo` zal de service uitvoeren als root in de container):

`distrobox-export --service {{pakket}} --extra-flags "--allow-newer-config" --sudo`

- Verwijder een geëxporteerde applicatie:

`distrobox-export --app {{pakket}} --delete`
