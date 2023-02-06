# docker login

> Jelentkezzen be egy dokkoló regiszterbe. További információ: <https://docs.docker.com/engine/reference/commandline/login/>.

- Interaktív bejelentkezés egy registrybe:

`docker login`

- Jelentkezzen be egy nyilvántartásba egy adott felhasználónévvel (a felhasználónak jelszót kell megadnia):

`docker login --username {{username}}`

- Bejelentkezés egy regiszterbe felhasználónévvel és jelszóval:

`docker login --username {{username}} --password {{password}} {{server}}`

- Bejelentkezés egy kibocsátásiegység-forgalmi jegyzékbe jelszóval a `stdin` oldalról:

`echo "{{password}}" | docker login --username {{username}} --password-stdin`
