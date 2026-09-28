# type

> Toon het type commando dat de shell zal uitvoeren.
> Opmerking: alle voorbeelden zijn niet POSIX-compatibel.
> Zie ook: `whereis`, `which`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-type>.

- Toon het type van een commando:

`type {{commando}}`

- Toon alle locaties die het opgegeven uitvoerbare bestand bevatten (werkt alleen in Bash/fish/Zsh-shells):

`type -a {{commando}}`

- Toon de naam van het schijfbestand dat uitgevoerd zou worden (werkt alleen in Bash/fish/Zsh-shells):

`type -p {{commando}}`

- Toon het type van een specifiek commando, alias/keyword/functie/builtin/bestand (werkt alleen in Bash/fish-shells):

`type -t {{commando}}`
