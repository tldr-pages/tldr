# rpcclient

> instrument client MS-RPC (parte din suita samba).
> Mai multe informaţii: <https://www.samba.org/samba/docs/current/man-html/rpcclient.1.html>

- Conectați-vă la o gazdă la distanță:

`rpcclient --user {{domain}}\{{username}}%{{password}} {{ip}}`

- Conectați-vă la o gazdă la distanță pe un domeniu fără o parolă:

`rpcclient --user {{username}} --workgroup {{domain}} --no-pass {{ip}}`

- Conectați-vă la o gazdă la distanță, trecând hash-ul parolei:

`rpcclient --user {{domain}}\{{username}} --pw-nt-hash {{ip}}`

- Executați comenzi shell pe o gazdă la distanță:

`rpcclient --user {{domain}}\{{username}}%{{password}} --command {{semicolon_separated_commands}} {{ip}}`

- Afișează utilizatorii de domenii:

`rpcclient $> enumdomusers`

- Privilegiile afişării:

`rpcclient $> enumprivs`

- Afișați informații despre un anumit utilizator:

`rpcclient $> queryuser {{username|rid}}`

- Creați un utilizator nou în domeniu:

`rpcclient $> createdomuser {{username}}`
