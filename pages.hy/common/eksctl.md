# eksctl

> Պաշտոնական CLI Amazon EKS-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/eks/latest/eksctl/what-is-eksctl.html>:.

- Ստեղծեք հիմնական կլաստեր.:

`eksctl create cluster`

- Թվարկեք կլաստերի կամ բոլոր կլաստերների մասին մանրամասները.:

`eksctl get cluster --name={{name}} --region={{region}}`

- Ստեղծեք կլաստեր, որը փոխանցում է բոլոր կազմաձևման տեղեկությունները ֆայլում.:

`eksctl create cluster --config-file={{path/to/file}}`

- Ստեղծեք կլաստեր՝ օգտագործելով կազմաձևման ֆայլը և բաց թողեք հանգույցների խմբերի ստեղծումը մինչև ավելի ուշ.:

`eksctl create cluster --config-file={{path/to/file}} --without-nodegroup`

- Ջնջել կլաստերը.:

`eksctl delete cluster --name={{name}} --region={{region}}`

- Ստեղծեք կլաստեր և գրեք կլաստերի հավատարմագրերը լռելյայնից տարբեր ֆայլում.:

`eksctl create cluster --name={{name}} --nodes={{4}} --kubeconfig={{path/to/config.yaml}}`

- Ստեղծեք կլաստեր և կանխեք կլաստերի հավատարմագրերի տեղական պահպանումը.:

`eksctl create cluster --name={{name}} --nodes={{4}} --write-kubeconfig=false`

- Ստեղծեք կլաստեր և թույլ տվեք `eksctl`-ին կառավարել կլաստերի հավատարմագրերը `~/.kube/eksctl/clusters` գրացուցակի տակ:

`eksctl create cluster --name={{name}} --nodes={{4}} --auto-kubeconfig`
