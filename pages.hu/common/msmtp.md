# msmtp

> SMTP kliens. Szöveget olvas be a standard bemenetről és elküldi egy SMTP szerverre. További információ: <https://marlam.de/msmtp>.

- E-mail küldése a `~/.msmtprc` oldalon beállított alapértelmezett fiókkal:

`echo "{{Hello world}}" | msmtp {{to@example.org}}`

- E-mail küldése a `~/.msmtprc` oldalon konfigurált adott fiókkal:

`echo "{{Hello world}}" | msmtp --account={{account_name}} {{to@example.org}}`

- E-mail küldése konfigurált fiók nélkül. A jelszót a `~/.msmtprc` fájlban kell megadni:

`echo "{{Hello world}}" | msmtp --host={{localhost}} --port={{999}} --from={{from@example.org}} {{to@example.org}}`
