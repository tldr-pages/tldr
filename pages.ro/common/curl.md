# curl

> Transferă date de pe sau către un server.
> Suportă majoritatea protocoalelor, inclusiv HTTP, FTP și POP3.
> Mai multe informaţii: <https://curl.se>

- Descărcați conținutul unui URL într-un fișier:

`curl {{http://example.com}} --output {{filename}}`

- Descărcați un fișier, salvând ieșirea sub numele fișierului indicat de URL-ul:

`curl --remote-name {{http://example.com/filename}}`

- Descărcați un fișier, următoarele redirecționări ale locației și continuând automat (reluarea) transferului de fișiere anterior:

`curl --remote-name --location --continue-at - {{http://example.com/filename}}`

- Trimiterea datelor codificate de formular (cerere POST de tip `aplication/x-www-form-urlencoded`). Utilizați `—data @file_name `sau `—data @'-' pentru a citi din STDIN:

`curl --data {{'name=bob'}} {{http://example.com/form}}`

- Trimiteți o solicitare cu un antet suplimentar, utilizând o metodă HTTP personalizată:

`curl --header {{'X-My-Header: 123'}} --request {{PUT}} {{http://example.com}}`

- Trimiteți date în format JSON, specificând antetul de tip de conținut corespunzător:

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://example.com/users/1234}}`

- Treceți un nume de utilizator și o parolă pentru autentificarea serverului:

`curl --user myusername:mypassword {{http://example.com}}`

- Pass certificat client și cheie pentru o resursă, sărind peste validarea certificatului:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}}`
