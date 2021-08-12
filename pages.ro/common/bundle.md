# bundle

> Manager de dependență pentru limbajul de programare Ruby.
> Mai multe informaţii: <https://bundler.io/man/bundle.1.html>

- Instalați toate pietrele definite în „Gemfile” de așteptat în directorul de lucru:

`bundle install`

- Execută o comandă în contextul pachetului curent:

`bundle exec {{command}} {{arguments}}`

- Actualizați toate pietrele de regulile definite în „Gemfile” și regenerați `Gemfile.Lock`:

`bundle update`

- Actualizarea uneia sau mai multor bijuterii specifice definite în „Gemfile”:

`bundle update {{gem_name}} {{gem_name}}`

- Actualizați una sau mai multe pietre specifice definite în „Gemfile”, dar numai la următoarea versiune a patch-ului:

`bundle update --patch {{gem_name}} {{gem_name}}`

- Actualizaţi toate pietrele din cadrul grupului dat în „Gemfile”:

`bundle update --group {{development}}`

- Lista pietrelor instalate în „Gemfile” cu versiuni mai noi disponibile:

`bundle outdated`

- Creați un nou schelet bijuterie:

`bundle gem {{gem_name}}`
