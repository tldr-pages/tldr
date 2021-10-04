# ac

> Zeige Statistiken darüber, wie lange Nutzer verbunden sind.
> Mehr Informationen: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Zeige wie lange der/die aktuelle Nutzer:in verbunden ist in Stunden:

`ac`

- Zeige wie lange alle Nutzer eingeloggt sind in Stunden:

`ac --individual-totals`

- Zeige wie lange ein:e spezifische:r Nutzer:in eingeloggt ist in Stunden:

`ac --individual-totals {{nutzername}}`

- Zeige wie lange ein:e spezifische:r Nutzer:in eingeloggt ist in Stunden am Tag (mit Gesamtsumme):

`ac --daily-totals --individual-totals {{nutzername}}`

- Zeige zusätzliche Details:

`ac --compatibility`
