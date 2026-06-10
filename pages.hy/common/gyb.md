# գիբ

> Տեղականորեն կրկնօրինակեք Gmail հաղորդագրությունները՝ օգտագործելով Gmail-ի API-ը HTTPS-ի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/GAM-team/got-your-back>:.

- Գնահատեք ձեր Gmail հաշվի բոլոր նամակների քանակը և չափը.:

`gyb --email {{email@gmail.com}} --action estimate`

- Կրկնօրինակեք Gmail հաշիվը որոշակի գրացուցակում.:

`gyb --email {{email@gmail.com}} --action backup --local-folder {{path/to/directory}}`

- Կրկնօրինակեք միայն կարևոր կամ աստղանշված նամակները Gmail-ի հաշվից կանխադրված տեղական թղթապանակում.:

`gyb --email {{email@gmail.com}} --search "{{is:important OR is:starred}}"`

- Վերականգնել տեղական թղթապանակից Gmail հաշիվ.:

`gyb --email {{email@gmail.com}} --action restore --local-folder {{path/to/directory}}`
