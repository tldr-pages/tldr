# kubectl պիտակ

> Նշել Kubernetes-ի ռեսուրսները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_label/>:.

- Պիտակավորեք պատիճը.:

`kubectl label {{[po|pods]}} {{pod_name}} {{key}}={{value}}`

- Թարմացրեք pod պիտակը` վերագրելով առկա արժեքը.:

`kubectl label {{[po|pods]}} {{pod_name}} {{key}}={{value}} --overwrite`

- Նշեք բոլոր պատիճները անունների տարածքում.:

`kubectl label {{[po|pods]}} {{key}}={{value}} --all`

- Պիտակավորեք պատիճը, որը նույնականացվում է պատիճ սահմանման ֆայլով.:

`kubectl label {{[-f|--filename]}} {{pod_definition_file}} {{key}}={{value}}`

- Հեռացրեք պիտակը պատյանից.:

`kubectl label {{[po|pods]}} {{pod_name}} {{key}}-`
