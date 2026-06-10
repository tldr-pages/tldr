# kubectl վստահված անձ

> Ստեղծեք պրոքսի սերվեր կամ հավելվածի մակարդակի դարպաս՝ localhost-ի և Kubernetes API սերվերի միջև:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_proxy/>:.

- Գործարկեք վստահված անձ՝ օգտագործելով լռելյայն կարգավորումները 8001 նավահանգստում և լսեք localhost-ում.:

`kubectl proxy`

- Kubernetes API-ի վստահված անձը տեղական գրացուցակից ստատիկ ֆայլեր սպասարկելիս.:

`kubectl proxy {{[-w|--www]}} {{path/to/static_dir}} {{[-P|--www-prefix]}} {{/static_prefix/}} --api-prefix {{/api_subset/}}`

- Ամբողջ Kubernetes API-ի վստահված անձը հատուկ նախածանցով.:

`kubectl proxy --api-prefix {{/custom_prefix/}}`

- Ծառայել Kubernetes API-ն կոնկրետ նավահանգստում, միաժամանակ սպասարկելով ստատիկ բովանդակություն.:

`kubectl proxy {{[-p|--port]}} {{port}} {{[-w|--www]}} {{path/to/static_dir}}`

- Գործարկեք վստահված անձ պատահական տեղական պորտի վրա՝ տպելով ընտրված նավահանգիստը `stdout`:

`kubectl proxy {{[-p|--port]}} 0`

- Գործարկեք վստահված անձը Unix տիրույթի վարդակից TCP պորտի փոխարեն.:

`kubectl proxy {{[-u|--unix-socket]}} {{path/to/socket}}`

- Ընդունեք կապեր հեռավոր հոսթներից՝ լսելով բոլոր ինտերֆեյսները (զգույշ եղեք վստահված անձին հրապարակայնորեն բացահայտելիս).:

`kubectl proxy --address 0.0.0.0 --accept-hosts '.*'`

- Թույլատրել միայն ընտրված API ուղիները՝ մերժելով զգայուն վերջնակետերը.:

`kubectl proxy --accept-paths '^/api/v1/namespaces/default/.*' --reject-paths '^/api/.*/pods/.*/exec'`
