# kubectl սանդղակ

> Սահմանեք նոր չափ՝ տեղակայման, կրկնօրինակների հավաքածուի, վերարտադրման վերահսկիչի կամ վիճակագրական հավաքածուի համար:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_scale/>:.

- Սանդղակավորեք կրկնօրինակների հավաքածուն.:

`kubectl scale --replicas {{replicas_count}} rs/{{replica_name}}`

- Սանդղակավորեք ֆայլով հայտնաբերված ռեսուրսը.:

`kubectl scale --replicas {{replicas_count}} {{[-f|--filename]}} {{path/to/file.yml}}`

- Սանդղակավորեք տեղակայումը` հիմնված կրկնօրինակների ընթացիկ քանակի վրա.:

`kubectl scale --replicas {{replicas_count}} --current-replicas {{current_replicas}} {{[deploy|deployment]}}/{{deployment_name}}`
