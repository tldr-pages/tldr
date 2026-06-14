# bun ստեղծել

> Ստեղծեք նոր նախագիծ կաղապարից:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/runtime/templating/create>:.

- Ստեղծեք նոր նախագիծ պաշտոնական ձևանմուշից ինտերակտիվ կերպով.:

`bun {{[c|create]}} {{template}}`

- Ստեղծեք նոր նախագիծ պաշտոնական ձևանմուշից նոր գրացուցակում.:

`bun {{[c|create]}} {{template}} {{path/to/destination}}`

- Ստեղծեք նոր նախագիծ GitHub պահեստի ձևանմուշից.:

`bun {{[c|create]}} {{https://github.com/username/repo}} {{path/to/destination}}`

- Ստեղծեք նոր նախագիծ տեղական ձևանմուշից.:

`bun {{[c|create]}} {{path/to/template}} {{path/to/destination}}`

- Ստեղծեք նոր նախագիծ՝ վերագրանցելով նպատակակետի գրացուցակը, եթե այն գոյություն ունի.:

`bun {{[c|create]}} {{template}} {{path/to/destination}} --force`

- Ստեղծեք նոր նախագիծ՝ առանց Git պահեստի ինքնաբերաբար սկզբնավորման.:

`bun {{[c|create]}} {{template}} {{path/to/destination}} --no-git`

- Ստեղծեք նոր նախագիծ՝ առանց ավտոմատ կերպով կախվածություն տեղադրելու.:

`bun {{[c|create]}} {{template}} {{path/to/destination}} --no-install`
