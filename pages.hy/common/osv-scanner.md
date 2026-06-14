# osv-սկաներ

> Սկանավորեք տարբեր միջավայրեր կախվածությունների համար և համապատասխանեցրեք դրանք OSV տվյալների բազայի հետ:.
> Լրացուցիչ տեղեկություններ. <https://google.github.io/osv-scanner/usage/>:.

- Սկանավորեք Docker պատկերը.:

`osv-scanner -D {{docker_image_name}}`

- Փաթեթի կողպեքի ֆայլի սկանավորում.:

`osv-scanner -L {{path/to/lockfile}}`

- Սկանավորեք SBOM ֆայլը.:

`osv-scanner -S {{path/to/sbom_file}}`

- Սկանավորեք բազմաթիվ գրացուցակներ ռեկուրսիվ կերպով.:

`osv-scanner -r {{directory1 directory2 ...}}`

- Բաց թողեք Git պահեստների սկանավորումը.:

`osv-scanner --skip-git {{-r|-D}} {{target}}`

- Արդյունք JSON ձևաչափով.:

`osv-scanner --json {{-D|-L|-S|-r}} {{target}}`
