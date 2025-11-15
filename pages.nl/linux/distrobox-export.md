# distrobox-export

> Exporteer app/service/binary van container naar host-besturingssysteem. Bekijk ook: `tldr distrobox`.
> Meer informatie: <https://distrobox.it/usage/distrobox-export>.

- Exporteer een app van de container naar de host (het desktop pictogram verschijnt in de applicatielijst van uw hostsysteem):

`distrobox-export {{[-a|--app]}} {{pakket}} {{[-ef|--extra-flags]}} "--foreground"`

- Exporteer een binary van de container naar de host:

`distrobox-export {{[-b|--bin]}} {{pad/naar/binary}} {{[-ep|--export-path]}} {{pad/naar/binary_op_host}}`

- Exporteer een binary van de container naar de host (bijv.`$HOME/.local/bin`) :

`distrobox-export {{[-b|--bin]}} {{pad/naar/binary}} {{[-ep|--export-path]}} {{pad/naar/export}}`

- Exporteer een service van de container naar de host (`--sudo` zal de service uitvoeren als root in de container):

`distrobox-export --service {{pakket}} {{[-ef|--extra-flags]}} "--allow-newer-config" {{[-S|--sudo]}}`

- Verwijder een geëxporteerde applicatie:

`distrobox-export {{[-a|--app]}} {{pakket}} {{[-d|--delete]}}`
