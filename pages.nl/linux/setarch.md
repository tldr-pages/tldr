# setarch

> Verander de gerapporteerde architectuur voor de uitvoering van een programma, voornamelijk gebruikt om aan te passen hoe programma's zich gedragen op basis van de systeemarchitectuur.
> Nuttig voor het testen van compatibiliteit of het draaien van oudere toepassingen.
> Meer informatie: <https://manned.org/setarch.8>.

- Voer een commando uit alsof de machine-architectuur `i686` is (handig voor het draaien van 32-bit applicaties op een 64-bit kernel):

`setarch i686 {{opdracht}}`

- Een shell uitvoeren met de `x86_64` architectuur:

`setarch x86_64 {{bash}}`

- Schakel de willekeurigheid van de virtuele adresruimte uit:

`setarch {{linux32}} {{[-R|--addr-no-randomize]}} {{commando}}`

- Toon ondersteunde architecturen:

`setarch --list`

- Toon help:

`setarch {{[-h|--help]}}`
