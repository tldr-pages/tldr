# ag

> The Silver Searcher. Zoals ack, maar wil sneller zijn.
> Meer informatie: <https://github.com/ggreer/the_silver_searcher>.

- Zoek bestanden die "foo" bevatten en druk de regelovereenkomsten in context af:

`ag {{foo}}`

- Vind bestanden die "foo" bevatten in een specifieke map:

`ag {{foo}} {{pad/naar/map}}`

- Vind bestanden die "foo" bevatten, maar vermeld alleen de bestandsnamen:

`ag -l {{foo}}`

- Vind bestanden die "FOO" niet hoofdlettergevoelig bevatten en druk alleen de overeenkomst af in plaats van de hele regel:

`ag -i -o {{FOO}}`

- Zoek "foo" in bestanden met een naam die overeenkomt met "bar":

`ag {{foo}} -G {{bar}}`

- Vind bestanden waarvan de inhoud overeenkomt met een reguliere expressie:

`ag '{{^ba(r|z)$}}'`

- Zoek bestanden met een naam die overeenkomt met "foo":

`ag -g {{foo}}`
