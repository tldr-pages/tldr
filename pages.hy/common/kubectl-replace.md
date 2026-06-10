# kubectl փոխարինել

> Փոխարինեք ռեսուրսը ֆայլով կամ `stdin`:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_replace/>:.

- Փոխարինեք ռեսուրսը, օգտագործելով ռեսուրսի սահմանման ֆայլը.:

`kubectl replace {{[-f|--filename]}} {{path/to/file.yml}}`

- Փոխարինեք ռեսուրսը, օգտագործելով `stdin` մուտքագրումը.:

`kubectl replace {{[-f|--filename]}} -`

- Ստիպեք փոխարինել, ջնջել և այնուհետև նորից ստեղծել ռեսուրսը.:

`kubectl replace {{[-f|--filename]}} {{path/to/file.yml}} --force`
