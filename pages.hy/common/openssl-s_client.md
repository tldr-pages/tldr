# openssl s_client

> Ստեղծեք TLS հաճախորդի կապեր:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl-s_client/>:.

- Ցուցադրել տիրույթի վկայագրի մեկնարկի և ժամկետի ավարտի ժամկետները.:

`openssl s_client -connect {{host}}:{{port}} 2>/dev/null | openssl x509 -noout -dates`

- Ցուցադրել SSL/TLS սերվերի կողմից ներկայացված վկայագիրը.:

`openssl < /dev/null s_client -connect {{host}}:{{port}}`

- Սահմանեք սերվերի անվան ցուցիչը (SNI) SSL/TLS սերվերին միանալիս.:

`openssl s_client -connect {{host}}:{{port}} -servername {{hostname}}`

- Ցուցադրել HTTPS սերվերի ամբողջական վկայականի շղթան.:

`openssl < /dev/null s_client -connect {{host}}:443 -showcerts`
