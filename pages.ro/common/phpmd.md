# phpmd

> Un detector de mizerie PHP care verifică eventualele probleme comune.
> Mai multe informaţii: <https://github.com/phpmd/phpmd>

- Afișează o listă de reguli și formate disponibile:

`phpmd`

- Scanați un fișier sau un director pentru probleme utilizând eturile de reguli separate prin virgulă:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}}`

- Specificați pragul minim de prioritate pentru reguli:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --minimumpriority {{priority}}`

- Includeți numai extensiile specificate în analiză:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --suffixes {{extensions}}`

- Excludeți directoarele separate prin virgulă specificate:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --exclude {{directory_patterns}}`

- Ieșiți rezultatele într-un fișier în loc de stdout:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --reportfile {{path/to/report_file}}`

- Ignorați utilizarea comentariilor phpDoc care suprimă avertismente:

`phpmd {{path/to/file_or_directory}} {{xml|text|html}} {{rulesets}} --strict`
