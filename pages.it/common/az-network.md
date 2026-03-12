# az network

> Gestisce le risorse di rete Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/network>.

- Elenca le risorse di rete in una regione che utilizzano la quota di sottoscrizione:

`az network list-usages`

- Elenca tutte le reti virtuali in una sottoscrizione:

`az network vnet list`

- Crea una rete virtuale:

`az network vnet create --address-prefixes {{10.0.0.0/16}} {{[-n|--name]}} {{vnet}} {{[-g|--resource-group]}} {{nome_gruppo}} --subnet-name {{sottorete}} --subnet-prefixes {{10.0.0.0/24}}`

- Abilita il networking accelerato per una scheda di interfaccia di rete:

`az network nic update --accelerated-networking true {{[-n|--name]}} {{nic}} {{[-g|--resource-group]}} {{gruppo_risorse}}`
