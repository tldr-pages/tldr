# ykman openpgp

> Կառավարեք OpenPGP YubiKey հավելվածը:.
> Նշում. որոշ կարգավորումների համար անհրաժեշտ է օգտագործել `gpg --card-edit`:.
> Լրացուցիչ տեղեկություններ. <https://docs.yubico.com/software/yubikey/tools/ykman/OpenPGP_Commands.html>:.

- Ցուցադրել ընդհանուր տեղեկություններ OpenPGP հավելվածի մասին.:

`ykman openpgp info`

- Սահմանեք համապատասխանաբար օգտագործողի PIN-ի, վերակայման կոդի և ադմինիստրատորի PIN-ի կրկնակի փորձերի քանակը.:

`ykman openpgp access set-retries {{3}} {{3}} {{3}}`

- Փոխեք օգտվողի PIN-ը, վերակայման կոդը կամ ադմինիստրատորի PIN-ը.:

`ykman openpgp access change-{{pin|reset-code|admin-pin}}`

- Վերագործարկեք OpenPGP հավելվածը գործարանային պարամետրերով (դա պետք է անեք Admin PIN-ի կրկնակի փորձերի քանակը գերազանցելուց հետո).:

`ykman openpgp reset`
