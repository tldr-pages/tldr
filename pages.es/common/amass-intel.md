# amass intel

> Recopila información de código abierto sobre una organización, como dominios raíz y ASNs.
> Más información: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Encuentra dominios raíz en un rango de direcciones IP específico:

`amass intel -addr {{192.168.0.1-254}}`

- Usa métodos activos de reconocimiento:

`amass intel -active -addr {{192.168.0.1-254}}`

- Encuentra dominios raíz relacionados con un [d]ominio específico:

`amass intel -whois -d {{nombre_de_dominio}}`

- Encuentra ASNs pertenecientes a una [org]anización específica:

`amass intel -org {{nombre_de_organización}}`

- Encuentra dominios raíz pertenecientes a un Número de Sistema Autónomo específico:

`amass intel -asn {{cadena}}`

- Guarda los resultados en un archivo de texto:

`amass intel -o {{ruta/al/archivo_de_salida}} -whois -d {{nombre_de_dominio}}`

- Lista todas las fuentes de datos disponibles:

`amass intel -list`
