# addcomputer.py

> Tambahkan akun komputer menuju suatu domain.
> Bagian dari kelompok peranti Impacket.
> Informasi lebih lanjut: <https://github.com/fortra/impacket>.

- Tambahkan suatu komputer dengan nama dan kata sandi:

`addcomputer.py -computer-name {{NAMA_KOMPUTER$}} -computer-pass {{kata_sandi_komputer}} {{domain}}/{{username}}:{{kata_sandi}}`

- Hanya atur kata sandi untuk perangkat komputer saat ini:

`addcomputer.py -no-add -computer-name {{NAMA_KOMPUTER$}} -computer-pass {{kata_sandi_komputer}} {{domain}}/{{username}}:{{kata_sandi}}`

- Hapus suatu akun perangkat komputer:

`addcomputer.py -delete -computer-name {{NAMA_KOMPUTER$}} {{domain}}/{{username}}:{{kata_sandi}}`

- Tambahkan perangkat komputer melalui protokol autentikasi Kerberos:

`addcomputer.py -k -no-pass {{domain}}/{{username}}@{{nama_host}}`

- Tambahkan perangkat komputer melalui protokol LDAPS (port 636) daripada SAMR (port 445):

`addcomputer.py -method LDAPS -port 636 {{domain}}/{{username}}:{{kata_sandi}}`

- Tentukan nama pengontrol domain (DC) yang akan dipakai, jika terdapat beberapa DC yang terhubung:

`addcomputer.py -dc-host {{nama_host}} {{domain}}/{{username}}:{{kata_sandi}}`
