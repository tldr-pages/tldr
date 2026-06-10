#բաց ճանկ

> Անձնական AI օգնական, որը դուք աշխատում եք ձեր սեփական սարքերով:.
> Որոշ ենթահրամաններ, ինչպիսիք են `onboard`, `agent`, `doctor` և այլն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Տես նաև՝ `zeroclaw`:.
> Լրացուցիչ տեղեկություններ. <https://docs.openclaw.ai/cli>:.

- Գործարկեք միացման հրաշագործը՝ դարպասը և ալիքները կարգավորելու համար.:

`openclaw onboard --install-daemon`

- Գործարկեք gateway սերվերը.:

`openclaw gateway --allow-unconfigured --port {{18789}} --verbose`

- Ուղարկեք հաղորդագրություն կոնտակտին.:

`openclaw message send {{[-t|--target]}} {{+1234567890}} {{[-m|--message]}} "{{Hello}}"`

- Խոսեք օգնականի հետ մեկ հաղորդագրությամբ.:

`openclaw agent {{[-m|--message]}} "{{Ship checklist}}"`

- Սկսեք ինտերակտիվ զրույցի ռեժիմը.:

`openclaw agent`

- Գործարկեք ախտորոշում և ստուգեք համակարգի առողջությունը.:

`openclaw doctor`

- Թարմացրեք OpenClaw-ը վերջին տարբերակին.:

`openclaw update`

- Նշեք կազմաձևված ալիքները.:

`openclaw channels list`
