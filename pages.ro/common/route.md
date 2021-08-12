# route

> Utilizați ruta cmd pentru a seta tabelul de rute.

- Afișați informațiile din tabelul de rute:

`route -n`

- Adaugă regulă de traseu:

`sudo route add -net {{ip_address}} netmask {{netmask_address}} gw {{gw_address}}`

- Ștergeți regula rutei:

`sudo route del -net {{ip_address}} netmask {{netmask_address}} dev {{gw_address}}`
