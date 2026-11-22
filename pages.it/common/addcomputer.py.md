# addcomputer.py

> Aggiunge un account computer a un dominio.
> Parte della suite Impacket.
> Maggiori informazioni: <https://github.com/fortra/impacket>.

- Aggiunge un computer con nome e password specifici:

`addcomputer.py -computer-name {{NOME_COMPUTER$}} -computer-pass {{password_computer}} {{dominio}}/{{nome_utente}}:{{password}}`

- Imposta solo una nuova password su un computer esistente:

`addcomputer.py -no-add -computer-name {{NOME_COMPUTER$}} -computer-pass {{password_computer}} {{dominio}}/{{nome_utente}}:{{password}}`

- Elimina un account computer esistente:

`addcomputer.py -delete -computer-name {{NOME_COMPUTER$}} {{dominio}}/{{nome_utente}}:{{password}}`

- Aggiunge computer usando autenticazione Kerberos:

`addcomputer.py -k -no-pass {{dominio}}/{{nome_utente}}@{{hostname}}`

- Aggiunge computer via LDAPS (porta 636) invece di SAMR (porta 445):

`addcomputer.py -method LDAPS -port 636 {{dominio}}/{{nome_utente}}:{{password}}`

- Specifica il domain controller esatto quando esistono più DC:

`addcomputer.py -dc-host {{hostname}} {{dominio}}/{{nome_utente}}:{{password}}`
