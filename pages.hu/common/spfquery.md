# spfquery

> A Sender Policy Framework rekordok lekérdezése az e-mail küldő hitelesítése érdekében. További információ: <https://www.libspf2.org/>.

- Annak ellenőrzése, hogy egy IP-cím jogosult-e e-mailt küldeni a megadott e-mail címről:

`spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}}`

- Kapcsolja be a hibakeresési kimenetet:

`spfquery -ip {{8.8.8.8}} -sender {{sender@example.com}} --debug`
