# npm կեռիկ

> Կառավարեք `npm` ռեեստրի կեռիկներ փաթեթների համար:.
> Նշում. այս հրամանը հնացել է:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/v10/hook/>:.

- Թվարկեք բոլոր ակտիվ կեռիկները.:

`npm hook ls`

- Ավելացնել նոր կեռիկ փաթեթի համար.:

`npm hook add {{package_name}} {{event}} {{target_url}}`

- Հեռացրեք հատուկ կեռը իր ID-ով.:

`npm hook rm {{hook_id}}`

- Թարմացրեք կեռիկը նոր տեղեկություններով.:

`npm hook update {{hook_id}} {{target_url}}`
