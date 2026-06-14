#Վելա

> Գործիքներ Vela խողովակաշարի համար:.
> Լրացուցիչ տեղեկություններ. <https://go-vela.github.io/docs/reference/cli>:.

- Գործարկեք խողովակաշար, որը կգործի Git ճյուղից, կատարեք կամ նշեք.:

`vela add deployment --org {{organization}} --repo {{repository_name}} --target {{environment}} --ref {{branch|commit|refs/tags/git_tag}} --description "{{deploy_description}}"`

- Ցուցակեք տեղակայումները պահեստի համար.:

`vela get deployment --org {{organization}} --repo {{repository_name}}`

- Ստուգեք կոնկրետ տեղակայումը.:

`vela view deployment --org {{organization}} --repo {{repository_name}} --deployment {{deployment_number}}`
