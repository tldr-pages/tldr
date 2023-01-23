# ssh-keygen

> Hitelesítéshez, jelszó nélküli bejelentkezésekhez és egyéb dolgokhoz használt ssh kulcsok generálása. További információ: <https://man.openbsd.org/ssh-keygen>.

- Kulcs generálása interaktívan:

`ssh-keygen`

- Adja meg a fájlt, amelybe a kulcsot menteni kívánja:

`ssh-keygen -f {{~/.ssh/filename}}`

- Generáljon egy ed25519 kulcsot 100 kulcsderiválási függvénykörrel:

`ssh-keygen -t {{ed25519}} -a {{100}}`

- RSA 4096 bites kulcs generálása e-mail megjegyzéssel:

`ssh-keygen -t {{dsa|ecdsa|ed25519|rsa}} -b {{4096}} -C "{{comment|email}}"`

- Egy állomás kulcsainak eltávolítása a known_hosts fájlból (hasznos, ha egy ismert állomás új kulccsal rendelkezik):

`ssh-keygen -R {{remote_host}}`

- Egy kulcs ujjlenyomatának lekérdezése MD5 Hex-ben:

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/filename}}`

- Egy kulcs jelszavának módosítása:

`ssh-keygen -p -f {{~/.ssh/filename}}`

- A kulcsformátum típusának megváltoztatása (például OPENSSH formátumról PEM-re), a fájl helyben átíródik:

`ssh-keygen -p -N "" -m {{PEM}} -f {{~/.ssh/OpenSSH_private_key}}`
