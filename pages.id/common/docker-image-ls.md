# docker image ls

> Tampilkan daftar citra Docker.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Tampilkan daftar seluruh citra Docker yang terpasang:

`docker {{[images|image ls]}}`

- Tampilkan daftar seluruh citra Docker termasuk citra-citra perantara (intermediates):

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Tampilkan daftar dalam mode sunyi (hanya tampilkan nomor induk setiap citra):

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Tampilkan daftar seluruh citra Docker yang tidak dipakai dalam kontainer apapun:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- Tampilkan daftar kumpulan citra yang memiliki nama dengan pola nama tertentu:

`docker {{[images|image ls]}} "{{*nama*}}"`

- Urutkan daftar citra berdasarkan ukurannya:

`docker {{[images|image ls]}} --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
