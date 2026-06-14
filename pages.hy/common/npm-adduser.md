# npm ավելացնող

> Ավելացնել ռեեստրի օգտատիրոջ հաշիվ:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-adduser/>:.

- Ստեղծեք նոր օգտվող նշված ռեեստրում և պահպանեք հավատարմագրերը `.npmrc`-ում:

`npm adduser --registry {{registry_url}}`

- Մուտք գործեք մասնավոր ռեգիստր հատուկ շրջանակով.:

`npm login --scope {{@organization}} --registry {{https://registry.example.com}}`

- Դուրս եկեք որոշակի շրջանակից և հեռացրեք վավերացման նշանը.:

`npm logout --scope {{@organization}}`

- Նախաստորագրման ընթացքում ստեղծեք շրջանակային փաթեթ.:

`npm init --scope {{@organization}} {{[-y|--yes]}}`
