# knife

> CLI a Chef szerverrel való interakcióhoz egy helyi Chef repóból. További információ: <https://docs.chef.io/knife.html>.

- Egy új csomópont bootstrapelése:

`knife bootstrap {{fqdn_or_ip}}`

- Az összes regisztrált csomópont listázása:

`knife node list`

- Egy csomópont megjelenítése:

`knife node show {{node_name}}`

- Egy csomópont szerkesztése:

`knife node edit {{node_name}}`

- Szerepkör szerkesztése:

`knife role edit {{role_name}}`

- Egy adattáska megtekintése:

`knife data bag show {{data_bag_name}} {{data_bag_item}}`

- Helyi szakácskönyv feltöltése a Chef-kiszolgálóra:

`knife cookbook upload {{cookbook_name}}`
