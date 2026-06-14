#պիգմենտացնել

> Python-ի վրա հիմնված շարահյուսական ընդգծող:.
> Լրացուցիչ տեղեկություններ. <https://pygments.org/docs/cmdline/>:.

- Նշեք ֆայլի շարահյուսությունը և տպեք `stdout` (լեզուն ենթադրվում է ֆայլի ընդլայնումից).:

`pygmentize {{file.py}}`

- Հստակորեն սահմանեք շարահյուսության ընդգծման լեզուն.:

`pygmentize -l {{javascript}} {{input_file}}`

- Ցուցակեք մատչելի lexers (պրոցեսորներ մուտքային լեզուների համար).:

`pygmentize -L lexers`

- Պահպանեք արդյունքը ֆայլի մեջ HTML ձևաչափով.:

`pygmentize -f html -o {{output_file.html}} {{input_file.py}}`

- Ցուցակեք հասանելի ելքային ձևաչափերը.:

`pygmentize -L formatters`

- Արտադրեք HTML ֆայլ՝ ձևաչափի լրացուցիչ ընտրանքներով (ամբողջական էջ, տողերի համարներով).:

`pygmentize -f html -O "full,linenos=True" -o {{output_file.html}} {{input_file}}`
