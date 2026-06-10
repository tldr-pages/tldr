# npm չեղարկել հրապարակումը

> Հեռացրեք փաթեթը npm ռեեստրից:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-unpublish/>:.

- Չհրապարակել որոշակի փաթեթի տարբերակը.:

`npm unpublish {{package_name}}@{{version}}`

- Չհրապարակել ամբողջ փաթեթը.:

`npm unpublish {{package_name}} {{[-f|--force]}}`

- Չհրապարակել փաթեթը, որը ներառում է.:

`npm unpublish @{{scope}}/{{package_name}}`

- Նշեք ժամանակի վերջնաժամկետը, նախքան չհրապարակելը.:

`npm unpublish {{package_name}} --timeout {{time_in_milliseconds}}`

- Չոր վազիր՝ տեսնելու, թե ինչ կարող է չհրապարակվել առանց իրականում դա անելու.:

`npm unpublish {{package_name}} --dry-run`
