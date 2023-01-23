# usermod

> Felhasználói fiók módosítása. Lásd még: `users`, `useradd`, `userdel`. További információ: <https://manned.org/usermod>.

- Felhasználónév módosítása:

`sudo usermod --login {{new_username}} {{username}}`

- Felhasználói azonosító módosítása:

`sudo usermod --uid {{id}} {{username}}`

- Felhasználói héj módosítása:

`sudo usermod --shell {{path/to/shell}} {{username}}`

- Felhasználó hozzáadása kiegészítő csoportokhoz (ügyeljen a szóközök hiányára):

`sudo usermod --append --groups {{group1,group2,...}} {{username}}`

- A felhasználó home könyvtárának módosítása:

`sudo usermod --move-home --home {{path/to/new_home}} {{username}}`
