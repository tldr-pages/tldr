# argocd հավելված

> Ինտերֆեյս՝ Argo CD-ով հավելվածները կառավարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>:.

- Ցուցակ հայտերը.:

`argocd app list --output {{json|yaml|wide}}`

- Ստացեք դիմումի մանրամասները.:

`argocd app get {{app_name}} --output {{json|yaml|wide}}`

- Տեղադրեք հավելվածը ներսում (նույն կլաստերին, որտեղ աշխատում է Argo CD-ն).:

`argocd app create {{app_name}} --repo {{git_repo_url}} --path {{path/to/repo}} --dest-server https://kubernetes.default.svc --dest-namespace {{ns}}`

- Ջնջել հավելվածը.:

`argocd app delete {{app_name}}`

- Միացնել հավելվածի ավտոմատ համաժամացումը.:

`argocd app set {{app_name}} --sync-policy auto --auto-prune --self-heal`

- Նախադիտեք հավելվածների համաժամացումը առանց կլաստերի վրա ազդելու.:

`argocd app sync {{app_name}} --dry-run --prune`

- Ցուցադրել հավելվածի տեղակայման պատմությունը.:

`argocd app history {{app_name}} --output {{wide|id}}`

- Պատմության ID-ով նախկինում տեղադրված տարբերակի հետ վերադարձի դիմում (անսպասելի ռեսուրսների ջնջում).:

`argocd app rollback {{app_name}} {{history_id}} --prune`
