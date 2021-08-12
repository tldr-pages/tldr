# r2e

> Redirecționează fluxurile RSS către o adresă de e-mail.
> Necesită configurarea `sendmail` sau smtp.
> Mai multe informaţii: <https://github.com/rss2email/rss2email>

- Creați o nouă bază de date de flux care trimite e-mail la o adresă de e-mail:

`r2e new {{email_address}}`

- Aboneaza-te la un feed:

`r2e add {{feed_name}} {{feed_URI}}`

- Trimite povești noi la o adresă de e-mail:

`r2e run`

- Listează toate fluxurile:

`r2e list`

- Ștergeți un flux la un index specificat:

`r2e delete {{index}}`
