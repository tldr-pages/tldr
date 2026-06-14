# chainctl

> Պաշտոնական CLI-ն Chainguard-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://edu.chainguard.dev/chainguard/chainctl/chainctl-docs/chainctl/>:.

- Նույնականացում Chainguard հարթակում.:

`chainctl auth login`

- Դուրս գալ Chainguard հարթակից.:

`chainctl auth logout`

- Թարմացրեք վերջին տարբերակին.:

`chainctl update`

- Թվարկեք ձեր հաշվին հասանելի պատկերները.:

`chainctl images list`

- Թվարկեք ձեր հաշվին հասանելի պատկերների պահոցները.:

`chainctl images repos list`

- Ուսումնասիրեք պատկերի պիտակի պատմությունը chainctl-ում (օրինակ՝ image=python tag=3):

`chainctl images history {{image}}:{{tag}}`

- Ցուցակեք փաթեթի տարբերակի տվյալները ձեր հաշվին հասանելի պահոցներից (օրինակ՝ փաթեթի անունը=գնա):

`chainctl packages versions list {{package_name}}`

- Ցուցադրման տարբերակը:

`chainctl version`
