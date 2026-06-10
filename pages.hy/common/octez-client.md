# octez-հաճախորդ

> Փոխազդեք Tezos բլոկչեյնի հետ:.
> Լրացուցիչ տեղեկություններ. <https://tezos.gitlab.io/introduction/howtouse.html#client>:.

- Կարգավորեք հաճախորդը Tezos RPC հանգույցի հետ կապով, ինչպիսին է <https://rpc.ghostnet.teztnets.com>:

`octez-client -E {{endpoint}} config update`

- Ստեղծեք հաշիվ և դրան նշանակեք տեղական կեղծանուն.:

`octez-client gen keys {{alias}}`

- Ստացեք հաշվի մնացորդը կեղծանունով կամ հասցեով.:

`octez-client get balance for {{alias_or_address}}`

- Փոխանցել tez-ը մեկ այլ հաշվի վրա.:

`octez-client transfer {{5}} from {{alias|address}} to {{alias|address}}`

- Ստեղծեք (տեղակայեք) խելացի պայմանագիր, նշանակեք այն տեղական անուն և սահմանեք դրա նախնական պահեստը որպես Michelson-ի կոդավորված արժեք.:

`octez-client originate contract {{alias}} transferring {{0}} from {{alias|address}} running {{path/to/source_file.tz}} --init "{{initial_storage}}" --burn_cap {{1}}`

- Զանգահարեք խելացի պայմանագիր իր կեղծանունով կամ հասցեով և փոխանցեք Michelson-ի կոդավորված պարամետրը.:

`octez-client transfer {{0}} from {{alias|address}} to {{contract}} --entrypoint "{{entrypoint}}" --arg "{{parameter}}" --burn-cap {{1}}`

- Ցուցադրել օգնությունը.:

`octez-client man`
