# ձեղնահարկ

> Տեղադրեք և կառավարեք բազմատեսակ Kubernetes միջավայրեր՝ օգտագործելով վիրտուալ կլաստերներ:.
> Լրացուցիչ տեղեկություններ. <https://loft.sh/docs/cli/loft/>:.

- Տեղադրեք կամ արդիականացրեք Loft-ը ընթացիկ Kubernetes կլաստերում.:

`loft start`

- Նույնականացրեք հեռավոր Loft օրինակին.:

`loft login {{https://loft.example.com}}`

- Ստեղծեք վիրտուալ կլաստեր հատուկ տարածությամբ և կլաստերով.:

`loft create vcluster {{vcluster_name}} {{[-s|--space]}} {{space_name}} {{[-c|--cluster]}} {{cluster_name}}`

- Թվարկեք բոլոր վիրտուալ կլաստերները.:

`loft list vclusters`

- Փոխեք համատեքստը կոնկրետ վիրտուալ կլաստերի.:

`loft use vcluster {{vcluster_name}}`

- Ջնջել վիրտուալ կլաստերը.:

`loft delete vcluster {{vcluster_name}}`

- Ցույց տալ ընթացիկ Loft օգտվողի անունը.:

`loft vars username`

- Տեղահանեք Loft-ը կլաստերից.:

`loft uninstall`
