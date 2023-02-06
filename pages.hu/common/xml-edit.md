# xml edit

> XML-dokumentum szerkesztése. További információ: <http://xmlstar.sourceforge.net/docs.php>.

- XPATH-nak megfelelő elemek törlése egy XML-dokumentumból:

`xml edit --delete "{{XPATH1}}" {{path/to/input.xml|URI}}`

- Egy XML-dokumentum elemcsomópontjának áthelyezése az XPATH1-ről az XPATH2-re:

`xml edit --move "{{XPATH1}}" "{{XPATH2}}" {{path/to/input.xml|URI}}`

- Az összes "id" nevű attribútum átnevezése "ID"-re:

`xml edit --rename "{{//*/@id}}" -v "{{ID}}" {{path/to/input.xml|URI}}`

- A "table" elem "rec" nevű alelemeinek átnevezése "record"-ra:

`xml edit --rename "{{/xml/table/rec}}" -v "{{record}}" {{path/to/input.xml|URI}}`

- Az "id=3" értékű XML-tábla rekordjának frissítése "id=5" értékre:

`xml edit --update "{{xml/table/rec[@id=3]/@id}}" -v {{5}} {{path/to/input.xml|URI}}`

- A `edit` alparancs súgójának megjelenítése:

`xml edit --help`
