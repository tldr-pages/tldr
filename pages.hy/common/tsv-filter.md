# tsv-ֆիլտր

> Զտել TSV ֆայլի տողերը՝ առանձին դաշտերի վրա թեստեր անցկացնելով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/eBay/tsv-utils#tsv-filter>:.

- Տպեք այն տողերը, որտեղ կոնկրետ սյունակը թվայինորեն հավասար է տվյալ թվին.:

`tsv-filter -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`

- Տպեք այն տողերը, որտեղ կոնկրետ սյունակը [e]qual/[l]ess [t]han/[l]ess քան կամ [e]qual/[g]reater [t]han/[g]reater, քան կամ [e]հավասար է տվյալ թվին.:

`tsv-filter --{{eq|ne|lt|le|gt|ge}} {{column_number}}:{{number}} {{path/to/tsv_file}}`

- Տպեք այն տողերը, որտեղ կոնկրետ սյունակը [eq]ual/[n]ot [e]qual/part of/not մաս է տրված տողի:

`tsv-filter --str-{{eq|ne|in-fld|not-in-fld}} {{column_number}}:{{string}} {{path/to/tsv_file}}`

- Զտիչ ոչ դատարկ դաշտերի համար.:

`tsv-filter --not-empty {{column_number}} {{path/to/tsv_file}}`

- Տպեք այն տողերը, որտեղ որոշակի սյունակ դատարկ է.:

`tsv-filter --invert --not-empty {{column_number}} {{path/to/tsv_file}}`

- Տպեք այն տողերը, որոնք բավարարում են երկու պայման.:

`tsv-filter --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- Տպեք տողերը, որոնք համապատասխանում են առնվազն մեկ պայմանին.:

`tsv-filter --or --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- Հաշվեք համապատասխանող տողերը՝ առաջին տողը մեկնաբանելով որպես [H]eader.:

`tsv-filter --count -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`
