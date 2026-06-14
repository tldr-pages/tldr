# bun patch

> Պատրաստեք փաթեթ կարկատելու համար կամ ստեղծեք կարկատել ֆայլ:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/pm/cli/patch>:.

- Պատրաստեք փաթեթ կարկատելու համար.:

`bun patch {{package}}`

- Պատրաստեք փաթեթի հատուկ տարբերակ.:

`bun patch {{package}}@{{version}}`

- Պատրաստեք փաթեթ, որը գտնվում է որոշակի ուղու վրա.:

`bun patch {{path/to/package}}`

- Ստեղծեք կարկատել ֆայլ փաթեթում կատարված փոփոխությունների համար.:

`bun patch --commit {{path/to/package}}`

- Ստեղծեք կարկատել ֆայլ և պահեք այն հատուկ գրացուցակում.:

`bun patch --commit {{path/to/package}} --patches-dir {{path/to/directory}}`
