# ruby

> Ruby-programmeertaal interpreter.
> Zie ook: `gem`, `bundler`, `rake`, `irb`.
> Meer informatie: <https://manned.org/ruby>.

- Voer een Ruby-script uit:

`ruby {{pad/naar/script.rb}}`

- Voer één Ruby-commando uit op de command-line:

`ruby -e "{{commando}}"`

- Controleer op syntax fouten in een bepaald Ruby-script:

`ruby -c {{pad/naar/script.rb}}`

- Start de ingebouwde HTTP-server op poort 8080 in de huidige map:

`ruby -run -e httpd`

- Voer een Ruby-binary lokaal uit zonder de vereiste library te installeren waarvan het afhankelijk is:

`ruby -I {{pad/naar/library_map}} -r {{vereiste_library_naam}} {{pad/naar/bin_map/bin_naam}}`

- Toon de versie:

`ruby {{[-v|--version]}}`
