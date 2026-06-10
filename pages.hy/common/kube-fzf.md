# kube-fzf

> Shell հրամաններ Kubernetes Pods-ի հրամանների տողում մշուշոտ որոնման համար:.
> Տես նաև՝ `kubectl`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/thecasualcoder/kube-fzf>:.

- Ստացեք pod մանրամասները (ներկայիս անվանատարածքից).:

`findpod`

- Ստացեք pod մանրամասները (բոլոր անվանատարածքներից).:

`findpod -a`

- Նկարագրեք պատիճ.:

`describepod`

- Պոչամբարի տեղեկամատյաններ.:

`tailpod`

- Exec մեջ pod-ի կոնտեյներով:

`execpod {{shell_command}}`

- Port-forward a pod:

`pfpod {{port_number}}`
