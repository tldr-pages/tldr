# ղեկի տեղադրում

> Տեղադրեք ղեկի գծապատկեր:.
> Լրացուցիչ տեղեկություններ. <https://helm.sh/docs/intro/using_helm/#helm-install-installing-a-package>:.

- Տեղադրեք ղեկի աղյուսակը.:

`helm install {{name}} {{repository_name}}/{{chart_name}}`

- Տեղադրեք ղեկային աղյուսակը չփաթեթավորված գծապատկերային գրացուցակից.:

`helm install {{name}} {{path/to/source_directory}}`

- Տեղադրեք ղեկային աղյուսակը URL-ից.:

`helm install {{package_name}} {{https://example.com/charts/packagename-1.2.3.tgz}}`

- Տեղադրեք ղեկի աղյուսակը և ստեղծեք անուն.:

`helm install {{repository_name}}/{{chart_name}} {{[-g|--generate-name]}}`

- Կատարել չոր վազք.:

`helm install {{name}} {{repository_name}}/{{chart_name}} --dry-run`

- Տեղադրեք ղեկային գծապատկեր՝ հատուկ արժեքներով.:

`helm install {{name}} {{repository_name}}/{{chart_name}} --set {{parameter1}}={{value1}},{{parameter2}}={{value2}}`

- Տեղադրեք ղեկի գծապատկերը, որն անցնում է հատուկ արժեքների ֆայլ.:

`helm install {{name}} {{repository_name}}/{{chart_name}} {{[-f|--values]}} {{path/to/values.yaml}}`
