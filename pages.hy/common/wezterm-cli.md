# wezterm cli

> Շփվեք գործող Wezterm GUI-ի կամ մուլտիպլեքսերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://wezterm.org/cli/cli/index.html>:.

- Ցուցակեք պատուհանները, ներդիրները և վահանակները.:

`wezterm cli list`

- Բաժանեք ընթացիկ վահանակը և տպեք նոր վահանակի ID-ն `stdout`:

`wezterm cli split-pane --{{left|right|top|bottom}} --{{cells|percent}} {{n}}`

- Ակտիվացնել (կենտրոնացնել) մի վահանակ.:

`wezterm cli activate-pane --pane-id {{id}}`

- Սպանել ապակին.:

`wezterm cli kill-pane --pane-id {{id}}`
