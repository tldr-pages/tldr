# zeroclaw գործակալ

> Սկսեք AI գործակալի հանգույցը ZeroClaw-ի հետ փոխգործակցության համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/zeroclaw-labs/zeroclaw#quick-start>:.

- Ուղարկեք մեկ հաղորդագրություն AI գործակալին.:

`zeroclaw agent {{[-m|--message]}} "{{Hello, ZeroClaw!}}"`

- Սկսեք ինտերակտիվ զրույցի ռեժիմը.:

`zeroclaw agent`

- Ուղարկեք հաղորդագրություն կոնկրետ մատակարարի հետ.:

`zeroclaw agent {{[-m|--message]}} "{{Hello}}" {{[-p|--provider]}} {{anthropic}}`

- Ուղարկեք հաղորդագրություն կոնկրետ մոդելով.:

`zeroclaw agent {{[-m|--message]}} "{{Hello}}" --model {{anthropic/claude-sonnet-4-20250514}}`

- Ուղարկեք հաղորդագրություն հատուկ ջերմաստիճանով.:

`zeroclaw agent {{[-m|--message]}} "{{Hello}}" {{[-t|--temperature]}} {{0.5}}`

- Ուղարկեք հաղորդագրություն և կցեք ապարատային ծայրամասային սարք.:

`zeroclaw agent {{[-m|--message]}} "{{Hello}}" --peripheral {{nucleo-f401re:/dev/ttyACM0}}`

- Ցուցադրել օգնությունը.:

`zeroclaw agent {{[-h|--help]}}`
