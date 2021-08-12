# knife

> CLI pentru interacțiunea cu un server Chef de la un repo local Chef.
> Mai multe informaţii: <https://docs.chef.io/knife.html>

- Bootstrap un nou nod:

`knife bootstrap {{fqdn_or_ip}}`

- Listează toate nodurile înregistrate:

`knife node list`

- Arată un nod:

`knife node show {{node_name}}`

- Editează un nod:

`knife node edit {{node_name}}`

- Editează un rol:

`knife role edit {{role_name}}`

- Vizualizaţi un sac de date:

`knife data bag show {{data_bag_name}} {{data_bag_item}}`

- Încărcați o carte de bucate locală pe serverul Chef:

`knife cookbook upload {{cookbook_name}}`
