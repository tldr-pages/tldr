# gh աշխատանքային հոսք

> Ցուցակել, դիտել և գործարկել GitHub Actions-ի աշխատանքային հոսքերը:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_workflow>:.

- Ինտերակտիվ կերպով ընտրեք աշխատանքային հոսք՝ վերջին աշխատանքները դիտելու համար՝:

`gh workflow view`

- Դիտեք որոշակի աշխատանքային հոսք լռելյայն դիտարկիչում.:

`gh workflow view {{id|workflow_name|filename.yml}} {{[-w|--web]}}`

- Ցուցադրել հատուկ աշխատանքային հոսքի YAML սահմանումը.:

`gh workflow view {{id|workflow_name|filename.yml}} {{[-y|--yaml]}}`

- Ցուցադրել YAML սահմանումը որոշակի Git մասնաճյուղի կամ պիտակի համար.:

`gh workflow view {{id|workflow_name|filename.yml}} {{[-r|--ref]}} {{branch|tag_name}} {{[-y|--yaml]}}`

- Ցուցակեք աշխատանքային հոսքի ֆայլերը (օգտագործեք `--all`՝ անջատված աշխատանքային հոսքերը ներառելու համար).:

`gh workflow {{[ls|list]}}`

- Գործարկել ձեռքով աշխատանքային հոսք պարամետրերով.:

`gh workflow run {{id|workflow_name|filename.yml}} {{--raw-field param1=value1 --raw-field param2=value2 ...}}`

- Գործարկեք ձեռքով աշխատանքային հոսք՝ օգտագործելով որոշակի ճյուղ կամ հատկորոշիչ՝ JSON պարամետրերով `stdin`-ից:

`echo '{{{"param1": "value1", "param2": "value2", ...}}}' | gh workflow run {{id|workflow_name|filename.yml}} {{[-r|--ref]}} {{branch|tag_name}}`

- Միացնել կամ անջատել որոշակի աշխատանքային հոսք.:

`gh workflow {{enable|disable}} {{id|workflow_name|filename.yml}}`
