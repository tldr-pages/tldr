# npm հրապարակում

> Հրապարակեք փաթեթ npm ռեեստրում:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/publish/>:.

- Հրապարակեք ընթացիկ փաթեթը լռելյայն npm ռեեստրում.:

`npm publish`

- Հրապարակեք փաթեթ որոշակի գրացուցակից.:

`npm publish {{path/to/package_directory}}`

- Հրապարակեք շրջանակային փաթեթ՝ հանրային հասանելիությամբ.:

`npm publish --access public`

- Հրապարակեք սահմանափակ (մասնավոր) մուտքով փաթեթավորված փաթեթ.:

`npm publish --access restricted`

- Փաթեթ հրապարակեք մաքսային գրանցամատյանում.:

`npm publish --registry {{https://registry.npmjs.org/}}`

- Անցեք չոր վազք՝ տեսնելու, թե ինչ կհրապարակվի առանց վերբեռնելու.:

`npm publish --dry-run`

- Հրապարակեք փաթեթ հատուկ բաշխման պիտակով (օրինակ՝ բետա).:

`npm publish --tag {{beta}}`

- Հրապարակեք մեկանգամյա գաղտնաբառով 2FA-ով միացված հաշիվների համար.:

`npm publish --otp {{one_time_password}}`
