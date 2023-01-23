# git mergetool

> Futtassa az egyesítési konfliktusok feloldására szolgáló eszközöket az egyesítési konfliktusok feloldásához. További információ: <https://git-scm.com/docs/git-mergetool>.

- Indítsa el az alapértelmezett összevonási eszközt a konfliktusok feloldásához:

`git mergetool`

- Az érvényes egyesítési eszközök listája:

`git mergetool --tool-help`

- A névvel azonosított egyesítési eszköz elindítása:

`git mergetool --tool {{tool_name}}`

- Ne kérdezzen az egyesítési eszköz minden egyes meghívása előtt:

`git mergetool --no-prompt`

- Kifejezetten használja a GUI egyesítési eszközt (lásd a `merge.guitool` config változót):

`git mergetool --gui`

- Kifejezetten a normál egyesítő eszközt használja (lásd a `merge.tool` config változót):

`git mergetool --no-gui`
