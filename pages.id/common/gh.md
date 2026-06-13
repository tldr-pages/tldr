# gh

> Memudahkan pengaksesan GitHub dari command-line.
> Beberapa subcommands seperti `gh config` memiliki dokumentasi sendiri.
> Informasi lebih lanjut: <https://cli.github.com/manual/gh>.

- Mengklon sebuah GitHub repositori di lokal:

`gh repo clone {{pemilik}}/{{repositori}}`

- Membuat isu baru:

`gh issue {{[new|create]}}`

- Melihat dan filter issue yang sedang open pada repositori:

`gh issue {{[ls|list]}}`

- Melihat isu di browser:

`gh issue view {{[-w|--web]}} {{nomor_isu}}`

- Membuat sebuah pull request:

`gh pr {{[new|create]}}`

- Melihat pull request di browser:

`gh pr view {{[-w|--web]}} {{nomor_pr}}`

- Mengecek pada local branch sebuah pull request, diikuti dengan nomor pull requestnya:

`gh {{[co|pr checkout]}} {{nomor_pr}}`

- Mengecek status pull request pada sebuah repository:

`gh pr status`
