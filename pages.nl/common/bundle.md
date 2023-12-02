# bundle

> Dependency manager voor de Ruby programmeertaal.
> Meer informatie: <https://bundler.io/man/bundle.1.html>.

- Installeer alle gems gedefineerd in de `Gemfile`, welke verwacht word in de huidige map:

`bundle install`

- Voer een commando uit in de context van de huidige bundle:

`bundle exec {{commando}} {{argumenten}}`

- Update alle gems volgens de regels gedefineerd in de `Gemfile` en regenereer de `Gemfile.lock`:

`bundle update`

- Update een of meerdere specifieke gem(s) gedefineerd in de `Gemfile`:

`bundle update {{gem_naam1}} {{gem_naam2}}`

- Update een of meerdere specifieke gem(s) gedefineerd in de `Gemfile` maar alleen naar de volgende patch versie:

`bundle update --patch {{gem_naam1}} {{gem_naam2}}`

- Update alle gems binnen de gegeven groep in de `Gemfile`:

`bundle update --group {{development}}`

- Toon de geïnstalleerde gems in de `Gemfile` welke  nieuwere versies beschikbaar hebben:

`bundle outdated`

- Maak een nieuw gem skelet:

`bundle gem {{gem_naam}}`
