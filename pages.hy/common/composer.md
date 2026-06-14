#կոմպոզիտոր

> Փաթեթի վրա հիմնված կախվածության կառավարիչ PHP նախագծերի համար:.
> Լրացուցիչ տեղեկություններ. <https://getcomposer.org/doc/03-cli.md>:.

- Ինտերակտիվ կերպով ստեղծեք `composer.json` ֆայլ.:

`composer init`

- Ավելացրեք փաթեթ որպես կախվածություն այս նախագծի համար՝ ավելացնելով մուտք `composer.json`:

`composer require {{user/package}}`

- Տեղադրեք բոլոր կախվածությունները այս նախագծի `composer.json`-ում և ստեղծեք `composer.lock`:

`composer install`

- Ապատեղադրեք փաթեթն այս նախագծից՝ հեռացնելով այն որպես կախվածություն `composer.json` և `composer.lock`-ից:

`composer remove {{user/package}}`

- Թարմացրեք այս նախագծի `composer.json` բոլոր կախվածությունները և նշեք նոր տարբերակները `composer.lock` ֆայլում՝:

`composer update`

- Թարմացրեք միայն `composer.lock` `composer.json`-ը ձեռքով թարմացնելուց հետո:

`composer update --lock`

- Իմացեք ավելին այն մասին, թե ինչու չի կարող տեղադրվել կախվածությունը.:

`composer why-not {{user/package}}`

- Թարմացրեք կոմպոզիտորին իր վերջին տարբերակին.:

`composer self-update`
