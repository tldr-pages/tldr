# երթուղի

> Ցույց տալ և շահարկել երթուղու աղյուսակը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/route>:.

- Ցուցադրել երթուղու աղյուսակի տեղեկատվությունը.:

`route -n`

- Ավելացնել երթուղու կանոն.:

`sudo route add -net {{ip_address}} netmask {{netmask_address}} gw {{gw_address}}`

- Ջնջել երթուղու կանոնը.:

`sudo route del -net {{ip_address}} netmask {{netmask_address}} dev {{gw_address}}`
