#բուսական

> Կոմունալ ծրագիր և գրադարան HTTP բեռնվածության փորձարկման համար:.
> Տես նաև՝ `ab`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tsenart/vegeta#usage-manual>:.

- Գործարկել 30 վայրկյան տևողությամբ հարձակումը.:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}`

- Հարձակում գործարկեք սերվերի վրա ինքնաստորագրված HTTPS վկայականով.:

`echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}`

- Գործարկել հարձակումը վայրկյանում 10 հարցումների արագությամբ.:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- Գործարկեք հարձակում և ցուցադրեք զեկույց.:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- Գործարկեք հարձակումը և արդյունքները գծեք գրաֆիկի վրա (ժամանակի հետ կապված ուշացում).:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{path/to/results.html}}`

- Գործարկեք հարձակում ֆայլից բազմաթիվ URL-ների դեմ.:

`vegeta attack -duration={{30s}} -targets={{requests.txt}} | vegeta report`
