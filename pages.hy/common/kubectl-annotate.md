# kubectl ծանոթագրություն

> Նշում է Kubernetes-ի ռեսուրսները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate/>:.

- Նշեք պատիճ.:

`kubectl annotate {{[po|pods]}} {{pod_name}} {{key}}={{value}}`

- Թարմացրեք պատի անոտացիան՝ վերագրելով առկա արժեքը.:

`kubectl annotate {{[po|pods]}} {{pod_name}} {{key}}={{value}} --overwrite`

- Նշեք բոլոր պատյանները անունների տարածքում հատուկ պիտակի ընտրիչով.:

`kubectl annotate {{[po|pods]}} {{key}}={{value}} {{[-l|--selector]}} {{label_key}}={{label_value}}`

- Թվարկեք բոլոր անոտացիաները, որոնք ունի pod.:

`kubectl annotate {{[po|pods]}} {{pod_name}} --list`

- Հեռացրեք ծանոթագրությունը պատյանից.:

`kubectl annotate {{[po|pods]}} {{pod_name}} {{key}}-`
