# devcontainer

> Օգտագործեք Docker կոնտեյներ որպես զարգացման միջավայր:.
> Լրացուցիչ տեղեկություններ. <https://containers.dev/implementors/reference/>:.

- Ստեղծեք և գործարկեք Dev Container.:

`devcontainer up`

- Կիրառեք Dev Container կաղապարը աշխատանքային տարածքում.:

`devcontainer templates apply {{[-t|--template-id]}} {{template_id}} {{[-a|--template-args]}} {{template_args}} {{[-w|--workspace-folder]}} {{path/to/workspace}}`

- Կատարեք հրաման ընթացիկ աշխատանքային տարածքում գործող Dev Container-ի վրա.:

`devcontainer exec {{command}}`

- Ստեղծեք Dev Container պատկեր `devcontainer.json`-ից:

`devcontainer build {{path/to/workspace}}`

- Կարդացեք և տպեք Dev Container-ի կոնֆիգուրացիան `devcontainer.json`-ից:

`devcontainer read-configuration`
