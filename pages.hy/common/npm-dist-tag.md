# npm dist-tag

> Կառավարեք բաշխման պիտակները փաթեթների վրա:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-dist-tag/>:.

- Թվարկեք բոլոր բաշխման պիտակները փաթեթի համար.:

`npm dist-tag ls {{package_name}}`

- Թվարկեք բոլոր բաշխման պիտակները ընթացիկ փաթեթի համար.:

`npm dist-tag ls`

- Ավելացրեք բաշխման պիտակ որոշակի փաթեթի տարբերակին.:

`npm dist-tag add {{package_name}}@{{version}} {{tag}}`

- Հեռացրեք բաշխման պիտակը փաթեթից.:

`npm dist-tag rm {{package_name}} {{tag}}`

- Ավելացրեք պիտակ՝ օգտագործելով npm config-ից կազմաձևված պիտակը.:

`npm dist-tag add {{package_name}}@{{version}}`

- Ավելացրեք պիտակ երկու գործոնով իսկորոշմամբ.:

`npm dist-tag add {{package_name}}@{{version}} {{tag}} --otp {{one_time_password}}`
