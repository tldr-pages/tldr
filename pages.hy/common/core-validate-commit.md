# core-validate-commit

> Վավերացրեք ստանձնման հաղորդագրությունները Node.js միջուկի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/nodejs/core-validate-commit>:.

- Վավերացրեք ընթացիկ պարտավորությունը.:

`core-validate-commit`

- Վավերացնել կոնկրետ պարտավորություն.:

`core-validate-commit {{commit_hash}}`

- Վավերացրեք մի շարք պարտավորություններ.:

`git rev-list {{commit_hash}}..HEAD | xargs core-validate-commit`

- Թվարկեք վավերացման բոլոր կանոնները.:

`core-validate-commit {{[-l|--list]}}`

- Նշեք բոլոր վավերական Node.js ենթահամակարգերը.:

`core-validate-commit {{[-ls|--list-subsystem]}}`

- Վավերացրեք ընթացիկ commit-ը, որը ձևավորում է ելքը թակել ձևաչափով.:

`core-validate-commit {{[-t|--tap]}}`

- Ցուցադրել օգնությունը.:

`core-validate-commit {{[-h|--help]}}`
