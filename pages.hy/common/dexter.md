# dexter

> Նույնականացրեք `kubectl` օգտվողներին OpenId Connect-ի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/gini/dexter#run-dexter>:.

- Ստեղծեք և նույնականացրեք օգտատեր Google OIDC-ով.:

`dexter auth {{[-i|--client-id]}} {{client_id}} {{[-s|--client-secret]}} {{client_secret}}`

- Անտեսեք լռելյայն kube կազմաձևման ֆայլի գտնվելու վայրը.:

`dexter auth {{[-i|--client-id]}} {{client_id}} {{[-s|--client-secret]}} {{client_secret}} {{[-k|--kube-config]}} {{sample/config}}`
