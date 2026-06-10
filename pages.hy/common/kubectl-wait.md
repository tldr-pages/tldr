# kubectl սպասիր

> Սպասեք, որ ռեսուրս(ներ)ը հասնեն որոշակի վիճակի:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_wait/>:.

- Սպասեք տեղակայման հասանելիությանը.:

`kubectl wait --for condition=available deployment/{{deployment_name}}`

- Սպասեք, որ բոլոր պատյանները որոշակի [l] պիտակով պատրաստ լինեն.:

`kubectl wait --for condition=ready {{[po|pods]}} {{[-l|--selector]}} {{label_key}}={{label_value}}`

- Սպասեք, որ պատիճը ջնջվի.:

`kubectl wait --for delete {{[po|pods]}} {{pod_name}}`

- Սպասեք աշխատանքի ավարտին 120 վայրկյանի ընթացքում (եթե պայմանը ժամանակին չկատարվի, ելքի կարգավիճակն անհաջող կլինի).:

`kubectl wait --for condition=complete job/{{job_name}} --timeout 120s`
