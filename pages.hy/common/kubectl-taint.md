# kubectl արատ

> Թարմացրեք հանգույցների ախտահարումները:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_taint/>:.

- Կիրառել բիծը հանգույցի վրա.:

`kubectl taint {{[no|nodes]}} {{node_name}} {{label_key}}={{label_value}}:{{effect}}`

- Հեռացնել բծը հանգույցից.:

`kubectl taint {{[no|nodes]}} {{node_name}} {{label_key}}:{{effect}}-`

- Հեռացրեք բոլոր բիծերը հանգույցից.:

`kubectl taint {{[no|nodes]}} {{node_name}} {{label_key}}-`
