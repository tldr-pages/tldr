# autoflake

> Հեռացրեք չօգտագործված ներմուծումները և փոփոխականները Python կոդից:.
> Լրացուցիչ տեղեկություններ. <https://github.com/PyCQA/autoflake#advanced-usage>:.

- Հեռացրեք չօգտագործված փոփոխականները մեկ ֆայլից և ցուցադրեք տարբերությունը.:

`autoflake --remove-unused-variables {{path/to/file.py}}`

- Հեռացրեք չօգտագործված ներմուծումները բազմաթիվ ֆայլերից և ցուցադրեք տարբերությունները.:

`autoflake --remove-all-unused-imports {{path/to/file1.py path/to/file2.py ...}}`

- Հեռացրեք չօգտագործված փոփոխականները ֆայլից՝ վերագրանցելով ֆայլը.:

`autoflake --remove-unused-variables --in-place {{path/to/file.py}}`

- Հեռացրեք չօգտագործված փոփոխականները ռեկուրսիվորեն գրացուցակի բոլոր ֆայլերից՝ վերագրանցելով յուրաքանչյուր ֆայլ.:

`autoflake --remove-unused-variables --in-place --recursive {{path/to/directory}}`
