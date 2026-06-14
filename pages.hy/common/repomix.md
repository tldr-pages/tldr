# repomix

> Փաթեթավորեք Github պահեստը AI-ի համար հարմար ֆայլի մեջ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/yamadashy/repomix>:.

- Արդյունքների մաքսային ձևաչափ.:

`repomix {{[-o|--output]}} {{path/to/file}} --style {{xml|markdown|plain}}`

- Ուղարկեք արդյունքը `stdout` հասցեին՝:

`repomix --stdout > {{path/to/file}}`

- Ուղարկեք արդյունքը `stdout`-ին, այնուհետև մուտքագրեք մեկ այլ ծրագիր.:

`repomix --stdout | {{less}}`

- Արդյունք սեղմումով.:

`repomix --compress`

- Մշակել հատուկ ֆայլեր.:

`repomix --include "{{src/**/*.ts}}" --ignore "{{**/*.test.ts}}"`

- Փաթեթավորեք պահեստը մասնաճյուղից.:

`repomix --remote {{https://github.com/user/repo/tree/main}}`

- Փաթեթավորեք պահեստը որոշակի պարտավորության մեջ.:

`repomix --remote {{https://github.com/user/repo/commit/836abcd7335137228ad77feb28655d85712680f1}}`

- Փաթեթավորեք պահեստը՝ օգտագործելով սղագրությունը.:

`repomix --remote {{user/repo}}`
