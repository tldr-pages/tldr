# salt-key

> Gestionează cheile minionilor de sare de pe maestrul de sare.
> Trebuie să fie rulat pe master sare, probabil ca rădăcină sau cu sudo.
> Mai multe informaţii: <https://docs.saltstack.com/ref/cli/salt-key.html>

- Afișează toate cheile de minion acceptate, neacceptate și respinse:

`salt-key -L`

- Acceptați o cheie de minion după nume:

`salt-key -a {{MINION_ID}}`

- Respingeți o cheie de minion după nume:

`salt-key -r {{MINION_ID}}`

- Imprimați amprentele tuturor cheilor publice:

`salt-key -F`
