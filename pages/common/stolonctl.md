# Stolon

> Stolon is a cloud native PostgreSQL manager for PostgreSQL high availability.

- Get cluster status:

`stolonctl --cluster-name ${{stolon_cluster_name}} --store-backend ${{stolon_store_backend}} --store-endpoints ${{stolon_store_endpoints}} status`

- Get cluster data:

`stolonctl --cluster-name ${{stolon_cluster_name}} --store-backend ${{stolon_store_backend}} --store-endpoints ${{stolon_store_endpoints}} clusterdata`

- Get cluster specification:

`stolonctl --cluster-name ${{stolon_cluster_name}} --store-backend ${{stolon_store_backend}} --store-endpoints ${{stolon_store_endpoints}} spec`

- Update cluster specification:

`stolonctl --cluster-name ${{stolon_cluster_name}} --store-backend ${{stolon_store_backend}} --store-endpoints ${{stolon_store_endpoints}} update --patch '{{cluster_spec_to_be_updated_as_json}}'`
