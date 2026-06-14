# pkcs11-գործիք

> Կոմունալ PKCS #11 անվտանգության նշանները կառավարելու և օգտագործելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/OpenSC/OpenSC/wiki/Using-pkcs11-tool-and-OpenSSL>:.

- Ցուցակեք սլոտները և դրանց պոտենցիալ նշանը՝ օգտագործելով հատուկ մոդուլ (օրինակ՝ `/usr/lib/softhsm/libsofthsm2.so`):

`pkcs11-tool --module {{path/to/module.so}} {{[-L|--list-slots]}} {{[-T|--list-token-slots]}}`

- Թվարկեք օբյեկտները կոնկրետ բնիկում: (Նշում. `slot_id`-ը բնիկի ինդեքսը չէ, որը ցուցադրվում է որպես «Slot X»):

`pkcs11-tool {{[-O|--list-objects]}} {{[-p|--pin]}} {{auth_pin}} --slot {{slot_id}}`

- Ստեղծեք նոր օբյեկտ հատուկ պիտակով և մուտքագրեք.:

`pkcs11-tool --slot {{slot_id}} {{[-p|--pin]}} {{auth_pin}} {{[-y|--type]}} {{cert|privkey|pubkey|secrkey|data|...}} {{[-a|--label]}} "{{label}}" {{[-d|--id]}} {{01}} {{[-w|--write-object]}} {{path/to/cert.crt}}`

- Ջնջել օբյեկտն ըստ իր պիտակի և տեսակի.:

`pkcs11-tool --slot {{slot_id}} {{[-p|--pin]}} {{auth_pin}} {{[-y|--type]}} {{cert|privkey|pubkey|secrkey|data|...}} {{[-a|--label]}} "{{label}}" {{[-b|--delete-object]}}`
