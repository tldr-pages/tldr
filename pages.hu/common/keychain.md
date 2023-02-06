# keychain

> Az ssh-agent és/vagy gpg-agent újrafelhasználása a bejelentkezések között. További információ: <http://funtoo.org/Keychain>.

- Ellenőrizze, hogy van-e futó ssh-agent, és indítson egyet, ha szükséges:

`keychain`

- Ellenőrizze a gpg-agentet is:

`keychain --agents "{{gpg,ssh}}"`

- Az összes aktív kulcs aláírásának listája:

`keychain --list`

- Az összes aktív kulcs ujjlenyomatának listázása:

`keychain --list-fp`

- Az ügynökhöz hozzáadott identitások időkorlátjának megadása percben:

`keychain --timeout {{minutes}}`
