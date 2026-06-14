# swaymsg

> Ուղարկեք հաղորդագրություններ Sway-ի գործող օրինակին՝ օգտագործելով IPC:.
> Հասանելի հրամանների համար տես <https://github.com/swaywm/sway/blob/master/sway/sway.5.scd>:.
> Լրացուցիչ տեղեկություններ. <https://github.com/swaywm/sway/blob/master/swaymsg/swaymsg.1.scd>:.

- Գործարկել Sway հրամանը.:

`swaymsg {{command}}`

- Ցուցադրել աշխատանքային տարածքների ցանկը.:

`swaymsg {{[-t|--type]}} get_workspaces`

- Ցուցադրել մուտքային սարքերի ցանկը.:

`swaymsg {{[-t|--type]}} get_inputs`

- Ցուցադրել ելքային սարքերի ցանկը.:

`swaymsg {{[-t|--type]}} get_outputs`

- Ցուցադրել բոլոր բաց պատուհանների, բեռնարկղերի, ելքերի և աշխատանքային տարածքների դասավորության ծառը.:

`swaymsg {{[-t|--type]}} get_tree`
