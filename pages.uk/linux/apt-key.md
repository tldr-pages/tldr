# apt-key

> Утиліта керування ключами для диспетчера пакетів APT в Debian та Ubuntu.
> Примітка: `apt-key` застарілий (за винятком використання `apt-key del` у сценаріях підтримки).
> Більше інформації: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Список довірених ключів:

`apt-key list`

- Додати ключ до довіреного сховища ключів:

`apt-key add {{public_key_file.asc}}`

- Видалити ключ з довіреного сховища ключів:

`apt-key del {{key_id}}`

- Додайте віддалений ключ до надійного сховища ключів:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- Додати ключ із сервера ключів лише з ідентифікатором ключа:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
