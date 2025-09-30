# bundle

> Administrador de dependencias para el lenguaje de programación Ruby.
> Más información: <https://bundler.io/man/bundle.1.html>.

- Instala todas las gemas (gems) definidas en el archivo `Gemfile` en el directorio de trabajo:

`bundle install`

- Ejecuta un comando en el contexto del paquete (bundle) actual:

`bundle exec {{comando}} {{argumentos}}`

- Actualiza todas las gemas (gems) definidas por las reglas en el `Gemfile` y regenera `Gemfile.lock`:

`bundle update`

- Actualiza una o más gemas específicas definidas en el `Gemfile`:

`bundle update {{gema1}} {{gema2}}`

- Actualiza una o más gemas (gems) específicas definidas en el `Gemfile` pero solo a la siguiente versión parche (patch):

`bundle update --patch {{gema1}} {{gema2}}`

- Actualiza todas las gemas (gems) dentro de un grupo dado en el `Gemfile`:

`bundle update --group {{development}}`

- Lista las gemas instaladas con nuevas versiones disponibles definidas en el `Gemfile`:

`bundle outdated`

- Crea una nueva estructura de gema:

`bundle gem {{gema}}`
