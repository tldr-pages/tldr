#բարի

> Գործարկեք տեղական Kubernetes կլաստերները՝ օգտագործելով Docker կոնտեյների «հանգույցները»:.
> Նախատեսված է հենց Kubernetes-ի փորձարկման համար, բայց կարող է օգտագործվել տեղական զարգացման կամ շարունակական ինտեգրման համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/kubernetes-sigs/kind>:.

- Ստեղծեք տեղական Kubernetes կլաստեր.:

`kind create cluster --name {{cluster_name}}`

- Ջնջել մեկ կամ մի քանի կլաստերներ.:

`kind delete clusters {{cluster_name}}`

- Ստացեք մանրամասներ կլաստերների, հանգույցների կամ kubeconfig-ի մասին.:

`kind get {{clusters|nodes|kubeconfig}}`

- Արտահանեք kubeconfig կամ տեղեկամատյանները.:

`kind export {{kubeconfig|logs}}`
