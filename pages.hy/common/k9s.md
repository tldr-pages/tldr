# k9s

> Դիտեք և կառավարեք Kubernetes կլաստերները:.
> Լրացուցիչ տեղեկություններ. <https://k9scli.io/topics/commands/>:.

- Կառավարեք կլաստերը՝ օգտագործելով kubeconfig համատեքստը.:

`k9s --context {{kubeconfig_context_name}}`

- Կառավարեք կլաստերը միայն կարդալու ռեժիմում (անջատելով բոլոր հրամանները, որոնք կարող են փոփոխություններ առաջացնել).:

`k9s --readonly --cluster {{cluster_name}}`

- Կառավարեք կլաստերը՝ օգտագործելով տվյալ Kubernetes անվանատարածքը.:

`k9s {{[-n|--namespace]}} {{kubernetes_namespace}} --cluster {{cluster_name}}`

- Կառավարեք կլաստերը, որը գործարկում է k9s-ը pod դիտում և միացրեք վրիպազերծման գրանցումը.:

`k9s {{[-c|--command]}} {{pod}} {{[-l|--logLevel]}} debug --cluster {{cluster_name}}`
