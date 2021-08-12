# git remote

> Gestionați setul de depozite urmărite („telecomenzi”).
> Mai multe informaţii: <https://git-scm.com/docs/git-remote>

- Afișează o listă de telecomenzi existente, numele lor și adresa URL:

`git remote -v`

- Afișează informații despre o telecomandă:

`git remote show {{remote_name}}`

- Adaugă o telecomandă:

`git remote add {{remote_name}} {{remote_url}}`

- Modificați adresa URL a unei telecomenzi (utilizați `—add` pentru a păstra adresa URL existentă):

`git remote set-url {{remote_name}} {{new_url}}`

- Elimină o telecomandă:

`git remote remove {{remote_name}}`

- Redenumiți o telecomandă:

`git remote rename {{old_name}} {{new_name}}`
