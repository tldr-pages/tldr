# bundle

> Gestore di dipendenze per il linguaggio di programmazione Ruby.
> Maggiori informazioni: <https://bundler.io/man/bundle.1.html>.

- Installa tutte le gem definite nel gemfile della directory corrente:

`bundle install`

- Aggiorna tutte le gem secondo le regole definite nel gemfile e genera un `gemfile.lock`:

`bundle update`

- Aggiorna una specifica gem definita nel gemfile:

`bundle update --source {{nome_gem}}`

- Crea un scheletro per una nuova gem:

`bundle gem {{nome_gem}}`
