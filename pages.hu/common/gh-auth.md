# gh auth

> Hitelesítse magát egy GitHub hoszton a parancssorból. További információ: <https://cli.github.com/manual/gh_auth>.

- Jelentkezzen be interaktív prompt segítségével:

`gh auth login`

- Bejelentkezés egy tokennel a standard bemenetről (a https://github.com/settings/tokens oldalon létrehozott):

`echo {{your_token}} | gh auth login --with-token`

- Ellenőrizze, hogy be van-e jelentkezve:

`gh auth status`

- Jelentkezzen ki:

`gh auth logout`

- Bejelentkezés egy adott GitHub Enterprise Serverrel:

`gh auth login --hostname {{github.example.com}}`

- Frissítse a munkamenetet, hogy a hitelesítési hitelesítő adatok a megfelelő minimális hatókörökkel rendelkezzenek (eltávolítja a korábban kért további hatóköröket):

`gh auth refresh`

- Bővítse ki az engedélyek hatókörét:

`gh auth refresh --scopes {{repo,admin:repo_hook,admin:org,admin:public_key,admin:org_hook,...}}`
