# ufw

> Tallafocs sense complicacions (_Uncomplicated Firewall_).
> Interfície d'usuari de `iptables` per facilitar la configuració d'un firewall.
> Més informació: <https://wiki.ubuntu.com/UncomplicatedFirewall>.

- Activa ufw:

`ufw enable`

- Desactiva ufw:

`ufw disable`

- Mostra les regles del ufw, en conjunt amb els seus números:

`ufw status numbered`

- Permet el tràfic entrant en el port 5432 en aquest host amb un comentari que indentifiqui el servei:

`ufw allow {{5432}} comment "{{servei}}"`

- Permet només el tràfic TCP desde 192.168.0.4 a qualsevol direcció d'aquest host, en el port 22:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- Denega el tràfic en el port 80 en aquest host:

`ufw deny {{80}}`

- Denega tot el tràfic al port 22:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{22}}`

- Elimina una regla concreta. El número de la regla es pot obtenir del comanadament `ufw status numbered`:

`ufw delete {{número_de_regla}}`
