# conda install

> Տեղադրեք փաթեթներ գոյություն ունեցող կոնդա միջավայրում:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/install.html>:.

- Տեղադրեք մեկ կամ մի քանի փաթեթ ներկայումս ակտիվ կոնդա միջավայրում.:

`conda install {{package1 package2 ...}}`

- Տեղադրեք մեկ փաթեթ ներկայումս ակտիվ կոնդա միջավայրում՝ օգտագործելով channel conda-forge-ը.:

`conda install {{[-c|--channel]}} conda-forge {{package}}`

- Տեղադրեք մեկ փաթեթ ներկայումս ակտիվ կոնդա միջավայրում՝ օգտագործելով channel conda-forge-ը և անտեսելով այլ ալիքները.:

`conda install {{[-c|--channel]}} conda-forge --override-channels {{package}}`

- Տեղադրեք փաթեթի որոշակի տարբերակ.:

`conda install {{package}}={{version}}`

- Տեղադրեք փաթեթը որոշակի միջավայրում.:

`conda install {{[-n|--name]}} {{environment}} {{package}}`

- Թարմացրեք փաթեթը ընթացիկ միջավայրում.:

`conda install --upgrade {{package}}`

- Տեղադրեք փաթեթ և համաձայնեք գործարքներին՝ առանց հուշելու.:

`conda install {{[-y|--yes]}} {{package}}`
