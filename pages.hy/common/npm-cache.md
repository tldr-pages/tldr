# npm քեշ

> Կառավարեք npm փաթեթի քեշը:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-cache/>:.

- Քեշին հատուկ փաթեթ ավելացրեք.:

`npm cache add {{package_name}}`

- Մաքրել հատուկ պահված տարրը բանալիով.:

`npm cache clean {{key}}`

- Մաքրել ամբողջ npm քեշը.:

`npm cache clean {{[-f|--force]}}`

- Ցուցակեք պահված փաթեթները.:

`npm cache ls`

- Ցուցակեք քեշավորված փաթեթները, որոնք համապատասխանում են կոնկրետ անվանմանը և տարբերակին.:

`npm cache ls {{name}}@{{version}}`

- Ստուգեք npm քեշի ամբողջականությունը.:

`npm cache verify`

- Թվարկեք բոլոր գրառումները npx քեշում.:

`npm cache npx ls`
