# ssh-agent

> Memulai sebuah proses SSH Agent.
> SSH Agent menyimpan kunci SSH yang terdekripsi di dalam memori hingga kunci tersebut dihapus atau prosesnya dimatikan.
> Lihat juga: `ssh-add`, yang dapat menambah dan mengelola kunci yang disimpan oleh SSH Agent.
> Informasi lebih lanjut: <https://man.openbsd.org/ssh-agent>.

- Mulai sebuah SSH Agent untuk sesi shell saat ini:

`eval $(ssh-agent)`

- Matikan agen yang sedang berjalan:

`ssh-agent -k`
