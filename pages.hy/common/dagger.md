# դաշույն

> Ծրագրավորվող CI/CD շարժիչ, որը խողովակաշարերն աշխատում է բեռնարկղերում տեղական, CI-ում կամ ամպի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://docs.dagger.io/reference/cli>:.

- Նախաձեռնեք նոր մոդուլ նշված SDK-ով.:

`dagger init --sdk {{go|python|typescript}} {{path/to/module}}`

- Մշակել տեղական մոդուլ.:

`dagger develop`

- Թվարկեք առկա գործառույթները ընթացիկ մոդուլում.:

`dagger functions`

- Կանչեք գործառույթ ընթացիկ մոդուլի վրա.:

`dagger call {{function_name}}`

- Տեղադրեք մոդուլի կախվածությունը Git պահոցից.:

`dagger install {{github.com/user/repo}}`

- Թարմացրեք մոդուլի կախվածությունները.:

`dagger update`

- Ցուցադրել օգնությունը.:

`dagger {{[-h|--help]}}`

- Ցուցադրման տարբերակը:

`dagger version`
