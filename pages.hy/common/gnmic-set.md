# gnmic հավաքածու

> Փոփոխել gnmi ցանցի սարքի կոնֆիգուրացիան:.
> Լրացուցիչ տեղեկություններ. <https://gnmic.openconfig.net/cmd/set/>:.

- Թարմացրեք ուղու արժեքը.:

`gnmic {{[-a|--address]}} {{ip:port}} set --update-path {{path/to/directory}} --update-value {{value}}`

- Թարմացրեք ուղու արժեքը՝ JSON ֆայլի բովանդակությանը համապատասխանելու համար.:

`gnmic {{[-a|--address]}} {{ip:port}} set --update-path {{path/to/directory}} --update-file {{path/to/file}}`

- Փոխարինեք ուղու արժեքը JSON ֆայլի բովանդակությանը համապատասխանելու համար.:

`gnmic {{[-a|--address]}} {{ip:port}} set --replace-path {{path/to/directory}} --replace-file {{path/to/file}}`

- Ջնջել հանգույցը տվյալ ուղու վրա.:

`gnmic {{[-a|--address]}} {{ip:port}} set --delete {{path/to/directory}}`
