#կոլիմա

> Կոնտեյների գործարկման ժամանակներ macOS-ի և Linux-ի համար՝ նվազագույն կարգավորումներով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/abiosoft/colima>:.

- Սկսեք դևոնը հետին պլանում.:

`colima start`

- Ստեղծեք կազմաձևման ֆայլ և օգտագործեք այն.:

`colima start --edit`

- Սկսեք և կարգավորեք բեռնարկղը (տեղադրեք `nerdctl`՝ բեռնարկղը `nerdctl`-ի միջոցով օգտագործելու համար):

`colima start --runtime containerd`

- Սկսեք Kubernetes-ից (`kubectl` պարտադիր է):

`colima start --kubernetes`

- Անհատականացրեք պրոցեսորի քանակը, RAM հիշողությունը և սկավառակի տարածությունը (GiB-ում).:

`colima start --cpu {{number}} --memory {{memory}} --disk {{storage_space}}`

- Օգտագործեք Docker-ը Colima-ի միջոցով (Docker-ը պարտադիր է).:

`colima start`

- Թվարկեք բեռնարկղերը իրենց տեղեկություններով և կարգավիճակով.:

`colima list`

- Ցույց տալ գործարկման կարգավիճակը.:

`colima status`
