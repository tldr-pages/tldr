# notmuch

> Parancssor alapú program e-mail üzenetek nagy gyűjteményeinek indexelésére, keresésére, olvasására és címkézésére. További információ: <https://notmuchmail.org/manpages/>.

- Konfigurálás az első használathoz:

`notmuch setup`

- Címke hozzáadása a keresési kifejezésnek megfelelő összes üzenethez:

`notmuch tag +{{custom_tag}} "{{search_term}}"`

- Címke eltávolítása a keresési kifejezésnek megfelelő összes üzenethez:

`notmuch tag -{{custom_tag}} "{{search_term}}"`

- Az adott keresési kifejezésnek megfelelő üzenetek számolása:

`notmuch count --output={{messages|threads}} "{{search_term}}"`

- Az adott keresési kifejezésnek megfelelő üzenetek keresése:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} "{{search_term}}"`

- A keresési eredmények számának korlátozása X-re:

`notmuch search --format={{json|text}} --output={{summary|threads|messages|files|tags}} --limit={{X}} "{{search_term}}"`

- Válaszsablon létrehozása egy üzenetkészlethez:

`notmuch reply --format={{default|headers-only}} --reply-to={{sender|all}} "{{search_term}}"`
