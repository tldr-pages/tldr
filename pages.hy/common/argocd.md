#argocd

> Ինտերֆեյս՝ Argo CD սերվերը կառավարելու համար:.
> Որոշ ենթահրամաններ, ինչպիսիք են `app`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>:.

- Մուտք գործեք Argo CD սերվեր.:

`argocd login --insecure --username {{user}} --password {{password}} {{argocd_server:port}}`

- Ցուցակ հայտերը.:

`argocd app list`
