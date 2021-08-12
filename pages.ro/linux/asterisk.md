# asterisk

> Telefon și server de schimb (telefon).
> Utilizat pentru rularea serverului în sine și gestionarea unei instanțe care rulează deja.
> Mai multe informaţii: <https://wiki.asterisk.org/wiki/display/AST/Home>

- [R] econnect la un server care rulează, și activați logare 3 niveluri de [v] erbosity:

`asterisk -r -vvv`

- [R] econectați la un server care rulează, executați o singură comandă și returnați:

`asterisk -r -x "{{command}}"`

- Arată clienții Chan_SIP (telefoane):

`asterisk -r -x "sip show peers"`

- Afișează apelurile active și canalele:

`asterisk -r -x "core show channels"`

- Arată cutiile poştale vocale:

`asterisk -r -x "voicemail show users"`

- Termină un canal:

`asterisk -r -x "hangup request {{channel_ID}}"`

- Reîncarcă configurația Chan_SIP:

`asterisk -r -x "sip reload"`
