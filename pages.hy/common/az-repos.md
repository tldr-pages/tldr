# ազ ռեպո

> Կառավարեք Azure DevOps պահեստները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/repos>:.

- Նշեք բոլոր ռեպոները կոնկրետ նախագծում.:

`az repos list {{[-p|--project]}} {{project_name}}`

- Ավելացրեք քաղաքականություն կոնկրետ պահեստի որոշակի ճյուղի վրա՝ հիմնական միաձուլումը սահմանափակելու համար.:

`az repos policy merge-strategy create --repository-id {{repository_id_in_repos_list}} --branch {{branch_name}} --blocking --enabled --allow-no-fast-forward false --allow-rebase true --allow-rebase-merge true --allow-squash true`

- Ավելացրեք կառուցման վավերացում կոնկրետ պահոցում, օգտագործելով գոյություն ունեցող կառուցման խողովակաշարը, որը ինքնաբերաբար կգործարկվի աղբյուրի թարմացման ժամանակ.:

`az repos policy build create --repository-id {{repository_id}} --build-definition-id {{build_pipeline_id}} --branch main --blocking --enabled --queue-on-source-update-only true --display-name {{name}} --valid-duration {{minutes}}`

- Թվարկեք բոլոր ակտիվ ձգման հարցումները կոնկրետ շտեմարանում կոնկրետ նախագծի շրջանակներում.:

`az repos pr list {{[-p|--project]}} {{project_name}} {{[-r|--repository]}} {{repository_name}} --status active`
