# kubectl վազում

> Գործարկել pods Kubernetes-ում:.
> Հատկորոշում է pod գեներատորը՝ K8S-ի որոշ տարբերակներում հնացման սխալից խուսափելու համար:.
> Լրացուցիչ տեղեկություններ. <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_run/>:.

- Գործարկեք `nginx` pod և բացահայտեք 80-րդ նավահանգիստը՝:

`kubectl run {{nginx-dev}} --image nginx --port 80`

- Գործարկեք `nginx` pod՝ սահմանելով `$TEST_VAR` միջավայրի փոփոխականը՝:

`kubectl run {{nginx-dev}} --image nginx --env "{{TEST_VAR}}={{testing}}"`

- Ցույց տալ API զանգերը, որոնք կկատարվեն `nginx` կոնտեյներ ստեղծելու համար.:

`kubectl run {{nginx-dev}} --image nginx --dry-run={{none|server|client}}`

- Գործարկեք Ubuntu pod-ը ինտերակտիվ կերպով, երբեք մի վերագործարկեք այն և հեռացրեք այն, երբ այն դուրս է գալիս:

`kubectl run {{temp-ubuntu}} --image ubuntu:22.04 --restart Never --rm -- /bin/bash`

- Գործարկեք Ubuntu pod՝ վերացնելով լռելյայն հրամանը echo-ով և նշելով հատուկ արգումենտներ.:

`kubectl run {{temp-ubuntu}} --image ubuntu:22.04 --command -- echo {{argument1 argument2 ...}}`
