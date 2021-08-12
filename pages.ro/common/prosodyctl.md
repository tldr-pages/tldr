# prosodyctl

> Instrumentul de control pentru serverul Prosody XMPP.
> Mai multe informaţii: <https://prosody.im/doc/prosodyctl>

- Afișați starea serverului Prosody:

`sudo prosodyctl status`

- Reîncarcă fișierele de configurare ale serverului:

`sudo prosodyctl reload`

- Adăugați un utilizator la serverul Prosody XMPP:

`sudo prosodyctl adduser {{user@example.com}}`

- Setați parola unui utilizator:

`sudo prosodyctl passwd {{user@example.com}}`

- Ștergeți permanent un utilizator:

`sudo prosodyctl deluser {{user@example.com}}`
