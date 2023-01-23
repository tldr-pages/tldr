# glab auth

> Hitelesítés egy GitLab hoszton a parancssorból. További információ: <https://glab.readthedocs.io/en/latest/auth>.

- Jelentkezzen be interaktív prompt segítségével:

`glab auth login`

- Jelentkezzen be egy tokennel:

`glab auth login --token {{token}}`

- Ellenőrizze a hitelesítés állapotát:

`glab auth status`

- Bejelentkezés egy adott GitLab példányba:

`glab auth login --hostname {{gitlab.example.com}}`
