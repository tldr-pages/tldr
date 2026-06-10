# npm տարբերություն

> Համեմատեք փաթեթի տարբերակները `npm` ռեեստրից և ցույց տվեք տարբերությունները:.
> Նման `git diff`-ին:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-diff/>:.

- Համեմատեք երկու կոնկրետ փաթեթի տարբերակներ.:

`npm diff --diff {{package_name}}@{{version1}} --diff {{package_name}}@{{version2}}`

- Համեմատեք ընթացիկ տեղական փաթեթները վերջին հրապարակված տարբերակի հետ.:

`npm diff`

- Համեմատեք ընթացիկ տեղական փաթեթը կոնկրետ տարբերակի հետ.:

`npm diff --diff {{package_name}}@{{version}}`

- Համեմատեք ընթացիկ գրացուցակի փաթեթը ռեեստրի տարբերակի հետ.:

`npm diff --diff {{package_name}}`

- Ցուցադրել միայն տարբեր ֆայլերի անուններ.:

`npm diff --diff-name-only --diff {{package_name}}@{{version1}} --diff {{package_name}}@{{version2}}`

- Համեմատեք միայն կոնկրետ ֆայլեր կամ գրացուցակներ.:

`npm diff {{path/to/file_or_directory}} --diff {{package_name}}@{{version1}} --diff {{package_name}}@{{version2}}`

- Համեմատելիս անտեսել բացատները՝:

`npm diff --diff-ignore-all-space --diff {{package_name}}@{{version1}} --diff {{package_name}}@{{version2}}`
