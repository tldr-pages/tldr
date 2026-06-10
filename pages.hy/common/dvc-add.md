# dvc ավելացնել

> Ավելացրեք փոփոխված ֆայլերը ինդեքսում:.
> Լրացուցիչ տեղեկություններ. <https://doc.dvc.org/command-reference/add>:.

- Ինդեքսում ավելացրեք մեկ թիրախային ֆայլ.:

`dvc add {{path/to/file}}`

- Ցուցակում ավելացրեք թիրախային գրացուցակ.:

`dvc add {{path/to/directory}}`

- Ռեկուրսիվ կերպով ավելացրեք բոլոր ֆայլերը տվյալ թիրախային գրացուցակում.:

`dvc add --recursive {{path/to/directory}}`

- Ավելացրեք թիրախային ֆայլ՝ հատուկ `.dvc` ֆայլի անունով.:

`dvc add --file {{custom_name.dvc}} {{path/to/file}}`
