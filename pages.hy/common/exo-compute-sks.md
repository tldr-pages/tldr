# exo հաշվողական sk

> Կառավարեք Exoscale Scalable Kubernetes ծառայությունը (SKS):.
> Լրացուցիչ տեղեկություններ. <https://community.exoscale.com/product/compute/containers/>:.

- Թվարկեք SKS կլաստերի աջակցվող տարբերակները.:

`exo compute sks versions`

- Ստեղծեք նոր SKS կլաստեր.:

`exo compute sks create {{cluster_name}} {{[-z|--zone]}} {{zone}}`

- Թվարկեք բոլոր SKS կլաստերները.:

`exo compute sks list`

- Ստեղծեք Kubernetes kubeconfig ֆայլ SKS կլաստերի համար, որն ավարտվում է 1800 վայրկյանից.:

`exo compute sks kubeconfig {{cluster_name|id}} {{user}} --ttl 1800 {{[-z|--zone]}} {{zone}}`

- Ստեղծեք և ավելացրեք 3 հանգույց պարունակող Nodepool SKS կլաստերին.:

`exo compute sks nodepool add {{cluster_name|id}} {{nodepool_name}} --size 3 {{[-z|--zone]}} {{zone}}`

- Հեռացրեք Nodepool-ը SKS կլաստերից.:

`exo compute sks nodepool delete {{cluster_name|id}} {{nodepool_name|id}}`

- Վտարել հանգույցը SKS կլաստերի հանգույցից.:

`exo compute sks nodepool evict {{cluster_name|id}} {{nodepool_name|id}} {{node_name|id}}`

- Միացնել Exoscale CSI դրայվերը գոյություն ունեցող SKS կլաստերի համար.:

`exo compute sks update {{cluster_name|id}} --enable-csi-addon {{[-z|--zone]}} {{zone}}`
