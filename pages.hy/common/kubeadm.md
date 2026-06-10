# kubeadm

> Ինտերֆեյս Kubernetes կլաստերների ստեղծման և կառավարման համար:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/setup-tools/kubeadm/>:.

- Ստեղծեք Kubernetes կառավարման ինքնաթիռ.:

`kubeadm init`

- Bootstrap Kubernetes աշխատանքային հանգույցը և միացրեք այն կլաստերին.:

`kubeadm join --token {{token}}`

- Ստեղծեք նոր bootstrap նշան՝ 12 ժամ տևողությամբ TTL.:

`kubeadm token create --ttl {{12h0m0s}}`

- Ստուգեք, արդյոք Kubernetes կլաստերը թարմացվող է, և որ տարբերակներն են հասանելի.:

`kubeadm upgrade plan`

- Թարմացրեք Kubernetes կլաստերը որոշակի տարբերակի.:

`kubeadm upgrade apply {{version}}`

- Դիտեք kubeadm ConfigMap-ը, որը պարունակում է կլաստերի կոնֆիգուրացիան.:

`kubeadm config view`

- Վերադարձեք «kubeadm init»-ի կամ «kubeadm join»-ի միջոցով հոսթին կատարված փոփոխությունները.:

`kubeadm reset`
