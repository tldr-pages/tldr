# qm stop

> Arrête une machine virtuelle.
> Plus d'informations : <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_stop>.

- Arrête immédiatement une machine virtuelle :

`qm stop {{100}}`

- Arrête une machine virtuelle et attend au maximum 10 secondes :

`qm stop {{100}} --timeout 10`

- Arrête une machine virtuelle et ignore le verrou (seul l'utilisateur root peut utiliser cette option) :

`qm stop {{100}} --skiplock true`

- Arrête une machine virtuelle sans désactiver les volumes de stockage :

`qm stop {{100}} --keepActive true`
