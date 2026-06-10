# doctl auth

> Նույնականացրեք `doctl`-ը API նշաններով:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/auth/>:.

- Բացեք API նշան մուտքագրելու հուշում և պիտակավորեք դրա համատեքստը.:

`doctl auth init --context {{token_label}}`

- Նշեք նույնականացման համատեքստերը (API նշաններ).:

`doctl auth {{[ls|list]}}`

- Փոխարկել համատեքստերը (API նշաններ).:

`doctl auth switch --context {{token_label}}`

- Հեռացրեք պահպանված վավերացման համատեքստը (API նշան).:

`doctl auth remove --context {{token_label}}`

- Ցույց տալ առկա հրամանները.:

`doctl auth {{[-h|--help]}}`
