# firewall-cmd

> Clientul de linie de comandă firewalld.
> Mai multe informaţii: <https://firewalld.org/documentation/man-pages/firewall-cmd>

- Vizualizaţi zonele de firewall disponibile:

`firewall-cmd --get-active-zones`

- Vezi regulile care sunt aplicate în prezent:

`firewall-cmd --list-all`

- Deplasați permanent interfața în zona blocului, blocând efectiv toate comunicațiile:

`firewall-cmd --permanent --zone={{block}} --change-interface={{enp1s0}}`

- Deschiderea permanentă a portului pentru un serviciu în zona specificată (cum ar fi portul 443 în zona „publică”):

`firewall-cmd --permanent --zone={{public}} --add-service={{https}}`

- Închideți permanent portul pentru un serviciu în zona specificată (cum ar fi portul 80 atunci când se află în zona „publică”):

`firewall-cmd --permanent --zone={{public}} --remove-service={{http}}`

- Deschideți permanent două porturi arbitrare în zona specificată:

`firewall-cmd --permanent --zone={{public}} --add-port={{25565/tcp}} --add-port={{19132/udp}}`

- Reîncărcați firewalld pentru a forța modificările regulii să intre în vigoare:

`firewall-cmd --reload`
