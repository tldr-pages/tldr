# cryptsetup

> Gestionați simplu dm-crypt și LUKS (Linux Unified Key Setup) volume criptate.
> Mai multe informaţii: <https://gitlab.com/cryptsetup/cryptsetup/>

- Inițializați un volum LUKS (suprascrie toate datele de pe partiție):

`cryptsetup luksFormat {{/dev/sda1}}`

- Deschideți un volum LUKS și creați o mapare decriptată la `/dev/mapper/ {target}} `:

`cryptsetup luksOpen {{/dev/sda1}} {{target}}`

- Eliminați o mapare existentă:

`cryptsetup luksClose {{target}}`

- Modificați fraza de acces a volumului LUKS:

`cryptsetup luksChangeKey {{/dev/sda1}}`
