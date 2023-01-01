# amass intel

> Recopila información de código abierto sobre una organización, como dominios raíz y ASNs.
> Más información: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Encuentre dominios raíz en un rango de direcciones IP específico:

`amass intel -addr {{192.168.0.1-254}}`

- Utiliza métodos activos de reconocimiento:

`amass intel -active -addr {{192.168.0.1-254}}`

- Encuentre dominios raíz relacionados con un dominio específico:

`amass intel -whois -d {{nombre_de_dominio}}`

- Encuentre ASN pertenecientes a una organización específica:

`amass intel -org {{nombre_de_organizacion}}`

- Busca dominios raíz pertenecientes a un determinado número de sistemas autónomos:

`amass intel -asn {{asn}}`

- Guarda los resultados en un archivo de texto:

`amass intel -o {{archivo_de_salida}} -whois -d {{nombre_de_dominio}}`
