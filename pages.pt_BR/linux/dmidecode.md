# dmidecode

> Exibe em formato de fácil leitura o sumário DMI (também conhecido como SMBIOS).
> Requer privilégio de super usuário.
> Veja também: `inxi`, `lshw`, `hwinfo`.
> Mais informações: <https://manned.org/dmidecode>.

- Exibe o sumário do DMI:

`sudo dmidecode`

- Exibe a versão da BIOS:

`sudo dmidecode {{[-s|--string]}} bios-version`

- Exibe o número de série do sistema:

`sudo dmidecode {{[-s|--string]}} system-serial-number`

- Exibe as informações da BIOS:

`sudo dmidecode {{[-t|--type]}} bios`

- Exibe as informações da CPU:

`sudo dmidecode {{[-t|--type]}} processor`

- Exibe as informações da memória:

`sudo dmidecode {{[-t|--type]}} memory`
