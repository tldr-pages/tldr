# fail2ban-client

> Configurați și controlați serverul fail2ban.
> Mai multe informaţii: <https://github.com/fail2ban/fail2ban>

- Recuperarea statutului actual al serviciului penitenciar:

`fail2ban-client status {{jail}}`

- Eliminați IP-ul specificat din lista de interdicții a serviciului de închisoare:

`fail2ban-client set {{jail}} unbanip {{ip}}`

- Verificați dacă serverul fail2ban este în viață:

`fail2ban-client ping`
