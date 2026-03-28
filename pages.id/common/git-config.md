# git config

> Ubah pengaturan Git untuk repositori-repositori tertentu.
> Konfigurasi ini dapat diatur hanya untuk repositori saat ini (lokal/local) atau untuk pengguna sistem operasi saat ini (global).
> Informasi lebih lanjut: <https://git-scm.com/docs/git-config>.

- Tentukan nama atau alamat surel Anda secara global (informasi ini diperlukan untuk melakukan proses komit, dan akan dicantumkan dalam seluruh komit Anda):

`git config --global {{user.name|user.email}} "{{Nama Anda|surel@example.com}}"`

- Tampilkan daftar pengaturan Git untuk lingkungan lokal, global, atau sistem operasi, dan tampilkan lokasi berkas tersebut:

`git config {{[-l|--list]}} --{{local|global|system}} --show-origin`

- Tentukan nilai global atas suatu entri konfigurasi (dalam hal ini merupakan alias):

`git config --global {{alias.unstage}} "reset HEAD --"`

- Dapatkan nilai atas entri konfigurasi saat ini:

`git config {{alias.unstage}}`

- Gunakan suatu perintah alias:

`git {{unstage}}`

- Hapus atau kembalikan nilai dari entri konfigurasi tersebut menuju nilai default (bila ada):

`git config --global --unset {{alias.unstage}}`

- Sunting konfigurasi Git pada repositori saat ini dengan aplikasi pengolah teks default:

`git config {{[-e|--edit]}}`

- Sunting konfigurasi Git pada pengguna saat ini (dalam berkas `~/.gitconfig` atau `$XDG_CONFIG_HOME/git/config` bila ada) dengan aplikasi pengolah teks default:

`git config --global {{[-e|--edit]}}`
