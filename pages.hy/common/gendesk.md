# gendesk

> Նշեք հրամանը՝ `.desktop` ֆայլ և նվազագույն տեղեկություններով ներբեռնման պատկերակ ստեղծելու համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/gendesk>:.

- Ստեղծեք `.desktop` ֆայլ `app` անունով:

`gendesk -n --name "{{app}}" --exec "/{{path/to/app}}" --icon "/{{path/to/icon.png}}" --comment "{{This is application}}"`

- Ստեղծեք `.desktop` ֆայլ՝ `app` անունով, մի ցուցադրեք որևէ ելք և վերագրեք այն, եթե այն կա.:

`gendesk -q -f -n --name "{{app}}" --exec "/{{path/to/app}}" --icon "/{{path/to/icon.png}}" --comment "{{This is application}}"`

- Ցուցադրել օգնությունը.:

`gendesk {{[-h|--help]}}`
