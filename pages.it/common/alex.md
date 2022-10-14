# alex

> Uno strumento per individuare frasi scritte in modo insensibile o sconsiderato.
> Aiuta a trovare termini che favoriscono un certo genere, legati alla razza, religiosamente inappropriati, o simili termini non equi in un testo.
> Maggiori informazioni: <https://github.com/get-alex/alex>.

- Analizza testo da standard input:

`echo {{Frase da analizzare}} | alex --stdin`

- Analizza tutti i file nella cartella corrente:

`alex`

- Analizza uno specifico file:

`alex {{file.md}}`

- Analizza tutti i file Markdown eccetto `esempio.md`:

`alex *.md !{{esempio.md}}`
