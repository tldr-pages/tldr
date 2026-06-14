# npm հանել աստղանիշը

> Հեռացրեք սիրելի/աստղի նշանը փաթեթից:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-unstar/>:.

- Հեռացնել հանրային փաթեթի աստղանշումը լռելյայն ռեեստրից.:

`npm unstar {{package_name}}`

- Փաթեթի աստղանշումը որոշակի շրջանակում.:

`npm unstar @{{scope}}/{{package_name}}`

- Փաթեթը հանել աստղանիշը կոնկրետ ռեեստրից.:

`npm unstar {{package_name}} --registry {{registry_url}}`

- Հեռացնել աստղանիշը մի մասնավոր փաթեթ, որը պահանջում է նույնականացում.:

`npm unstar {{package_name}} --auth-type {{legacy|oauth|web|saml}}`

- Ապացուցադրել փաթեթը՝ տրամադրելով OTP երկգործոն նույնականացման համար.:

`npm unstar {{package_name}} --otp {{otp}}`

- Ապացուցադրել փաթեթը հատուկ գրանցման մակարդակով.:

`npm unstar {{package_name}} --loglevel {{silent|error|warn|notice|http|timing|info|verbose|silly}}`
