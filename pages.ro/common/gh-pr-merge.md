# gh pr merge

> Îmbinare cereri de extragere GitHub.
> Mai multe informaţii: <https://cli.github.com/manual/gh_pr_merge>

- Îmbinați solicitarea de tragere asociată sucursalei curente interactiv:

`gh pr merge`

- Îmbinați solicitarea de tragere specificată, interactiv:

`gh pr merge {{pr_number}}`

- Mergeți cererea de tragere, eliminând ramura atât pe cea locală, cât și pe telecomandă:

`gh pr merge --delete-branch`

- Îmbinați solicitarea curentă de tragere cu strategia de îmbinare specificată:

`gh pr merge --{{merge|squash|rebase}}`

- Squash cererea de tragere curentă într-o singură comite cu corpul mesajului și îmbinare:

`gh pr merge --squash --body="{{commit_message_body}}"`

- Ajutor pentru afișare:

`gh pr merge --help`
