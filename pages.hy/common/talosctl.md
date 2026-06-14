# talosctl

> Փոխազդեք Talos Linux-ի հետ՝ նվազագույն և անփոփոխ Kubernetes բաշխում:.
> Տես նաև՝ `kubectl`:.
> Լրացուցիչ տեղեկություններ. <https://docs.siderolabs.com/talos/v1.11/reference/cli>:.

- Կիրառեք կազմաձևը թարմ հանգույցի վրա.:

`talosctl apply-config {{[-i|--insecture]}} {{[-n|--nodes]}} {{control_plane_ip}} {{[-f|--file]}} {{path/to/control_plane.yaml}}`

- Bootstrap `etcd` կլաստերը հանգույցի վրա.:

`talosctl bootstrap {{[-n|--nodes]}} {{node_ip}}`

- Խմբագրել API ռեսուրսը.:

`talosctl edit {{resource_to_edit}} {{[-n|--nodes]}} {{node_ip}}`

- Ստացեք ռեսուրսներ.:

`talosctl get {{resource_to_get}} {{[-n|--nodes]}} {{node_ip}}`

- Ներբեռնեք ադմինիստրատորի kube կոնֆիգուրացիան հանգույցից.:

`talosctl kubeconfig {{[-n|--nodes]}} {{node_ip}}`

- Վերականգնել հանգույցը.:

`talosctl reset {{[-n|--nodes]}} {{node_ip}}`
