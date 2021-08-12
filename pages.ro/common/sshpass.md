# sshpass

> Un furnizor de parole ssh.
> Funcționează prin crearea unui TTY, introducerea parolei în el, apoi redirecționarea stdin la sesiunea ssh.

- Conectați-vă la un server la distanță utilizând o parolă furnizată pe un descriptor de fișier (în acest caz, stdin):

`sshpass -d {{0}} ssh {{user}}@{{hostname}}`

- Conectați-vă la un server de la distanță cu parola furnizată ca opțiune și acceptați automat tastele ssh necunoscute:

`sshpass -p {{password}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}}`

- Conectați-vă la un server la distanță utilizând prima linie a unui fișier ca parolă, acceptați automat chei ssh necunoscute și lansați o comandă:

`sshpass -f {{file}} ssh -o StrictHostKeyChecking=no {{user}}@{{hostname}} "{{command}}"`
