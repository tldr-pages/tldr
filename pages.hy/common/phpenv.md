# phpenv

> PHP տարբերակի կառավարիչ՝ զարգացման նպատակներով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/phpenv/phpenv>:.

- Տեղադրեք PHP տարբերակը գլոբալ.:

`phpenv install {{version}}`

- Թարմացրեք shim ֆայլերը բոլոր PHP երկուականների համար, որոնք հայտնի են `phpenv`-ին:

`phpenv rehash`

- Թվարկեք բոլոր տեղադրված PHP տարբերակները.:

`phpenv versions`

- Ցուցադրել ներկայումս ակտիվ PHP տարբերակը.:

`phpenv version`

- Սահմանեք PHP-ի գլոբալ տարբերակը.:

`phpenv global {{version}}`

- Սահմանեք տեղական PHP տարբերակը, որը վերացնում է գլոբալ տարբերակը.:

`phpenv local {{version}}`

- Չեղարկեք տեղական PHP տարբերակը.:

`phpenv local --unset`
