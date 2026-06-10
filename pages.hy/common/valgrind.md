# valgrind

> Փաթաթում փորձագիտական գործիքների մի շարք ծրագրերի պրոֆիլավորման, օպտիմալացման և վրիպազերծման համար:.
> Սովորաբար օգտագործվող գործիքները ներառում են `memcheck`, `cachegrind`, `callgrind`, `massif`, `helgrind` և `drd`:.
> Լրացուցիչ տեղեկություններ. <https://valgrind.org/docs/manual/manual-core.html#manual-core.options>:.

- Օգտագործեք (կանխադրված) Memcheck գործիքը՝ `program`-ով հիշողության օգտագործման ախտորոշումը ցույց տալու համար:

`valgrind {{program}}`

- Օգտագործեք Memcheck-ը՝ `program`-ի բոլոր հնարավոր արտահոսքերը մանրամասնորեն հաղորդելու համար.:

`valgrind --leak-check=full --show-leak-kinds=all {{program}}`

- Օգտագործեք Cachegrind գործիքը՝ `program`-ի CPU-ի քեշի գործողությունները պրոֆիլավորելու և գրանցելու համար:

`valgrind --tool=cachegrind {{program}}`

- Օգտագործեք «Massif» գործիքը՝ կույտային հիշողությունը պրոֆիլավորելու և գրանցելու համար և `program`-ի օգտագործումը:

`valgrind --tool=massif --stacks=yes {{program}}`
