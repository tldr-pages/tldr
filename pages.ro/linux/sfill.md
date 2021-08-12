# sfill

> Suprascrieți în siguranță spațiul liber și inodele partiției în care se află directorul specificat.
> Mai multe informaţii: <https://manned.org/sfill>

- Suprascrie spațiul liber și inodele unui disc cu 38 de scrieri (lent, dar sigur):

`sfill {{/path/to/mounted_disk_directory}}`

- Suprascrie spațiul liber și inodele unui disc cu 6 scrieri (rapid, dar mai puțin sigur) și arată starea:

`sfill -l -v {{/path/to/mounted_disk_directory}}`

- Suprascrie spațiul liber și inodele unui disc cu 1 scriere (foarte rapidă, dar nesigură) și arată starea:

`sfill -ll -v {{/path/to/mounted_disk_directory}}`

- Suprascrie doar spațiul liber al unui disc:

`sfill -I {{/path/to/mounted_disk_directory}}`

- Suprascrie numai inodele libere ale unui disc:

`sfill -i {{/path/to/mounted_disk_directory}}`
