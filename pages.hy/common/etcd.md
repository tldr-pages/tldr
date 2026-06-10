# և այլն

> Բաշխված, հուսալի բանալի արժեքի պահեստ՝ բաշխված համակարգի ամենակարևոր տվյալների համար:.
> Լրացուցիչ տեղեկություններ. <https://etcd.io/docs/latest/op-guide/configuration/#command-line-flags>:.

- Սկսեք մեկ հանգույցով etcd կլաստեր.:

`etcd`

- Սկսեք մեկ հանգույցի etcd կլաստեր՝ լսելով հաճախորդի հարցումները հատուկ URL-ով.:

`etcd --advertise-client-urls {{http://127.0.0.1:1234}} --listen-client-urls {{http://127.0.0.1:1234}}`

- Սկսեք մեկ հանգույցի etcd կլաստեր հատուկ անունով.:

`etcd --name {{my_etcd_cluster}}`

- Սկսեք մեկ հանգույցի etcd կլաստեր՝ ընդարձակ չափորոշիչներով, որոնք հասանելի են <http://localhost:2379/debug/pprof/> կայքում:

`etcd --enable-pprof --metrics extensive`
