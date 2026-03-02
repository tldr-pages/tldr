# apptainer delete

> Hapus image kontainer dari library remote.
> Informasi lebih lanjut: <https://apptainer.org/docs/user/main/cli/apptainer_delete.html>.

- Hapus image dari Container Library:

`apptainer delete library://{{user/collection/container}}:{{tag}}`

- Hapus image untuk arsitektur tertentu:

`apptainer delete {{[-A|--arch]}} {{amd64|arm64|ppc64le}} library://{{user/collection/container}}:{{tag}}`

- Hapus paksa image tanpa konfirmasi:

`apptainer delete {{[-F|--force]}} library://{{user/collection/container}}:{{tag}}`

- Hapus image dari server library tertentu:

`apptainer delete --library {{https://library.example.com}} library://{{user/collection/container}}:{{tag}}`

- Hapus image menggunakan HTTP alih-alih HTTPS:

`apptainer delete --no-https library://{{hostname/user/collection/container}}:{{tag}}`

- Tampilkan bantuan:

`apptainer delete {{[-h|--help]}}`
