#velero

> Կրկնօրինակեք և տեղափոխեք Kubernetes հավելվածները և դրանց մշտական ծավալները:.
> Լրացուցիչ տեղեկություններ. <https://velero.io/docs/main/>:.

- Ստեղծեք կրկնօրինակ, որը պարունակում է բոլոր ռեսուրսները.:

`velero backup create {{backup_name}}`

- Նշեք բոլոր կրկնօրինակները.:

`velero backup get`

- Ջնջել կրկնօրինակը.:

`velero backup delete {{backup_name}}`

- Ստեղծեք շաբաթական կրկնօրինակում, յուրաքանչյուրը ապրում է 90 օր (2160 ժամ).:

`velero schedule create {{schedule_name}} --schedules="{{@every 7d}}" --ttl {{2160h0m0s}}`

- Ստեղծեք վերականգնում վերջին հաջող կրկնօրինակից, որը գործարկվել է հատուկ ժամանակացույցով.:

`velero restore create --from-schedule {{schedule_name}}`
