# pacstall

> AUR csomagkezelő Ubuntu számára. További információ: <https://github.com/pacstall/pacstall>.

- Keresés a csomagadatbázisban egy csomag nevére:

`pacstall --search {{package_name}}`

- Telepítsen egy csomagot:

`pacstall --install {{package_name}}`

- Egy csomag eltávolítása:

`pacstall --remove {{package_name}}`

- Adjon hozzá egy tárolót az adatbázishoz (csak a GitHub és a GitLab támogatott):

`pacstall --add-repo {{remote_repository_location}}`

- A pacstall szkriptek frissítése:

`pacstall --update`

- Az összes csomag frissítése:

`pacstall --upgrade`

- Információk megjelenítése egy csomagról:

`pacstall --query-info {{package_name}}`

- Az összes telepített csomag listázása:

`pacstall --list`
