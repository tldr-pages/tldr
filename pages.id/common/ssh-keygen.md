# ssh-keygen

> Membuat kunci SSH yang digunakan untuk autentikasi, login tanpa kata sandi, dan hal lainnya.
> Lihat juga: `ssh-copy-id` untuk memasang kunci SSH di host jarak jauh.
> Informasi lebih lanjut: <https://man.openbsd.org/ssh-keygen>.

- Buat kunci kriptografi secara interaktif:

`ssh-keygen`

- Buat kunci kriptografi jenis ed25519 dengan 32 putaran fungsi derivasi kunci (Key Derivation Function) dan simpan kunci ke berkas/fail tertentu:

`ssh-keygen -t {{ed25519}} -a {{32}} -f {{~/.ssh/nama_berkas}}`

- Buat kunci kriptografi jenis RSA 4096-bit dengan email sebagai komentar:

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{komentar|email}}"`

- Hapus kunci sebuah host dari berkas/fail `known_hosts` (digunakan saat host yang dikenal memiliki kunci kriptografi baru):

`ssh-keygen -R {{host_jarak_jauh}}`

- Ambil sidik jari (fingerprint) dari sebuah kunci kriptografi dalam format MD5 Hex:

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/nama_berkas}}`

- Ubah kata sandi (passphrase) sebuah kunci kriptografi:

`ssh-keygen -p -f {{~/.ssh/nama_berkas}}`

- Ubah tipe format kunci (contohnya dari format OPENSSH ke PEM), berkas akan ditimpa di tempat yang sama:

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/kunci_privat_OpenSSH}}`

- Ambil kunci publik dari kunci rahasia (privat):

`ssh-keygen -y -f {{~/.ssh/kunci_privat_OpenSSH}}`
