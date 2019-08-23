# dmidecode

> Exibe em formato de fácil leitura o sumário DMI (também conhecido como SMBIOS) .
> Requer privilégio de super usuário.

- Exibir o sumário do DMI:

`sudo dmidecode`

- Exibir a versão da BIOS:

`sudo dmidecode -s bios-version`

- Exibir o número de série do sistema:

`sudo dmidecode -s system-serial-number`

- Exibir as informações da BIOS:

`sudo dmidecode -t bios`

- Exibir as informações da CPU:

`sudo dmidecode -t processor`

- Exibir as informações da memória:

`sudo dmidecode -t memory`
