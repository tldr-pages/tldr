# zerotier-cli

> Վերահսկեք տեղական ZeroTier վիրտուալ ցանցի ծառայությունը:.
> Տես նաև՝ `zerotier-idtool`, `zerotier-one`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/zerotier/ZeroTierOne/blob/main/doc/zerotier-cli.1.md>:.

- Միացեք ցանցին.:

`sudo zerotier-cli join {{network_id}}`

- Ցուցակ ցանցեր.:

`sudo zerotier-cli listnetworks`

- Ցուցակեք հասակակիցներին ընթեռնելի ձևաչափով.:

`sudo zerotier-cli peers`

- Հեռանալ ցանցից.:

`sudo zerotier-cli leave {{network_id}}`

- Ցուցադրել ZeroTier One-ի կարգավիճակը.:

`sudo zerotier-cli {{[info|status]}}`
