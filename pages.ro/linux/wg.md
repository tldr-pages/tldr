# wg

> Gestionați configurația interfețelor WireGuard.
> Mai multe informaţii: <https://www.wireguard.com/quickstart/>

- Verificați starea interfețelor active în prezent:

`sudo wg`

- Imprimați o nouă cheie privată:

`wg genkey`

- Imprimați o nouă cheie publică:

`echo {{private_key}} | wg pubkey`

- Generează o cheie publică și privată:

`wg genkey | tee {{privatekey.txt}} | wg pubkey > {{publickey.txt}}`
