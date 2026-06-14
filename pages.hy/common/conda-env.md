# conda env

> Կառավարեք կոնդա միջավայրերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/env/index.html>:.

- Ստեղծեք միջավայր շրջակա միջավայրի ֆայլից (YAML, TXT և այլն):

`conda env create {{[-f|--file]}} {{path/to/file}}`

- Ջնջել միջավայրը և դրա մեջ եղած ամեն ինչ.:

`conda env remove {{[-n|--name]}} {{environment_name}}`

- Թարմացրեք միջավայրը շրջակա միջավայրի ֆայլի հիման վրա.:

`conda env update {{[-f|--file]}} {{path/to/file}} --prune`

- Թվարկեք բոլոր միջավայրերը.:

`conda env list`

- Դիտեք շրջակա միջավայրի մանրամասները.:

`conda env export`

- Ցուցակել շրջակա միջավայրի փոփոխականները.:

`conda env config vars list`

- Սահմանել շրջակա միջավայրի փոփոխականները.:

`conda env config vars set {{my_var}}={{value}}`
