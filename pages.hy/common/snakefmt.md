# snakefmt

> Ձևաչափեք Snakemake ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/snakemake/snakefmt#usage>:.

- Ձևաչափեք հատուկ Snafile-ը.:

`snakefmt {{path/to/snakefile}}`

- Ձևաչափեք բոլոր Snakefiles-ը ռեկուրսիվորեն որոշակի գրացուցակում.:

`snakefmt {{path/to/directory}}`

- Ձևաչափեք ֆայլը հատուկ կազմաձևման ֆայլի միջոցով.:

`snakefmt --config {{path/to/config.toml}} {{path/to/snakefile}}`

- Ձևաչափեք ֆայլը, օգտագործելով որոշակի առավելագույն տողի երկարությունը.:

`snakefmt --line-length {{100}} {{path/to/snakefile}}`

- Ցուցադրել փոփոխությունները, որոնք կկատարվեն առանց դրանք կատարելու (չոր գործարկում).:

`snakefmt --diff {{path/to/snakefile}}`
