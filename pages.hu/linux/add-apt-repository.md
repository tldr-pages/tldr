# add-apt-repository

> Kezeli az apt repository definíciókat. További információ: <https://manned.org/apt-add-repository>.

- Új apt tároló hozzáadása:

`add-apt-repository {{repository_spec}}`

- Egy apt tároló eltávolítása:

`add-apt-repository --remove {{repository_spec}}`

- A csomagtár gyorsítótárának frissítése egy tároló hozzáadása után:

`add-apt-repository --update {{repository_spec}}`

- Forráscsomagok letöltésének engedélyezése a tárolóból:

`add-apt-repository --enable-source {{repository_spec}}`
