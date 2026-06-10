# swaylock

> Էկրանի կողպման ծրագիր Wayland կոմպոզիտորների համար:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/swaylock>:.

- Կողպեք էկրանը՝ օգտագործելով `$HOME/.swaylock/config` կամ `$XDG_CONFIG_HOME/swaylock/config` կոնֆիգուրսը:

`swaylock`

- Կողպեք էկրանը պարզ գունային ֆոնով (`rrggbb` ձևաչափ).:

`swaylock {{[-c|--color]}} {{0000ff}}`

- Կողպեք էկրանը ֆոնային պատկերով.:

`swaylock {{[-i|--image]}} {{path/to/image}}`

- Կողպեք էկրանը և անջատեք ապակողպման ցուցիչը (հեռացնում է հետադարձ կապը ստեղնաշարի վրա).:

`swaylock {{[-u|--no-unlock-indicator]}}`

- Կողպելուց հետո անջատեք հսկիչ տերմինալից (ինչպես `i3lock`):

`swaylock {{[-f|--daemonize]}}`

- Կողպեք էկրանը բոլոր մոնիտորների վրա սալիկապատված ֆոնային պատկերով.:

`swaylock {{[-i|--image]}} {{path/to/image}} {{[-t|--tiling]}}`

- Կողպեք էկրանը և ցույց տվեք մուտքի անհաջող փորձերի քանակը.:

`swaylock {{[-F|--show-failed-attempts]}}`

- Բեռնել կոնֆիգուրացիան որոշակի ֆայլից.:

`swaylock {{[-C|--config]}} {{path/to/config}}`
