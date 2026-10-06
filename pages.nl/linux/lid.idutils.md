# lid

> Bevraag een ID-database op tokens die overeenkomen met een patroon.
> Opmerking: er moet eerst een ID-database gebouwd worden met `mkid`.
> Meer informatie: <https://www.gnu.org/software/idutils/manual/idutils.html#lid-invocation>.

- Toon alle tokens en hun bestandslocaties in de ID-database:

`lid`

- Zoek bestanden die een specifiek token bevatten:

`lid {{token}}`

- Zoek tokens die overeenkomen met een patroon, ongeacht hoofdlettergebruik:

`lid {{[-i|--ignore-case]}} {{token}}`

- Zoek tokens die overeenkomen met een uitgebreide `regex`:

`lid {{[-r|--regexp]}} "{{patroon}}"`

- Toon overeenkomende regels in grep-stijl formaat:

`lid {{[-R|--result]}} grep {{token}}`

- Zoek tokens die slechts één keer voorkomen (handig voor het vinden van ongebruikte definities):

`lid {{[-F|--frequency]}} 1`
