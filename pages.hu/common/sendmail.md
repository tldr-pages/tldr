# sendmail

> E-mail küldése a parancssorból. További információ: <https://manned.org/sendmail>.

- A `message.txt` tartalmú üzenet küldése a `username` helyi felhasználó levelezési könyvtárába:

`sendmail {{username}} < {{message.txt}}`

- Küldjön e-mailt a you@yourdomain.com címről (feltéve, hogy a levelezőszerver be van erre konfigurálva) a test@gmail.com címre, amely a `message.txt` címben található üzenetet tartalmazza:

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{message.txt}}`

- Küldjön e-mailt a you@yourdomain.com címről (feltételezve, hogy a levelezőszerver be van erre konfigurálva) a test@gmail.com címre, amely tartalmazza a `file.zip` fájlt:

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{file.zip}}`
