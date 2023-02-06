# volta

> Egy JavaScript eszközkezelő, amely telepíti a Node.js futtatóidőket, az npm és Yarn csomagkezelőket, vagy bármilyen bináris állományt az npm-ből. További információ: <https://volta.sh>.

- Az összes telepített eszköz listázása:

`volta list`

- Telepítse egy eszköz legújabb verzióját:

`volta install {{node|npm|yarn|package_name}}`

- Egy eszköz egy adott verziójának telepítése:

`volta install {{node|npm|yarn}}@version`

- Válasszon ki egy eszközverziót egy projekthez (a `package.json` oldalon tárolja):

`volta pin {{node|npm|yarn}}@version`

- Súgó megjelenítése:

`volta help`

- Súgó megjelenítése egy alparancshoz:

`volta help {{fetch|install|uninstall|pin|list|completions|which|setup|run|help}}`
