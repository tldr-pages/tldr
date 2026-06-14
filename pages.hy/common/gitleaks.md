# gitleaks

> Հայտնաբերեք գաղտնիքները և API ստեղները, որոնք արտահոսել են Git պահեստներում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/gitleaks/gitleaks#usage>:.

- Սկանավորեք հեռավոր պահոց.:

`gitleaks detect --repo-url {{https://github.com/username/repository.git}}`

- Սկանավորեք տեղական գրացուցակը.:

`gitleaks detect {{[-s|--source]}} {{path/to/repository}}`

- Արտադրեք սկանավորման արդյունքները JSON ֆայլ.:

`gitleaks detect {{[-s|--source]}} {{path/to/repository}} --report {{path/to/report.json}}`

- Օգտագործեք հատուկ կանոնների ֆայլ.:

`gitleaks detect {{[-s|--source]}} {{path/to/repository}} --config-path {{path/to/config.toml}}`

- Սկսեք սկանավորումը կոնկրետ պարտավորությունից.:

`gitleaks detect {{[-s|--source]}} {{path/to/repository}} --log-opts {{--since=commit_id}}`

- Սկանավորեք չհաստատված փոփոխությունները մինչև պարտավորությունը.:

`gitleaks protect --staged`

- Ցուցադրել լայնածավալ ելք, որը ցույց է տալիս, թե որ մասերն են հայտնաբերվել որպես արտահոսք սկանավորման ընթացքում.:

`gitleaks protect --staged --verbose`
