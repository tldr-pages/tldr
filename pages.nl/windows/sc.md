# sc

> Communiceer met de Service Control Manager en services.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- Toon de status van een service (geen service naam zal alle services tonen):

`sc.exe query {{service_naam}}`

- Start een service asynchroon:

`sc.exe create {{service_naam}} binpath= {{pad\naar\service_binary_bestand}}`

- Stop een service asynchroon:

`sc.exe delete {{service_naam}}`

- Zet het type van een service:

`sc.exe config {{service_naam}} type= {{service_type}}`
