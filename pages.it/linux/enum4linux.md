# enum4linux

> Strumento per ottenere informazioni da Windows e Samba da un sistema remoto.
> Maggiori informazioni: <https://labs.portcullis.co.uk/tools/enum4linux/>.

- Ottieni informazioni utilizzando tutti i metodi disponibili:

`enum4linux -a {{host_remoto}}`

- Ottieni informazioni utilizzando le credenziali fornite:

`enum4linux -u {{nome_utente}} -p {{password}} {{host_remoto}}`

- Ottieni la lista utenti:

`enum4linux -U {{host_remoto}}`

- Mostra le risorse condivise:

`enum4linux -S {{host_remoto}}`

- Ottieni informazioni riguardo al sistema operativo:

`enum4linux -o {{host_remoto}}`
