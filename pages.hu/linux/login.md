# login

> Munkamenetet kezdeményez egy felhasználó számára. További információ: <https://manned.org/login>.

- Bejelentkezés felhasználóként:

`login {{user}}`

- Bejelentkezés felhasználóként hitelesítés nélkül, ha a felhasználó előzetesen hitelesített:

`login -f {{user}}`

- Bejelentkezés felhasználóként és a környezet megőrzése:

`login -p {{user}}`

- Bejelentkezés felhasználóként egy távoli állomáson:

`login -h {{host}} {{user}}`
