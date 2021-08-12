# msmtp

> Un client SMTP.
> Citește textul de la intrarea standard și îl trimite la un server SMTP.
> Mai multe informaţii: <https://marlam.de/msmtp>

- Trimiteți un e-mail utilizând contul implicit configurat în `~/.msmtprc`:

`echo "{{Hello world}}" | msmtp {{to@example.org}}`

- Trimiteți un e-mail folosind un cont specific configurat în `~/.msmtprc`:

`echo "{{Hello world}}" | msmtp --account={{account_name}} {{to@example.org}}`

- Trimiteți un e-mail fără un cont configurat. Parola trebuie specificată în fișierul `~/.msmtprc`:

`echo "{{Hello world}}" | msmtp --host={{localhost}} --port={{999}} --from={{from@example.org}} {{to@example.org}}`
