# gem

> Een pakketbeheerder voor de programmeertaal Ruby.
> Meer informatie: <https://guides.rubygems.org/command-reference/>.

- Zoek naar externe gem(s) en toon alle beschikbare versies:

`gem search {{regex}} {{[-a|--all]}}`

- Installeer de nieuwste versie van een gem:

`gem install {{gem_naam}}`

- Installeer een specifieke versie van een gem:

`gem install {{gem_naam}} {{[-v|--version]}} {{1.0.0}}`

- Installeer de nieuwste overeenkomende (SemVer) versie van een gem:

`gem install {{gem_naam}} {{[-v|--version]}} '~> {{1.0}}'`

- Update een gem:

`gem update {{gem_naam}}`

- Toon alle lokale gems:

`gem list`

- Verwijder een gem:

`gem uninstall {{gem_naam}}`

- Verwijder een specifieke versie van een gem:

`gem uninstall {{gem_naam}} {{[-v|--version]}} {{1.0.0}}`
