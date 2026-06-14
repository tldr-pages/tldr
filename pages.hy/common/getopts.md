# ստանալ

> Վերլուծել պատյանների ընտրանքները փաստարկներից:.
> Նշում. այս հրամանը չի աջակցում երկար ձևի ընտրանքներին, ուստի դրա փոխարեն խորհուրդ է տրվում օգտագործել `getopt`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-getopts>:.

- Ստուգեք, թե արդյոք որևէ տարբերակ առաջին ընտրանքն է ընթացիկ համատեքստում.:

`getopts {{x}} {{opt}}; echo ${{opt}}`

- Ստուգեք՝ արդյոք ընտրանքը դրված է տողի մեջ (նշված տարբերակը պետք է լինի տողի առաջին տարրը).:

`getopts {{x}} {{opt}} "{{string text}}"; echo ${{opt}}`

- Սահմանեք արգումենտ պահանջելու տարբերակ և տպեք դրանք.:

`getopts {{x}}: {{opt}}; echo ${{opt}} $OPTARG`

- Ստուգեք բազմաթիվ տարբերակներ.:

`while getopts {{xyz}} {{opt}}; do case ${{opt}} in x) {{echo x is set}};; y) {{echo y is set}};; z) {{echo z is set}};; esac; done`

- Սահմանեք `getopts`-ը լուռ ռեժիմի և կարգավորեք ընտրանքային սխալները.:

`while getopts :{{x:}} {{opt}}; do case ${{opt}} in x) ;; :) {{echo "Argument required"}};; ?) {{echo "Invalid argument"}} esac;; done`

- Վերակայել `getopts`:

`OPTIND=1`
