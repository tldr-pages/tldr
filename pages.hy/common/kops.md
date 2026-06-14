#կոպ

> Ստեղծեք, ոչնչացրեք, արդիականացրեք և պահպանեք Kubernetes կլաստերները:.
> Լրացուցիչ տեղեկություններ. <https://kops.sigs.k8s.io/cli/kops/>:.

- Ստեղծեք կլաստեր կազմաձևման ճշգրտումից.:

`kops create cluster {{[-f|--filename]}} {{cluster_name.yaml}}`

- Ստեղծեք նոր SSH հանրային բանալի.:

`kops create sshpublickey {{key_name}} {{[-i|--ssh-public-key]}} {{~/.ssh/id_rsa.pub}}`

- Արտահանել կլաստերի կազմաձևը `~/.kube/config` ֆայլ.:

`kops export kubecfg {{cluster_name}}`

- Ստացեք կլաստերի կոնֆիգուրացիան որպես YAML.:

`kops get cluster {{cluster_name}} {{[-o|--output]}} yaml`

- Ջնջել կլաստերը.:

`kops delete cluster {{cluster_name}} {{[-y|--yes]}}`

- Վավերացնել կլաստերը.:

`kops validate cluster {{cluster_name}} --wait {{wait_time_until_ready}} --count {{num_required_validations}}`
