# userdel

> Felhasználói fiók eltávolítása vagy felhasználó eltávolítása egy csoportból. Lásd még: `users`, `useradd`, `usermod`. További információ: <https://manned.org/userdel>.

- Felhasználó eltávolítása:

`sudo userdel {{username}}`

- Felhasználó eltávolítása más gyökérkönyvtárban:

`sudo userdel --root {{path/to/other/root}} {{username}}`

- Felhasználó eltávolítása a home könyvtárral és a levelezési tárral együtt:

`sudo userdel --remove {{username}}`
