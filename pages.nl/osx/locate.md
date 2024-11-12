# locate

> Vind snel bestandsnamen.
> Meer informatie: <https://keith.github.io/xcode-man-pages/locate.1.html>.

- Zoek naar een patroon in de database. Opmerking: de database wordt periodiek herberekend (meestal wekelijks of dagelijks):

`locate "{{patroon}}"`

- Zoek naar een bestand op basis van de exacte bestandsnaam (een patroon zonder glob-tekens wordt geïnterpreteerd als `*patroon*`):

`locate */{{bestandsnaam}}`

- Herbereken de database. Dit moet je doen als je recent toegevoegde bestanden wilt vinden:

`sudo /usr/libexec/locate.updatedb`
