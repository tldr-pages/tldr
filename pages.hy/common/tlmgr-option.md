# tlmgr տարբերակ

> TeX Live կարգավորումների կառավարիչ:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#option>:.

- Թվարկեք TeX Live-ի բոլոր կարգավորումները.:

`tlmgr option showall`

- Թվարկեք բոլոր ներկայումս սահմանված Tex Live կարգավորումները.:

`tlmgr option show`

- Տպեք TeX Live-ի բոլոր կարգավորումները JSON ձևաչափով.:

`tlmgr option showall --json`

- Ցույց տալ հատուկ TeX Live պարամետրի արժեքը.:

`tlmgr option {{setting}}`

- Փոփոխեք հատուկ TeX Live պարամետրի արժեքը.:

`tlmgr option {{setting}} {{value}}`

- Նախադրեք TeX Live-ը՝ DVD-ից տեղադրելուց հետո ինտերնետից ապագա թարմացումներ ստանալու համար.:

`tlmgr option {{repository}} {{https://mirror.ctan.org/systems/texlive/tlnet}}`
