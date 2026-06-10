# kubectl բացահայտել

> Բացահայտեք ռեսուրսը որպես նոր Kubernetes ծառայություն:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_expose/>:.

- Ստեղծեք ծառայություն ռեսուրսի համար, որը կսպասարկի կոնտեյներային նավահանգիստից մինչև հանգույց նավահանգիստ.:

`kubectl expose {{resource_type}} {{resource_name}} --port {{node_port}} --target-port {{container_port}}`

- Ստեղծեք ծառայություն ֆայլով բացահայտված ռեսուրսի համար.:

`kubectl expose {{[-f|--filename]}} {{path/to/file.yml}} --port {{node_port}} --target-port {{container_port}}`

- Ստեղծեք ծառայություն անունով, որը կծառայի հանգույցի պորտին, որը նույնը կլինի կոնտեյներային պորտի համար.:

`kubectl expose {{resource_type}} {{resource_name}} --port {{node_port}} --name {{service_name}}`
