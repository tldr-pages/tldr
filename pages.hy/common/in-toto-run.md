# in-toto-վազում

> Մատակարարման շղթայի քայլն իրականացնելիս կապի մետատվյալների ստեղծում:.
> Լրացուցիչ տեղեկություններ. <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-run.html>:.

- Նշեք Git ռեպո-ն և ստորագրելով ստացված հղման ֆայլը.:

`in-toto-run {{[-n|--step-name]}} {{tag}} {{[-p|--products]}} {{.}} --signing-key {{key_file}} -- {{git tag v1.0}}`

- Ստեղծեք tarball՝ ֆայլերը պահելով որպես նյութեր և tarball՝ որպես արտադրանք.:

`in-toto-run {{[-n|--step-name]}} {{package}} {{[-m|--materials]}} {{project}} {{[-p|--products]}} {{project.tar.gz}} -- {{tar czf project.tar.gz project}}`

- Ստեղծեք ստորագրված ատեստավորումներ վերանայման աշխատանքների համար.:

`in-toto-run {{[-n|--step-name]}} {{review}} --signing-key {{key_file}} {{[-m|--materials]}} {{document.pdf}} {{[-x|--no-command]}}`

- Սկանավորեք պատկերը Trivy-ի միջոցով և ստեղծեք հղման ֆայլ.:

`in-toto-run {{[-n|--step-name]}} {{scan}} --signing-key {{key_file}} {{[-p|--products]}} {{report.json}} -- /bin/sh -c "trivy --output report.json --format json {{path/to/image}}"`
