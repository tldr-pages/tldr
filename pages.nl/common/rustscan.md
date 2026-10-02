# rustscan

> Moderne poortscanner geschreven in Rust.
> Opmerking: `nmap` moet geïnstalleerd zijn om sommige onderstaande voorbeelden te laten werken.
> Zie ook: `hping3`, `masscan`, `naabu`, `nmap`, `zmap`.
> Meer informatie: <https://github.com/bee-san/RustScan/wiki>.

- Scan alle poorten van één of meerdere door komma's gescheiden adressen met de standaardwaarden:

`rustscan {{[-a|--addresses]}} {{ip_of_hostnaam1,ip_of_hostnaam2,...}}`

- Scan de top 1000 poorten met service- en versiedetectie:

`rustscan --top {{[-a|--addresses]}} {{adres}}`

- Scan een specifieke lijst van poorten:

`rustscan {{[-p|--ports]}} {{poort1,poort2,...}} {{[-a|--addresses]}} {{adres}}`

- Scan een specifiek bereik van poorten:

`rustscan {{[-r|--range]}} {{start}}-{{einde}} {{[-a|--addresses]}} {{adres}}`

- Roep `nmap`-functionaliteiten aan (Nmap's OS-detectie en standaardscripts):

`rustscan {{[-a|--addresses]}} {{adres}} -- -O {{[-sC|--script=default]}}`

- Scan met een aangepaste batchgrootte (standaard: 4500) en timeout (standaard: 1500ms):

`rustscan {{[-b|--batch-size]}} {{batch_grootte}} {{[-t|--timeout]}} {{timeout}} {{[-a|--addresses]}} {{adres}}`

- Scan met een specifieke poortvolgorde:

`rustscan --scan-order {{serial|random}} {{[-a|--addresses]}} {{adres}}`

- Scan in greppable modus (alleen output van de poorten, geen `nmap`):

`rustscan {{[-g|--greppable]}} {{[-a|--addresses]}} {{adres}}`
