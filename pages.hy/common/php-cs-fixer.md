# php-cs-fixer

> PHP-ի համար կոդավորման ոճի ավտոմատ ամրագրիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/PHP-CS-Fixer/PHP-CS-Fixer>:.

- Կատարեք կոդի ոճի ամրագրում ընթացիկ գրացուցակում.:

`php-cs-fixer fix`

- Կատարեք կոդի ոճի ամրագրում որոշակի գրացուցակի համար.:

`php-cs-fixer fix {{path/to/directory}}`

- Կատարեք կոդի ոճի linting՝ առանց փոփոխություններ կիրառելու.:

`php-cs-fixer fix --dry-run`

- Կատարեք կոդի ոճի ուղղումներ՝ օգտագործելով հատուկ կանոններ.:

`php-cs-fixer fix --rules={{rules}}`

- Ցուցադրել կիրառված կանոնները.:

`php-cs-fixer fix --verbose`

- Արդյունքները թողարկեք այլ ձևաչափով.:

`php-cs-fixer fix --format={{txt|json|xml|checkstyle|junit|gitlab}}`

- Ցուցադրել ֆայլեր, որոնք պահանջում են ամրագրում.:

`php-cs-fixer list-files`

- Նկարագրեք կանոն կամ կանոնակարգ.:

`php-cs-fixer describe {{rule}}`
