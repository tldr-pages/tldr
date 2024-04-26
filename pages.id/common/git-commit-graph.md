# git commit-graph

> Tulis dan verifikasi file grafik komit Git.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-commit-graph>.

- Tulis file grafik komit untuk komit yang dikemas di dalam direktori `.git` pada lokal repositori:

`git commit-graph write`

- Tulis file grafik komit yang berisi semua komit yang dapat dijangkau:

`git show-ref --hash | git commit-graph write --stdin-commits`

- Tulis file grafik komit yang berisi semua komit dalam file grafik komit saat ini beserta yang dapat dijangkau dari `HEAD`:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`
