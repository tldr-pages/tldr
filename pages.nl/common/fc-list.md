# fc-list

> Toon beschikbare lettertypen die op het systeem zijn geïnstalleerd.
> Meer informatie: <https://manned.org/fc-list>.

- Toon geïnstalleerde lettertypen:

`fc-list`

- Toon geïnstalleerde lettertypen die overeenkomen met een bepaalde naam:

`fc-list | grep '{{DejaVu Serif}}'`

- Toon het aantal geïnstalleerde lettertypen:

`fc-list | wc {{[-l|--lines]}}`

- Toon geïnstalleerde lettertypen die een taal ondersteunen op basis van de landcode:

`fc-list :lang={{jp}}`

- Toon geïnstalleerde lettertypen die het teken bevatten dat is opgegeven door zijn Unicode-codepunt:

`fc-list :charset={{f303}}`
