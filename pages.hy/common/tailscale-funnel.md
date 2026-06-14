# tailscale ձագար

> Համօգտագործեք տեղական սերվերը ինտերնետում, օգտագործելով Tailscale:.
> Լրացուցիչ տեղեկություններ. <https://tailscale.com/kb/1311/tailscale-funnel>:.

- Բացահայտեք տեղական ֆայլը կամ գրացուցակը առաջին պլանում.:

`tailscale funnel {{path/to/file_or_directory}}`

- Առաջին պլանում ցուցադրեք 127.0.0.1:3000-ով աշխատող HTTP սերվերը.:

`tailscale funnel 3000`

- Բացահայտեք HTTP սերվերը, որն աշխատում է 127.0.0.1:3000 ֆոնին.:

`tailscale funnel --bg 3000`

- Բացահայտեք HTTPS սերվերը անվավեր կամ ինքնաստորագրված վկայականներով https://localhost:8443:

`tailscale funnel https+insecure://localhost:8443`
