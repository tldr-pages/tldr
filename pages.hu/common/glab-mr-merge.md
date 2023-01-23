# glab mr merge

> GitLab egyesítési kérelmek egyesítése. További információ: <https://glab.readthedocs.io/en/latest/mr/merge.html>.

- Az aktuális ághoz tartozó egyesítési kérelem interaktív egyesítése:

`glab mr merge`

- A megadott egyesítési kérelem egyesítése, interaktívan:

`glab mr merge {{mr_number}}`

- Egyesíti az egyesítési kérelmet, eltávolítva az ágat mind a helyi, mind a távoli ágon:

`glab mr merge --remove-source-branch`

- Az aktuális egyesítési kérelem összezsúfolása egy commitba az üzenettörzzsel és az egyesítéssel:

`glab mr merge --squash --message="{{commit_message_body}}"`

- Súgó megjelenítése:

`glab mr merge --help`
