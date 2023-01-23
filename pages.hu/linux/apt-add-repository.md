# apt-add-repository

> Kezeli az apt repository definíciókat. További információ: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Új apt tároló hozzáadása:

`apt-add-repository {{repository_spec}}`

- Egy apt tároló eltávolítása:

`apt-add-repository --remove {{repository_spec}}`

- Frissíti a csomagtár gyorsítótárát egy tároló hozzáadása után:

`apt-add-repository --update {{repository_spec}}`

- Forráscsomagok engedélyezése:

`apt-add-repository --enable-source {{repository_spec}}`
