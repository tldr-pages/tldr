# bundle

> Gestore delle dipendenze per il linguaggio Ruby.
> Maggiori informazioni: <https://bundler.io/man/bundle.1.html>.

- Installa tutte le gem definite nel `Gemfile` nella directory corrente:

`bundle install`

- Esegue un comando nel contesto del bundle corrente:

`bundle exec {{comando}} {{argomenti}}`

- Aggiorna tutte le gem secondo le regole del `Gemfile` e rigenera `Gemfile.lock`:

`bundle update`

- Aggiorna una o più gem specifiche definite nel `Gemfile`:

`bundle update {{nome_gem1}} {{nome_gem2}}`

- Aggiorna una o più gem specifiche solo alla prossima versione patch:

`bundle update --patch {{nome_gem1}} {{nome_gem2}}`

- Aggiorna tutte le gem del gruppo specificato nel `Gemfile`:

`bundle update --group {{development}}`

- Elenca le gem installate del `Gemfile` con versioni più recenti disponibili:

`bundle outdated`

- Crea uno scheletro per una nuova gem:

`bundle gem {{nome_gem}}`
