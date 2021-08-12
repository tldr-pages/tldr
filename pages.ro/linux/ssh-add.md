# ssh-add

> Gestionați tastele ssh încărcate în agentul ssh-.
> Asigurați-vă că agentul ssh-este în funcțiune pentru ca cheile să fie încărcate în el.

- Adaugă tastele ssh implicite în `~/.ssh` la ssh-agent:

`ssh-add`

- Adăugați o cheie specifică agentului ssh-:

`ssh-add {{path/to/private_key}}`

- Lista amprentelor digitale ale cheilor încărcate în prezent:

`ssh-add -l`

- Ștergeți o cheie din agentul ssh-:

`ssh-add -d {{path/to/private_key}}`

- Ștergeți toate cheile încărcate în prezent din agentul ssh-:

`ssh-add -D`
