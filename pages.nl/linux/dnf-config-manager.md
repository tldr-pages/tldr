# dnf config-manager

> Beheer DNF-configuratie-opties en repositories op Fedora-gebaseerde systemen.
> Meer informatie: <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>.

- Voeg een repository toe (en schakel deze in) vanaf een URL:

`dnf config-manager --add-repo={{repository_url}}`

- Print de huidige configuratiewaarden:

`dnf config-manager --dump`

- Schakel een specifieke repository in:

`dnf config-manager {{[--enable|--set-enabled]}} {{repository_id}}`

- Schakel opgegeven repositories uit:

`dnf config-manager {{[--disable|--set-disabled]}} {{repository_id1 repository_id2 ...}}`

- Stel een configuratieoptie in voor een repository:

`dnf config-manager --setopt={{option}}={{value}}`

- Toon de help:

`dnf config-manager --help-cmd`
