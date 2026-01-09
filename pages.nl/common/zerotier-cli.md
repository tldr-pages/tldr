# zerotier-cli

> Beheer de lokale ZeroTier virtuele netwerkservice.
> Zie ook: `zerotier-idtool`, `zerotier-one`.
> Meer informatie: <https://github.com/zerotier/ZeroTierOne/blob/main/doc/zerotier-cli.1.md>.

- Verbind met een netwerk:

`sudo zerotier-cli join {{netwerk_id}}`

- Toon netwerken:

`sudo zerotier-cli listnetworks`

- Toon peers in een leesbaar formaat:

`sudo zerotier-cli peers`

- Verlaat een netwerk:

`sudo zerotier-cli leave {{netwerk_id}}`

- Toon de status van ZeroTier One:

`sudo zerotier-cli {{[info|status]}}`
