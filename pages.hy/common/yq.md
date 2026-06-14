# yq

> Թեթև և շարժական YAML պրոցեսոր:.
> Լրացուցիչ տեղեկություններ. <https://mikefarah.gitbook.io/yq/>:.

- Արտադրեք YAML ֆայլ, գեղեցիկ տպագիր ձևաչափով (v4+):

`yq eval {{path/to/file.yaml}}`

- Արտադրեք YAML ֆայլ, գեղեցիկ տպագիր ձևաչափով (v3):

`yq read {{path/to/file.yaml}} {{[-C|--colors]}}`

- Արտադրեք առաջին տարրը YAML ֆայլում, որը պարունակում է միայն զանգված (v4+):

`yq eval '.[0]' {{path/to/file.yaml}}`

- Արտադրեք առաջին տարրը YAML ֆայլում, որը պարունակում է միայն զանգված (v3):

`yq read {{path/to/file.yaml}} '[0]'`

- Սահմանեք (կամ վերագրեք) ֆայլի արժեքի բանալի (v4+).:

`yq eval '.{{key}} = "{{value}}"' {{[-i|--inplace]}} {{path/to/file.yaml}}`

- Սահմանեք (կամ վերագրեք) ֆայլի արժեքի բանալի (v3):

`yq write {{[-i|--inplace]}} {{path/to/file.yaml}} '{{key}}' '{{value}}'`

- Միավորել երկու ֆայլ և տպել `stdout` (v4+):

`yq eval-all 'select(filename == "{{path/to/file1.yaml}}") * select(filename == "{{path/to/file2.yaml}}")' {{path/to/file1.yaml}} {{path/to/file2.yaml}}`

- Միավորել երկու ֆայլ և տպել `stdout` (v3):

`yq merge {{path/to/file1.yaml}} {{path/to/file2.yaml}} {{[-C|--colors]}}`
