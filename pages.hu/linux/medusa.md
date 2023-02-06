# Medusa

> Egy moduláris és párhuzamos bejelentkezési brute-forcer különböző protokollokhoz. További információ: <https://manned.org/medusa>.

- Brute force végrehajtása egy FTP-kiszolgáló ellen egy felhasználóneveket tartalmazó fájl és egy jelszavakat tartalmazó fájl segítségével:

`medusa -M ftp -h host -U {{path/to/username_file}} -P {{path/to/password_file}}`

- Bejelentkezési kísérlet végrehajtása egy HTTP-kiszolgáló ellen a megadott felhasználónév, jelszó és user-agent használatával:

`medusa -M HTTP -h host -u {{username}} -p {{password}} -m USER-AGENT:"{{Agent}}"`

- Brute force kísérlet végrehajtása MySQL-kiszolgáló ellen egy felhasználóneveket és egy hash-t tartalmazó fájl segítségével:

`medusa -M mysql -h host -U {{path/to/username_file}} -p {{hash}} -m PASS:HASH`

- Brute force kísérlet végrehajtása SMB-kiszolgálók listája ellen egy felhasználónév és egy pwdump fájl felhasználásával:

`medusa -M smbnt -H {{path/to/hosts_file}} -C {{path/to/pwdump_file}} -u {{username}} -m PASS:HASH`
