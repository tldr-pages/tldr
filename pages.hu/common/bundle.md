# bundle

> Függőségkezelő a Ruby programozási nyelvhez. További információ: <https://bundler.io/man/bundle.1.html>.

- Telepítse az összes, a `Gemfile` által definiált drágakövet a munkakönyvtárba:

`bundle install`

- Parancs végrehajtása az aktuális csomag kontextusában:

`bundle exec {{command}} {{arguments}}`

- Frissítse az összes drágakövet a `Gemfile` meghatározott szabályok szerint, és újragenerálja a `Gemfile.lock`:

`bundle update`

- Egy vagy több konkrét, a `Gemfile`-ban meghatározott drágakő(k) frissítése:

`bundle update {{gem_name}} {{gem_name}}`

- Egy vagy több, a `Gemfile` -ban meghatározott konkrét drágakő(k) frissítése, de csak a következő javított verzióra:

`bundle update --patch {{gem_name}} {{gem_name}}`

- A `Gemfile` adott csoporton belüli összes drágakő frissítése:

`bundle update --group {{development}}`

- A telepített drágakövek listája a `Gemfile` oldalon, amelyeknek újabb verziója elérhető:

`bundle outdated`

- Új drágakőváz létrehozása:

`bundle gem {{gem_name}}`
