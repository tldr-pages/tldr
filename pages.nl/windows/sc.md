# sc

> Communiceer met de Service Control Manager en services.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/sc-query>.

- Toon de status van een service (geen service naam zal alle services tonen):

`sc query {{service_naam}}`

- Start een service asynchroon:

`sc start {{service_naam}}`

- Stop een service asynchroon:

`sc stop {{service_naam}}`

- Maak een service aan:

`sc create {{service_naam}} binpath= {{pad\naar\service_binary_bestand}}`

- Verwijder een service:

`sc delete {{service_naam}}`

- Zet het type van een service:

`sc config {{service_naam}} type= {{service_type}}`
