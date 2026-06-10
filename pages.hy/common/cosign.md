# նշան

> Բեռնարկղերի ստորագրում, ստուգում և պահպանում OCI գրանցամատյանում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sigstore/cosign/blob/main/doc/cosign.md>:.

- Ստեղծեք բանալիների զույգ.:

`cosign generate-key-pair`

- Ստորագրեք կոնտեյներ և պահեք ստորագրությունը գրանցամատյանում.:

`cosign sign --key {{cosign.key}} {{image}}`

- Ստորագրեք կոնտեյների պատկերը Kubernetes գաղտնիքում պահվող բանալիների զույգով.:

`cosign sign --key k8s://{{namespace}}/{{key}} {{image}}`

- Ստորագրեք բշտիկ տեղական բանալիների զույգ ֆայլով.:

`cosign sign-blob --key {{cosign.key}} {{path/to/file}}`

- Ստուգեք կոնտեյները հանրային բանալիով.:

`cosign verify --key {{cosign.pub}} {{image}}`

- Ստուգեք պատկերները հանրային բանալիով Dockerfile-ում.:

`cosign dockerfile verify -key {{cosign.pub}} {{path/to/Dockerfile}}`

- Ստուգեք պատկերը Kubernetes գաղտնիքում պահվող հանրային բանալիով.:

`cosign verify --key k8s://{{namespace}}/{{key}} {{image}}`

- Պատճենել կոնտեյների պատկերը և դրա ստորագրությունները.:

`cosign copy {{example.com/src:latest}} {{example.com/dest:latest}}`
