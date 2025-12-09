# aa-disable

> Schakel AppArmor-beveiligingsprofielen uit.
> Zie ook: `aa-complain`, `aa-enforce`, `aa-status`.
> Meer informatie: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Schakel een profiel uit:

`sudo aa-disable {{pad/naar/profiel1 pad/naar/profiel2 ...}}`

- Schakel profielen uit (standaard naar `/etc/apparmor.d`):

`sudo aa-disable --dir {{pad/naar/profielen}}`
