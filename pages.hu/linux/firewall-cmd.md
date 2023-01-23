# firewall-cmd

> A firewalld parancssori kliens. További információ: <https://firewalld.org/documentation/man-pages/firewall-cmd>.

- A rendelkezésre álló tűzfalzónák megtekintése:

`firewall-cmd --get-active-zones`

- A jelenleg alkalmazott szabályok megtekintése:

`firewall-cmd --list-all`

- Az interfész véglegesen a blokkolási zónába helyezése, ami gyakorlatilag minden kommunikációt blokkol:

`firewall-cmd --permanent --zone={{block}} --change-interface={{enp1s0}}`

- Tartósan megnyitja a portot egy szolgáltatás számára a megadott zónában (például a 443-as portot, ha a `public` zónában van):

`firewall-cmd --permanent --zone={{public}} --add-service={{https}}`

- A megadott zónában lévő szolgáltatás portjának végleges lezárása (például a 80-as port, ha a `public` zónában van):

`firewall-cmd --permanent --zone={{public}} --remove-service={{http}}`

- Két tetszőleges port végleges megnyitása a megadott zónában:

`firewall-cmd --permanent --zone={{public}} --add-port={{25565/tcp}} --add-port={{19132/udp}}`

- A firewalld újratöltése a szabálymódosítások érvénybe lépésének kikényszerítéséhez:

`firewall-cmd --reload`
