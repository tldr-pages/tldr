# powerstat

> Az akkumulátoros áramforrással rendelkező vagy a RAPL interfészt támogató számítógép energiafogyasztását méri. További információ: <https://manned.org/powerstat>.

- A teljesítmény mérése alapértelmezés szerint 10 minta 10 másodperces időközzel:

`powerstat`

- A teljesítmény mérése egyéni mintaszámmal és intervallum időtartamával:

`powerstat {{interval}} {{number_of_samples}}`

- Az Intel RAPL-interfész segítségével történő teljesítménymérés:

`powerstat -R {{interval}} {{number_of_samples}}`

- A teljesítménymérések hisztogramjának megjelenítése:

`powerstat -H {{interval}} {{number_of_samples}}`

- Minden statisztikagyűjtési opció engedélyezése:

`powerstat -a {{interval}} {{number_of_samples}}`
