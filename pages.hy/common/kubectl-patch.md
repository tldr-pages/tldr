# kubectl կարկատել

> Կարկատել Kubernetes-ի ռեսուրսները նոր արժեքներով:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_patch/>:.

- Մասամբ կարկատեք գաղտնիքը՝ օգտագործելով ռազմավարական միաձուլման JSON պատչը՝ վերջնականացուցիչը հեռացնելու համար.:

`kubectl patch secrets {{secret_name}} {{[-p|--patch]}} '{"metadata":{"finalizers": []\}\}' --type merge`

- Մասամբ կարկատեք գաղտնիքը՝ օգտագործելով ռազմավարական միաձուլման YAML կարկատը՝ վերջնականացուցիչը հեռացնելու համար.:

`kubectl patch secrets {{secret_name}} {{[-p|--patch]}} $'metadata:\n finalizers: []' --type merge`

- Մասամբ կարկատել pod-ի կոնտեյները՝ օգտագործելով JSON կարկատել դիրքային զանգվածներով.:

`kubectl patch {{[po|pods]}} {{pod_name}} --type 'json' {{[-p|--patch]}} '[{"op": "replace", "path": "/spec/containers/0/image", "value":"{{new_image_value}}"}]'`

- Թարմացրեք տեղակայման կրկնօրինակները մասշտաբի ենթառեսուրսի միջոցով՝ օգտագործելով ռազմավարական միաձուլման JSON կարկատելը.:

`kubectl patch {{[deploy|deployments]}} {{deployment_name}} --subresource 'scale' --type 'merge' {{[-p|--patch]}} '{"spec":{"replicas":{{number_of_replicas}}\}\}'`
