#մոնաստված

> MongoDB տվյալների բազայի սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://www.mongodb.com/docs/manual/reference/program/mongod/>:.

- Նշեք պահեստավորման գրացուցակը (կանխադրված՝ `/data/db` Linux-ում և macOS-ում, `C:\data\db` Windows-ում):

`mongod --dbpath {{path/to/directory}}`

- Նշեք կազմաձևման ֆայլը.:

`mongod --config {{path/to/file}}`

- Նշեք այն նավահանգիստը, որը պետք է լսել (կանխադրված՝ 27017):

`mongod --port {{port}}`

- Նշեք տվյալների բազայի պրոֆիլավորման մակարդակը: 0-ն անջատված է, 1-ը միայն դանդաղ գործողություն է, 2-ը՝ բոլորը (կանխադրված՝ 0):

`mongod --profile {{0|1|2}}`
