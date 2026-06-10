# tailscale ssh

> SSH դեպի Tailscale մեքենա (միայն Linux):.
> Լրացուցիչ տեղեկություններ. <https://tailscale.com/kb/1193/tailscale-ssh>:.

- Գովազդեք/անջատեք SSH-ը հյուրընկալողի վրա.:

`tailscale up --ssh={{true|false}}`

- SSH կոնկրետ հոսթին, որն ունի Tailscale-SSH միացված.:

`tailscale ssh {{username}}@{{host}}`
