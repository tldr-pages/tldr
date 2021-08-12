# smbmap

> Instrumentul de enumerare SMB.
> Mai multe informaţii: <https://github.com/ShawnDEvans/smbmap>

- Afișați partajările și permisiunile SMB pe o gazdă, solicitând parola utilizatorului sau hash NTLM:

`smbmap -u {{username}} --prompt -H {{ip}}`

- Afișați SMB partajări și permisiuni pe o gazdă, specificând domeniul și trecerea parolei NTLM hash:

`smbmap -u {{username}} --prompt -d {{domain}} -H {{ip}}`

- Afișează partajările SMB și listează un singur nivel de directoare și fișiere:

`smbmap -u {{username}} --prompt -H {{ip}} -r`

- Afișează partajările SMB și listează recursiv un număr definit de niveluri de directoare și fișiere:

`smbmap -u {{username}} --prompt -H {{ip}} -R --depth {{3}}`

- Afișează partajările SMB și listează recursiv directoare și fișiere, descărcarea fișierelor care se potrivesc cu o expresie regulată:

`smbmap -u {{username}} --prompt -H {{ip}} -R -A {{pattern}}`

- Afișează partajările SMB și listează recursiv directoarele și fișierele, căutând conținut de fișier care corespunde unei expresii regulate:

`smbmap -u {{username}} --prompt -H {{ip}} -R -F {{pattern}}`

- Executați o comandă shell pe un sistem la distanță:

`smbmap -u {{username}} --prompt -H {{ip}} -x {{command}}`

- Încărcați un fișier într-un sistem de la distanță:

`smbmap -u {{username}} --prompt -H {{ip}} --upload {{source}} {{destination}}`
