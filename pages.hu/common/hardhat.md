# hardhat

> Fejlesztői környezet Ethereum szoftverekhez. További információ: <https://hardhat.org>.

- Az elérhető alparancsok listája (vagy új projekt létrehozása, ha nincs konfiguráció):

`hardhat`

- Az aktuális projekt fordítása és az összes artefaktum összeállítása:

`hardhat compile`

- Egy felhasználó által definiált szkript futtatása a projekt lefordítása után:

`hardhat run {{path/to/script.js}}`

- Mocha tesztek futtatása:

`hardhat test`

- Az összes megadott tesztfájl futtatása:

`hardhat test {{path/to/file1.js}} {{path/to/file2.js}}`

- Helyi Ethereum JSON-RPC csomópont indítása a fejlesztéshez:

`hardhat node`

- Helyi Ethereum JSON-RPC csomópont indítása egy adott hostnévvel és porttal:

`hardhat node --hostname {{hostname}} --port {{port}}`

- A gyorsítótár és az összes artefakt megtisztítása:

`hardhat clean`
