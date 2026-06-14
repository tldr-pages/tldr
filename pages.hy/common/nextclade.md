#հաջորդկլադ

> Կենսաինֆորմատիկայի գործիք վիրուսի գենոմի հավասարեցման, կլադի նշանակման և qc ստուգումների համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextclade-cli/reference.html>:.

- Հավասարեցրեք հաջորդականությունները օգտատիրոջ կողմից տրամադրված տեղեկանքին՝ դուրս բերելով հավասարեցումը ֆայլի մեջ.:

`nextclade run {{path/to/sequences.fa}} {{[-r|--input-ref]}} {{path/to/reference.fa}} {{[-o|--output-fasta]}} {{path/to/alignment.fa}}`

- Ստեղծեք TSV հաշվետվություն՝ ավտոմատ կերպով ներբեռնելով վերջին տվյալների բազան.:

`nextclade run {{path/to/fasta}} {{[-d|--dataset-name]}} {{dataset_name}} {{[-t|--output-tsv]}} {{path/to/report.tsv}}`

- Թվարկեք բոլոր առկա տվյալների հավաքածուները.:

`nextclade dataset list`

- Ներբեռնեք SARS-CoV-2-ի վերջին տվյալների բազան.:

`nextclade dataset get {{[-n|--name]}} sars-cov-2 {{[-o|--output-dir]}} {{path/to/directory}}`

- Օգտագործեք ներբեռնված տվյալների բազա՝ արտադրելով բոլոր արդյունքները.:

`nextclade run {{[-D|--input-dataset]}} {{path/to/dataset_directory}} {{[-O|--output-all]}} {{path/to/output_directory}} {{path/to/sequences.fasta}}`

- Գործարկել բազմաթիվ ֆայլերի վրա.:

`nextclade run {{[-d|--dataset-name]}} {{dataset_name}} {{[-t|--output-tsv]}} {{path/to/output_tsv}} -- {{path/to/input_fasta_1 path/to/input_fasta_2 ...}}`

- Փորձեք հակադարձ լրացնել, եթե հաջորդականությունը չի համընկնում.:

`nextclade run --retry-reverse-complement {{[-d|--dataset-name]}} {{dataset_name}} {{[-t|--output-tsv]}} {{path/to/output_tsv}} {{path/to/input_fasta}}`
