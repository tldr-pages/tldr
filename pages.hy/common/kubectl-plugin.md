# kubectl plugin

> Կառավարեք kubectl հավելվածները, որոնք ընդլայնում են հրամանի ֆունկցիոնալությունը:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_plugin/>:.

- Թվարկե՛ք համակարգի բոլոր հասանելի հավելվածները `$PATH`:

`kubectl plugin list`

- Թվարկեք միայն հասանելի պլագինների գործարկվող անուններն առանց ամբողջական ուղիների.:

`kubectl plugin list --name-only`

- Ցուցադրել օգնությունը.:

`kubectl plugin {{[-h|--help]}}`
