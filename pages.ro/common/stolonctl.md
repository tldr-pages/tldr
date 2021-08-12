# stolonctl

> CLI pentru Stoton, un manager PostgreSQL nativ în cloud pentru disponibilitate ridicată PostgreSQL.
> Mai multe informaţii: <https://github.com/sorintlab/stolon>

- Obțineți starea clusterului:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} status`

- Obțineți date de cluster:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} clusterdata`

- Obțineți specificația clusterului:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} spec`

- Actualizare specificație cluster cu un patch în format json:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} update --patch '{{cluster_spec}}'`
