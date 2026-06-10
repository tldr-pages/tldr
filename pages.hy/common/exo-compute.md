# exo հաշվարկ

> Կառավարեք Exoscale Compute ռեսուրսները:.
> Որոշ ենթահրամաններ, ինչպիսիք են `instance`-ն, ունեն իրենց սեփական փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://community.exoscale.com/product/>:.

- Արագ ստեղծեք Exoscale Compute ռեսուրս (օրինակ, Անվտանգության խումբ, SKS կլաստեր,...):

`exo compute {{resource_type}} create {{resource_name}}`

- Թվարկեք Exoscale Compute օրինակների տեսակները.:

`exo compute instance-type list`

- Գրանցեք նոր SSH բանալի, որը կարող է օգտագործվել Հաշվարկային օրինակներ մուտք գործելու համար.:

`exo compute ssh-key register {{key_name}} {{public_key_file}}`

- Ստեղծեք հաշվարկային օրինակ՝ դրա վրա տեղադրված ssh ստեղնով.:

`exo compute instance create {{instance_name}} {{ssh_key_name}}`

- Գրանցեք նոր Հաշվարկային օրինակի ձևանմուշ՝ հիմնված Հաշվողական օրինակի պատկերի վրա (օգտակար է, երբ ցանկանում եք արագ ստեղծել Հաշվողական օրինակի կրկնօրինակը).:

`exo compute instance template register {{template_name}} --from-snapshot {{snapshot_id}}`

- Ավելացրեք նոր կանոն գոյություն ունեցող անվտանգության խմբին.:

`exo compute security-group rule add {{security_group_name|id}} --description '{{Allow SSH access}}' --flow {{ingress}} --port {{22}} --network {{0.0.0.0/0}}`

- Կառավարեք գոյություն ունեցող ցանցի բեռնվածության հաշվեկշռի ծառայությունները.:

`exo compute load-balancer service add {{load_balancer_name|id}} {{service_name}} --port {{service_port}}`
