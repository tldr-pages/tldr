# http

> HTTPie: clientul HTTP, își propune să fie mai ușor de utilizat decât CurL.
> Mai multe informaţii: <https://httpie.org>

- Descărcați un URL într-un fișier:

`http --download {{example.org}}`

- Trimiteți date codificate de formular:

`http --form {{example.org}} {{name='bob'}} {{profile_picture@'bob.png'}}`

- Trimite obiectul JSON:

`http {{example.org}} {{name='bob'}}`

- Specificați o metodă HTTP:

`http {{HEAD}} {{example.org}}`

- Includeți un antet suplimentar:

`http {{example.org}} {{X-MyHeader:123}}`

- Treceți un nume de utilizator și o parolă pentru autentificarea serverului:

`http --auth {{username:password}} {{example.org}}`

- Specificați organismul de solicitare brută prin stdin:

`cat {{data.txt}} | http PUT {{example.org}}`
