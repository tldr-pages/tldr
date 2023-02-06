# salt-key

> Kezeli a salt minion kulcsokat a salt master-en. A salt master-en kell futtatni, valószínűleg root-ként vagy sudo-val. További információ: <https://docs.saltstack.com/ref/cli/salt-key.html>.

- Listázza az összes elfogadott, nem elfogadott és elutasított minion kulcsot:

`salt-key -L`

- Elfogad egy minion kulcsot név szerint:

`salt-key -a {{MINION_ID}}`

- Minion kulcsok elutasítása név szerint:

`salt-key -r {{MINION_ID}}`

- Az összes nyilvános kulcs ujjlenyomatának kinyomtatása:

`salt-key -F`
