# stolonctl

> CLI a Stolonhoz, egy felhő natív PostgreSQL menedzserhez a PostgreSQL magas rendelkezésre állásához. További információ: <https://github.com/sorintlab/stolon>.

- Klaszter állapotának lekérdezése:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} status`

- Klaszteradatok lekérdezése:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} clusterdata`

- Klaszter specifikáció lekérdezése:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} spec`

- Frissítse a fürt specifikációját egy javítással JSON formátumban:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} update --patch '{{cluster_spec}}'`
