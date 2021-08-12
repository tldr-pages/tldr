# wol

> Client pentru trimiterea pachetelor magice Wake-on-LAN.
> Mai multe informaţii: <https://sourceforge.net/projects/wake-on-lan/>

- Trimiteți un pachet Wol la un dispozitiv:

`wol {{mac_address}}`

- Trimiteți un pachet Wol la un dispozitiv într-o altă subrețea bazată pe IP-ul său:

`wol --ipaddr={{ip_address}} {{mac_address}}`

- Trimiteți un pachet Wol la un dispozitiv într-o altă subrețea bazată pe numele gazdei sale:

`wol --host={{hostname}} {{mac_address}}`

- Trimiteți un pachet Wol la un anumit port pe o gazdă:

`wol --port={{port_number}} {{mac_address}}`

- Citiți adrese hardware, adrese IP/nume de gazdă, porturi opționale și parole SecureOn dintr-un fișier:

`wol --file={{path/to/file}}`

- Activați ieșirea verbose:

`wol --verbose {{mac_address}}`
