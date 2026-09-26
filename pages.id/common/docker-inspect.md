# docker inspect

> Dapatkan informasi objek-objek Docker secara terperinci.
> Informasi lebih lanjut: <https://docs.docker.com/reference/cli/docker/inspect/>.

- Tampilkan informasi suatu kontainer, citra (image), atau volume menggunakan nama atau ID tertentu:

`docker inspect {{kontainer|citra|id}}`

- Tampilkan alamat IP suatu kontainer:

`docker inspect {{[-f|--format]}} '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{kontainer}}`

- Tampilkan alamat berkas log untuk suatu kontainer:

`docker inspect {{[-f|--format]}} '\{\{.LogPath\}\}' {{kontainer}}`

- Tampilkan nama citra yang dipakai dalam suatu kontainer:

`docker inspect {{[-f|--format]}} '\{\{.Config.Image\}\}' {{kontainer}}`

- Tampilkan informasi konfigurasi dalam format JSON:

`docker inspect {{[-f|--format]}} '\{\{json .Config\}\}' {{kontainer}}`

- Tampilkan daftar port yang ditautkan dari sistem host menuju port internal suatu kontainer:

`docker inspect {{[-f|--format]}} '\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{kontainer}}`

- Tampilkan bantuan:

`docker inspect`
