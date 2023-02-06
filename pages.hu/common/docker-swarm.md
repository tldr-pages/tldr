# docker swarm

> Egy konténer-orchestrációs eszköz. További információ: <https://docs.docker.com/engine/swarm/>.

- Egy raj fürt inicializálása:

`docker swarm init`

- Megjeleníti a tokent, hogy csatlakozzon egy menedzserhez vagy egy munkáshoz:

`docker swarm join-token {{worker|manager}}`

- Új csomópont csatlakozása a fürthöz:

`docker swarm join --token {{token}} {{manager_node_url:2377}}`

- Egy munkás eltávolítása a rajból (a munkás csomóponton belül futtatva):

`docker swarm leave`

- Az aktuális hitelesítésszolgáltatói tanúsítvány megjelenítése PEM formátumban:

`docker swarm ca`

- Az aktuális CA-tanúsítvány forgatása és az új tanúsítvány megjelenítése:

`docker swarm ca --rotate`

- A csomóponti tanúsítványok érvényességi idejének módosítása:

`docker swarm update --cert-expiry {{hours}}h{{minutes}}m{{seconds}}s`
