# Պրոյչեր

> Ծրագրի ղեկավար JUCE շրջանակային հավելվածների համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.juce.com/master/projucer_manual.html#projucer_manual_tools_command_line_tools>:.

- Ցուցադրել տեղեկատվություն նախագծի մասին.:

`Projucer --status {{path/to/project_file}}`

- Վերականգնեք բոլոր ֆայլերը և ռեսուրսները նախագծում.:

`Projucer --resave {{path/to/project_file}}`

- Թարմացրեք տարբերակի համարը նախագծում.:

`Projucer --set-version {{version_number}} {{path/to/project_file}}`

- Ստեղծեք JUCE նախագիծ PIP ֆայլից.:

`Projucer --create-project-from-pip {{path/to/PIP}} {{path/to/output}}`

- Հեռացրեք JUCE ոճի բոլոր մեկնաբանությունները (`//=====`, `//-----` կամ `///////`):

`Projucer --tidy-divider-comments {{path/to/target_folder}}`

- Ցուցադրել օգնությունը.:

`Projucer --help`
