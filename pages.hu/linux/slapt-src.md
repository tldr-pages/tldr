# slapt-src

> A slackbuildek építésének automatizálására szolgáló segédprogram. A SlackBuild forrásokat a slapt-srcrc fájlban kell beállítani. További információ: <https://github.com/jaos/slapt-src>.

- Az elérhető slackbuildek és verziók listájának frissítése:

`slapt-src --update`

- Az összes elérhető slackbuild listája:

`slapt-src --list`

- A megadott slackbuild(ek) lekérése, összeállítása és telepítése:

`slapt-src --install {{slackbuild_name}}`

- A slackbuildek keresése a nevük vagy leírásuk alapján:

`slapt-src --search {{search_term}}`

- Információk megjelenítése egy slackbuildről:

`slapt-src --show {{slackbuild_name}}`
