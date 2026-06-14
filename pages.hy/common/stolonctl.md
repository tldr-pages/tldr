# stolonctl

> CLI Stolon-ի համար, PostgreSQL-ի ամպի բնիկ մենեջեր PostgreSQL բարձր հասանելիության համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sorintlab/stolon/blob/master/doc/commands/stolonctl.md>:.

- Ստացեք կլաստերի կարգավիճակը.:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} status`

- Ստացեք կլաստերային տվյալներ.:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} clusterdata`

- Ստացեք կլաստերի ճշգրտում.:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} spec`

- Թարմացրեք կլաստերի ճշգրտումը JSON ձևաչափով կարկատով.:

`stolonctl --cluster-name {{cluster_name}} --store-backend {{store_backend}} --store-endpoints {{store_endpoints}} update --patch '{{cluster_spec}}'`
