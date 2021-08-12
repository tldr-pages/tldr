# ufw

> Paravan de protecție necomplicat.
> Interfață pentru iptables cu scopul de a facilita configurarea unui paravan de protecție.
> Mai multe informaţii: <https://wiki.ubuntu.com/UncomplicatedFirewall>

- Activează ufw:

`ufw enable`

- Dezactivează ufw:

`ufw disable`

- Arată regulile ufw, împreună cu numerele lor:

`ufw status numbered`

- Permite traficul de intrare pe portul 5432 pe această gazdă cu un comentariu de identificare a serviciului:

`ufw allow {{5432}} comment "{{Service}}"`

- Permite numai traficul TCP de la 192.168.0.4 la orice adresă de pe această gazdă, pe portul 22:

`ufw allow proto {{tcp}} from {{192.168.0.4}} to {{any}} port {{22}}`

- Negați traficul pe portul 80 pe această gazdă:

`ufw deny {{80}}`

- Neagă tot traficul UDP la portul 22:

`ufw deny proto {{udp}} from {{any}} to {{any}} port {{22}}`

- Şterge o anumită regulă. Numărul regulii poate fi preluat din comanda `ufw status numbered`:

`ufw delete {{rule_number}}`
