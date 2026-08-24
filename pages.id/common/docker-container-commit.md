# docker container commit

> Buat citra (image) baru atas hasil perubahan isi kontainer.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/container/commit/>.

- Buat citra baru dari suatu kontainer secara spesifik:

`docker {{[commit|container commit]}} {{kontainer}} {{citra}}:{{tag}}`

- Gunakan instruksi Dockerfile `CMD` untuk citra yang sedang dibuat:

`docker {{[commit|container commit]}} {{[-c|--change]}} "CMD {{perintah}}" {{kontainer}} {{citra}}:{{tag}}`

- Gunakan instruksi Dockerfile `ENV` untuk citra yang sedang dibuat:

`docker {{[commit|container commit]}} {{[-c|--change]}} "ENV {{nama_kunci}}={{nilai}}" {{kontainer}} {{citra}}:{{tag}}`

- Buat suatu citra dengan menentukan nama pembuat (author) dalam metadata:

`docker {{[commit|container commit]}} {{[-a|--author]}} "{{nama_pembuat}}" {{kontainer}} {{citra}}:{{tag}}`

- Buat suatu citra dengan menentukan isi pesan komentar dalam metadata:

`docker {{[commit|container commit]}} {{[-m|--message]}} "{{pesan_komentar}}" {{kontainer}} {{citra}}:{{tag}}`

- Buat suatu citra tanpa menjedakan kontainer saat proses komit berlangsung:

`docker {{[commit|container commit]}} {{[-p|--pause]}} false {{kontainer}} {{citra}}:{{tag}}`

- Tampilkan bantuan:

`docker {{[commit|container commit]}} --help`
