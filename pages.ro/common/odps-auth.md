# odps auth

> Autoritățile utilizatorilor din ODPS (Serviciul de procesare a datelor deschise).
> A se vedea, de asemenea, `odps`.
> Mai multe informaţii: <https://www.alibabacloud.com/help/doc-detail/27971.htm>

- Adăugați un utilizator la proiectul curent:

`add user {{username}};`

- Acordarea unui set de autorități unui utilizator:

`grant {{action_list}} on {{object_type}} {{object_name}} to user {{username}};`

- Afișează autoritățile unui utilizator:

`show grants for {{username}};`

- Crearea unui rol de utilizator:

`create role {{role_name}};`

- Acordarea unui set de autorități unui rol:

`grant {{action_list}} on {{object_type}} {{object_name}} to role {{role_name}};`

- Descrieți autoritățile care au un rol:

`desc role {{role_name}};`

- Acordarea unui rol unui utilizator:

`grant {{role_name}} to {{username}};`
