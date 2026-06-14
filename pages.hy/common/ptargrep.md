# ptargrep

> Գտեք `regex` նախշեր `.tar` արխիվային ֆայլերում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/ptargrep>:.

- Որոնեք օրինակ մեկ կամ ավելի `.tar` արխիվներում.:

`ptargrep "{{search_pattern}}" {{path/to/file1 path/to/file2 ...}}`

- Արխիվից հանեք ընթացիկ գրացուցակ՝ օգտագործելով ֆայլի բազային անունը.:

`ptargrep {{[-b|--basename]}} "{{search_pattern}}" {{path/to/file}}`

- Որոնել `.tar` արխիվում համապատասխան օրինաչափություն՝:

`ptargrep {{[-i|--ignore-case]}} "{{search_pattern}}" {{path/to/file}}`
