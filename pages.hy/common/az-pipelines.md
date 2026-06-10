# az խողովակաշարեր

> Կառավարեք Azure Pipelines-ի ռեսուրսները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/pipelines>:.

- Ստեղծեք նոր Azure խողովակաշար (YAML-ի վրա հիմնված).:

`az pipelines create {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}} --description {{description}} --repository {{repository_name}} --branch {{branch_name}}`

- Ջնջել կոնկրետ խողովակաշար.:

`az pipelines delete {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --id {{pipeline_id}}`

- Ցուցակ խողովակաշարեր.:

`az pipelines list {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}}`

- Հերթագրեք որոշակի խողովակաշար՝ գործարկելու համար.:

`az pipelines run {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}}`

- Ստացեք կոնկրետ խողովակաշարի մանրամասները.:

`az pipelines show {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}}`

- Թարմացրեք կոնկրետ խողովակաշար.:

`az pipelines update {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}} --new-name {{pipeline_new_name}} --new-folder-path {{user1/production_pipelines}}`

- Թվարկեք բոլոր գործակալներին լողավազանում.:

`az pipelines agent list {{[--org|--organization]}} {{organization_url}} --pool-id {{agent_pool}}`
