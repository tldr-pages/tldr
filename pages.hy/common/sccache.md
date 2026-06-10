# sccache

> Արագ C/C++/Rust կոմպիլյատորի քեշ:.
> Կազմված է հաճախորդից և սերվերից, որոնք երկուսն էլ աշխատում են մեքենայի վրա:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sccache>:.

- Ցույց տալ կազմման վիճակագրությունը.:

`sccache {{[-s|--show-stats]}}`

- Գործարկեք `gcc` (կամ կոմպիլյատորի ցանկացած հրաման) `sccache`-ի միջոցով:

`sccache gcc {{path/to/file.c}}`

- Գործարկեք `sccache` սերվերը առաջին պլանում և տպեք տեղեկամատյանները.:

`sccache --stop-server; SCCACHE_LOG=trace SCCACHE_START_SERVER=1 SCCACHE_NO_DAEMON=1 sccache`

- Հարցրեք ժամանակացույցին բաշխված կազմման կարգավիճակի համար.:

`sccache --dist-status`
