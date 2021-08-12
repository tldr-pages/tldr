# ssh-agent

> Procesarea unui agent SSH.
> Un agent SSH deține chei SSH decriptate în memorie până când este eliminat sau procesul este ucis.
> A se vedea, de asemenea, `ssh-add`, care poate adăuga și gestiona cheile deținute de un agent SSH.

- Porniți un agent SSH pentru carcasa curentă:

`eval $(ssh-agent)`

- Ucide agentul care rulează în prezent:

`ssh-agent -k`
