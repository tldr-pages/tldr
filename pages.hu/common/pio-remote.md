# pio remote

> Segédparancs a PlatformIO távoli fejlesztéshez.`pio remote [command]` ugyanazokat az argumentumokat veszi fel, mint a helyben futtatható `pio [command]`. További információ: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>.

- Az összes aktív távoli ügynök listázása:

`pio remote agent list`

- Új távoli ügynök indítása egy adott névvel, és megosztása a barátokkal:

`pio remote agent start --name {{agent_name}} --share {{example1@example.com}} --share {{example2@example.com}}`

- Megadott ügynökök eszközeinek listázása (az összes ügynök megadásához hagyja ki a `--agent` címet):

`pio remote --agent {{agent_name1}} --agent {{agent_name2}} device list`

- Csatlakozás egy távoli eszköz soros portjához:

`pio remote --agent {{agent_name}} device monitor`

- Egy megadott ügynök összes célpontjának futtatása:

`pio remote --agent {{agent_name}} run`

- A telepített alapcsomagok, fejlesztési platformok és globális könyvtárak frissítése egy adott ügynökön:

`pio remote --agent {{agent_name}} update`

- Az összes teszt futtatása minden környezetben egy adott ügynökön:

`pio remote --agent {{agent_name}} test`
