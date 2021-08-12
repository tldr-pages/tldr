# vegeta

> Un utilitar de linie de comandă și o bibliotecă pentru testarea încărcării HTTP.
> A se vedea și `ab`.
> Mai multe informaţii: <https://github.com/tsenart/vegeta>

- Lansarea unui atac care durează 30 de secunde:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}`

- Lansarea unui atac pe un server cu un certificat https auto-semnat:

`echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}`

- Lansarea unui atac cu o rată de 10 cereri pe secundă:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- Lansarea unui atac și afișarea unui raport:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- Lansați un atac și trasați rezultatele pe un grafic (latență în timp):

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{path/to/results.html}}`

- Lansarea unui atac împotriva mai multor adrese URL dintr-un fișier:

`vegeta attack -duration={{30s}} -targets={{requests.txt}} | vegeta report`
