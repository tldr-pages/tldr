# k3d

> Դոկերի ներսում k3s կլաստերներ հեշտությամբ ստեղծելու փաթաթան:.
> Լրացուցիչ տեղեկություններ. <https://k3d.io/stable/usage/commands/>:.

- Ստեղծեք կլաստեր.:

`k3d cluster create {{cluster_name}}`

- Ջնջել կլաստերը.:

`k3d cluster delete {{cluster_name}}`

- Ստեղծեք նոր կոնտեյներացված k3s հանգույց.:

`k3d node create {{node_name}}`

- Ներմուծեք պատկեր Docker-ից k3d կլաստերի մեջ.:

`k3d image import {{image_name}} {{[-c|--cluster]}} {{cluster_name}}`

- Ստեղծեք նոր ռեեստր.:

`k3d registry create {{registry_name}}`
