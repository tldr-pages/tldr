# gh ssh-key

> Կառավարեք GitHub SSH ստեղները:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_ssh-key>:.

- Ցուցակեք SSH ստեղները տվյալ պահին վավերացված օգտվողի համար.:

`gh ssh-key {{[ls|list]}}`

- Ներկայիս վավերացված օգտվողի հաշվին ավելացրեք SSH բանալի.:

`gh ssh-key add {{path/to/key.pub}}`

- Ներկայիս վավերացված օգտվողի հաշվին ավելացրեք SSH բանալի հատուկ վերնագրով.:

`gh ssh-key add {{[-t|--title]}} {{title}} {{path/to/key.pub}}`

- Ցուցադրել օգնությունը.:

`gh ssh-key`
