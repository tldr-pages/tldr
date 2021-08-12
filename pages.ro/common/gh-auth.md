# gh auth

> Autentificare cu o gazdă GitHub din linia de comandă.
> Mai multe informaţii: <https://cli.github.com/manual/gh_auth>

- Autentificare cu prompt interactiv:

`gh auth login`

- Conectați-vă cu un token de intrare standard (creat în https://github.com/settings/tokens):

`echo {{your_token}} | gh auth login --with-token`

- Verificați dacă sunteți autentificat:

`gh auth status`

- Deconectați-vă:

`gh auth logout`

- Conectați-vă cu un anumit server GitHub Enterprise:

`gh auth login --hostname {{github.example.com}}`

- Reîmprospătați sesiunea pentru a vă asigura că acreditările de autentificare au domeniile minime corecte (elimină domeniile suplimentare solicitate anterior):

`gh auth refresh`

- Extindeți domeniile de permisiune:

`gh auth refresh --scopes {{write:org,read:public_key}}`
