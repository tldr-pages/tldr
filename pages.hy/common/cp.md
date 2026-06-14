# cp

> Պատճենել ֆայլերը և գրացուցակները:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>:.

- Պատճենեք ֆայլը մեկ այլ վայրում.:

`cp {{path/to/source_file}} {{path/to/target_file}}`

- Պատճենեք ֆայլը մեկ այլ գրացուցակում՝ պահպանելով ֆայլի անունը.:

`cp {{path/to/source_file}} {{path/to/target_parent_directory}}`

- Ռեկուրսիվ կերպով պատճենեք գրացուցակի բովանդակությունը մեկ այլ վայրում (եթե նպատակակետը գոյություն ունի, գրացուցակը պատճենվում է դրա ներսում).:

`cp {{[-r|--recursive]}} {{path/to/source_directory}} {{path/to/target_directory}}`

- Պատճենեք գրացուցակը ռեկուրսիվ կերպով, բառացի ռեժիմով (ցուցադրում է ֆայլերը, երբ դրանք պատճենվում են).:

`cp {{[-vr|--verbose --recursive]}} {{path/to/source_directory}} {{path/to/target_directory}}`

- Պատճենեք բազմաթիվ ֆայլեր միանգամից գրացուցակում.:

`cp {{[-t|--target-directory]}} {{path/to/destination_directory}} {{path/to/file1 path/to/file2 ...}}`

- Պատճենեք բոլոր ֆայլերը հատուկ ընդլայնմամբ մեկ այլ վայրում, ինտերակտիվ ռեժիմում (հուշում է օգտվողին նախքան վերագրելը).:

`cp {{[-i|--interactive]}} {{*.ext}} {{path/to/target_directory}}`

- Պատճենելուց առաջ հետևեք խորհրդանշական հղումներին.:

`cp {{[-L|--dereference]}} {{link}} {{path/to/target_directory}}`

- Օգտագործեք աղբյուրի ֆայլերի ամբողջական ուղին, պատճենելու ժամանակ ստեղծելով բացակայող միջանկյալ գրացուցակներ.:

`cp --parents {{source/path/to/file}} {{path/to/target_file}}`
