# npm աստղ

> Նշեք փաթեթը որպես սիրելի:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-star/>:.

- Աստղանշեք հանրային փաթեթը լռելյայն ռեգիստրից.:

`npm star {{package_name}}`

- Փաթեթի աստղանշում որոշակի շրջանակում.:

`npm star @{{scope}}/{{package_name}}`

- Աստղանշեք փաթեթը որոշակի ռեեստրից.:

`npm star {{package_name}} --registry {{registry_url}}`

- Աստղանշեք մասնավոր փաթեթ, որը պահանջում է նույնականացում.:

`npm star {{package_name}} --auth-type {{legacy|oauth|web|saml}}`

- Աստղանշեք փաթեթը՝ տրամադրելով OTP երկգործոն նույնականացման համար.:

`npm star {{package_name}} --otp {{otp}}`

- Աստղանշեք փաթեթը մանրամասն գրանցմամբ.:

`npm star {{package_name}} --loglevel verbose`

- Նշեք ձեր բոլոր աստղանշված փաթեթները.:

`npm star --list`

- Նշեք ձեր աստղանշված փաթեթները որոշակի ռեեստրից.:

`npm star --list --registry {{registry_url}}`
