# notmuch

> Program bazat pe linie de comandă pentru indexarea, căutarea, citirea și etichetarea colecțiilor mari de mesaje de e-mail.
> Mai multe informaţii: <https://notmuchmail.org/manpages/>

- Configurați pentru prima utilizare:

`notmuch setup`

- Adăugați o etichetă pentru toate mesajele care corespund unui termen de căutare:

`notmuch tag +{{custom_tag}} "{{search_term}}"`

- Eliminați o etichetă pentru toate mesajele care corespund unui termen de căutare:

`notmuch tag -{{custom_tag}} "{{search_term}}"`

- Contorizarea mesajelor care corespund termenului de căutare dat:

`notmuch count --output={{messages|threads}} "{{search_term}}"`

- Caută mesaje care corespund termenului de căutare dat:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} "{{search_term}}"`

- Limitați numărul de rezultate de căutare la X:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} --limit={{X}} "{{search_term}}"`

- Creați un șablon de răspuns pentru un set de mesaje:

`notmuch reply --format={{default|headers-only}} --reply-to={{sender|all}} "{{search_term}}"`
