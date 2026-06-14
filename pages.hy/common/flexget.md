# flexget

> Բազմաֆունկցիոնալ ավտոմատացման գործիք բովանդակության համար, ինչպիսիք են torrents, nzbs, podcasts, comics, շարքեր, ֆիլմեր և այլն:.
> Լրացուցիչ տեղեկություններ. <https://flexget.com/en/CLI>:.

- Գործարկեք Flexget-ի բոլոր առաջադրանքները հիմա.:

`flexget execute --now`

- Սկսեք Flexget դեյմոնը և դևոնացրեք դրա գործընթացը.:

`flexget daemon start --daemonize`

- Թվարկեք Flexget-ում գրանցված բոլոր սերիաները.:

`flexget series list`

- Գործարկել առաջադրանք կազմաձևման ֆայլից.:

`flexget -c {{path/to/config.yml}} execute --task {{task_name}}`
