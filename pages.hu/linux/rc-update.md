# rc-update

> OpenRC szolgáltatások hozzáadása és eltávolítása a futtatási szintekhez, illetve azokból. Lásd még: `openrc`. További információ: <https://manned.org/rc-update>.

- Az összes szolgáltatás és a hozzájuk hozzáadott futási szintek listája:

`rc-update show`

- Szolgáltatás hozzáadása egy runlevelhez:

`sudo rc-update add {{service_name}} {{runlevel}}`

- Szolgáltatás törlése egy futási szintről:

`sudo rc-update delete {{service_name}} {{runlevel}}`

- Szolgáltatás törlése az összes futási szintről:

`sudo rc-update --all delete {{service_name}}`
