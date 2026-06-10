# համաժամացում

> Շարունակական երկկողմանի ապակենտրոնացված թղթապանակների համաժամացման գործիք:.
> Լրացուցիչ տեղեկություններ. <https://docs.syncthing.net/users/syncthing.html>:.

- Սկսել համաժամացումը.:

`syncthing`

- Սկսեք համաժամացումը առանց վեբ զննարկիչ բացելու.:

`syncthing --no-browser`

- Փոխեք տնային գրացուցակը.:

`syncthing --home {{path/to/directory}}`

- Գործարկել Syncthing-ը ավելացված գրանցամատյանով.:

`syncthing --verbose`

- Դադարեցնել բոլոր սարքերը.:

`syncthing cli config devices pause --all`

- Վերսկսել բոլոր սարքերը.:

`syncthing cli config devices resume --all`

- Փոխեք հասցեն, որի վրա լսվում է վեբ ինտերֆեյսը.:

`syncthing --gui-address {{ip_address:port|path/to/socket.sock}}`

- Սահմանեք ելքի մատյան մակարդակը.:

`syncthing --log-level {{info|warning|error|debug}}`
