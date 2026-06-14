# VBoxManage ամպ

> VirtualBox հրամանի տող ինտերֆեյս՝ ամպային օրինակների և պատկերների կառավարման համար:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-cloud>:.

- Թվարկե՛ք նշված վիճակում գտնվող դեպքերը, որոնք պատկանում են նշված բաժինին.:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list instances --state={{running|terminated|paused}} --compartment-id={{compartment_id}}`

- Ստեղծեք նոր օրինակ.:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance create --domain-name={{domain_name}} --image-id={{image_id}}`

- Հավաքեք տեղեկատվություն որոշակի օրինակի մասին.:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance info --id={{unique_id}}`

- Դադարեցնել օրինակը.:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} instance terminate --id={{unique_id}}`

- Թվարկեք պատկերները որոշակի խցիկում և նշեք.:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} list images --compartment-id={{compartment_id}} --state={{state_name}}`

- Ստեղծեք նոր պատկեր.:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image create --instance-id={{instance_id}} --display-name={{display_name}} --compartment-id={{compartment_id}}`

- Առբերեք տեղեկատվություն որոշակի պատկերի մասին.:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image info --id={{unique_id}}`

- Ջնջել պատկերը.:

`VBoxManage cloud --provider={{provider_name}} --profile={{profile_name}} image delete --id={{unique_id}}`
