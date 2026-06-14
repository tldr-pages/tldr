# gitlab

> Ruby wrapper GitLab API-ի համար:.
> Որոշ ենթահրամաններ, ինչպիսիք են `ctl`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://narkoz.github.io/gitlab/>:.

- Ստեղծեք նոր նախագիծ.:

`gitlab create_project {{project_name}}`

- Ստացեք տեղեկատվություն կոնկրետ պարտավորության մասին.:

`gitlab commit {{project_name}} {{commit_hash}}`

- Ստացեք տեղեկատվություն CI խողովակաշարում աշխատատեղերի մասին.:

`gitlab pipeline_jobs {{project_name}} {{pipeline_id}}`

- Սկսեք կոնկրետ CI աշխատանք.:

`gitlab job_play {{project_name}} {{job_id}}`
