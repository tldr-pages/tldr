# cs complete dep

> Lehetővé teszi a fejlesztő számára, hogy könyvtárakat keressen anélkül, hogy közvetlenül a weben keresne, hanem a parancssorból. További információ: <https://get-coursier.io/docs/cli-complete>.

- Kinyomtatja, hogy mely artefaktumok vannak egy adott Maven csoport azonosítója alatt közzétéve:

`cs complete-dep {{group_id}}`

- Egy adott Maven csoportazonosító és egy artefakt azonosító alatt közzétett könyvtárverziók listázása:

`cs complete-dep {{group_id}}:{{artifact_id}}`

- Nyomtassa ki, mely artefaktumok vannak publikálva egy adott Maven groupId alatt az ivy2localban keresve:

`cs complete-dep {{group_id}} --repository ivy2local`

- Listázza a közzétett artefaktumokat egy adott tárolóban és hitelesítő adatokban keresett Maven csoportazonosító alatt:

`cs complete-dep {{group_id}}:{{artifact_id}} --repository {{repository_url}} --credentials {{user}}:{{password}}`
