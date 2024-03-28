# apt-key

> Key management utility for the APT Package Manager on Debian and Ubuntu.
> Note: `apt-key` is now deprecated (except for the use of `apt-key del` in maintainer scripts).
> More information: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Список довірених ключів:

`apt-key list`

- Додати ключ до надійного сховища ключів:

`apt-key add {{public_key_file.asc}}`

- Видалити ключ з довіреного сховища ключів:

`apt-key del {{key_id}}`

- Додайте віддалений ключ до надійного сховища ключів:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- Додати ключ із сервера ключів лише з ідентифікатором ключа:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
