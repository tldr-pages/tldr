# az հաշիվ

> Կառավարեք Azure-ի բաժանորդագրության տեղեկատվությունը:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/account>:.

- Նշեք բոլոր բաժանորդագրությունները մուտք գործած հաշվի համար.:

`az account list`

- Սահմանեք `subscription` որպես ընթացիկ ակտիվ բաժանորդագրություն՝:

`az account set {{[-s|--subscription]}} {{subscription_id}}`

- Ցուցակեք աջակցվող տարածաշրջանները ներկայումս ակտիվ բաժանորդագրության համար.:

`az account list-locations`

- Տպեք մուտքի նշան, որը կօգտագործվի `MS Graph API`-ով.:

`az account get-access-token --resource-type {{ms-graph}}`

- Տպել տվյալ պահին ակտիվ բաժանորդագրության մանրամասները հատուկ ձևաչափով.:

`az account show {{[-o|--output]}} {{json|tsv|table|yaml}}`
