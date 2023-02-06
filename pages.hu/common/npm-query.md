# npm query

> Függőségi objektumok tömbjének kiírása CSS-szerű szelektorok használatával. További információ: <https://docs.npmjs.com/cli/v8/commands/npm-query>.

- Közvetlen függőségek nyomtatása:

`npm query ':root > *'`

- Az összes közvetlen termelési/fejlesztési függőség kiírása:

`npm query ':root > .{{prod|dev}}'`

- Egy adott névvel rendelkező függőségek nyomtatása:

`npm query '#{{package_name}}'`

- Egy adott névvel és egy szemantikus verziószámtartományon belüli függőségek nyomtatása:

`npm query #{{package_name}}@{{semantic_version}}`

- Függőségek nyomtatása, amelyeknek nincsenek függőségei:

`npm query ':empty'`

- Az összes függőség megkeresése és eltávolítása utólagos telepítési szkriptekkel:

`npm query ":attr(scripts, [postinstall])" | jq 'map(.name) | join("\n")' -r | xargs -I {} npm uninstall {}`

- Az összes Git-függőség megkeresése és annak kiírása, hogy melyik alkalmazásnak van szüksége rájuk:

`npm query ":type(git)" | jq 'map(.name)' | xargs -I {} npm why {}`
