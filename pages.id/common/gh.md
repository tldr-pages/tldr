# gh

> Memudahkan pengaksesan GitHub dari command-line.
> Beberapa subcommands seperti `gh config` memiliki dokumentasi sendiri.
> Informasi lebih lanjut: <https://cli.github.com/>.

- Clone sebuah GitHub repository pada local:

`gh repo clone {{owner}}/{{repository}}`

- Membuat issue baru:

`gh issue create`

- Melihat dan filter issue yang sedang open pada repository:

`gh issue list`

- Melihat issue di browser:

`gh issue view --web {{nomor_issue}}`

- Membuat sebuah pull request:

`gh pr create`

- Melihat pull request di browser:

`gh pr view --web {{nomor_pr}}`

- Mengecek pada local branch sebuah pull request, diikuti dengan nomor pull requestnya:

`gh pr checkout {{nomor_pr}}`

- Mengecek status pull request pada sebuah repository:

`gh pr status`
