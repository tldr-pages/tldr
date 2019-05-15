# route

> Use route cmd to set the route table.

- Display the information of route table:

`route -n`

- Add route rule:

`sudo route add -net {{ip_address}} netmask {{netmask_address}} gw {{gw_address}}`

- Delete route rule:

`sudo route del -net {{ip_address}} netmask {{netmask_address}} dev {{gw_address}}`
