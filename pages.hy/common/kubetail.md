# kubetail

> Կոմունալ՝ միաժամանակ մի քանի Kubernetes pod տեղեկամատյաններ պոչելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/johanhaleby/kubetail>:.

- Միանգամից միացրեք բազմաթիվ պատյանների տեղեկամատյանները (որոնց անունը սկսվում է `app_name`-ով):

`kubetail {{app_name}}`

- Պոչեք միայն որոշակի կոնտեյներ բազմաթիվ պատյաններից.:

`kubetail {{app_name}} {{[-c|--container]}} {{container_name}}`

- Պոչը մի քանի տարաներ բազմաթիվ պատյաններից.:

`kubetail {{app_name}} {{[-c|--container]}} {{container_name_1}} {{[-c|--container]}} {{container_name_2}}`

- Միևնույն ժամանակ մի քանի հավելվածներ բաժանեք ստորակետով.:

`kubetail {{app_name_1,app_name_2,...}}`
