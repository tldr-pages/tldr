#ասցիինեմա

> Ձայնագրեք և վերարտադրեք տերմինալի նիստերը և կամայականորեն տարածեք դրանք <https://asciinema.org> կայքում:.
> Տես նաև՝ `terminalizer`, `agg`:.
> Լրացուցիչ տեղեկություններ. <https://docs.asciinema.org/manual/cli/>:.

- Կապել `asciinema`-ի տեղական տեղադրումը asciinema.org հաշվի հետ.:

`asciinema {{[a|auth]}}`

- Կատարեք նոր ձայնագրություն և պահեք այն տեղական ֆայլում (ավարտեք այն `<Ctrl d>`-ով կամ մուտքագրեք `exit`):

`asciinema {{[r|record]}} {{path/to/recording.cast}}`

- Վերարտադրեք տերմինալի ձայնագրությունը տեղական ֆայլից.:

`asciinema {{[p|play]}} {{path/to/recording.cast}}`

- Կրկնել <https://asciinema.org> կայքում տեղադրված տերմինալի ձայնագրությունը.:

`asciinema {{[p|play]}} https://asciinema.org/a/{{cast_id}}`

- Կատարեք նոր ձայնագրություն՝ սահմանափակելով ցանկացած անգործության ժամանակը առավելագույնը 2,5 վայրկյանով:

`asciinema {{[r|record]}} {{[-i|--idle-time-limit]}} 2.5`

- Տպեք տեղական պահպանված ձայնագրության ամբողջական արդյունքը.:

`asciinema {{[ca|cat]}} {{path/to/recording.cast}}`

- Վերբեռնեք տեղական պահպանված տերմինալային նստաշրջան asciinema.org-ում:

`asciinema {{[u|upload]}} {{path/to/recording.cast}}`

- Հեռարձակեք ընթացիկ տերմինալը տեղական կայքէջում.:

`asciinema {{[st|stream]}} --local`
