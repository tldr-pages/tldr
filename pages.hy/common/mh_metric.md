# mh_metric

> Հաշվարկել և կիրառել կոդերի չափումներ MATLAB-ի կամ Octave կոդի համար:.
> Լրացուցիչ տեղեկություններ. <https://florianschanda.github.io/miss_hit/metrics.html>:.

- Տպեք նշված ֆայլերի կոդի չափումները.:

`mh_metric {{path/to/file1.m path/to/file2.m ...}}`

- Տպեք կոդի չափումները նշված Octave ֆայլերի համար.:

`mh_metric --octave {{path/to/file1.m path/to/file2.m ...}}`

- Տպեք նշված գրացուցակի կոդի չափումները ռեկուրսիվ կերպով.:

`mh_metric {{path/to/directory}}`

- Տպեք ընթացիկ գրացուցակի կոդի չափումները.:

`mh_metric`

- Տպեք կոդի չափման հաշվետվությունը HTML կամ JSON ձևաչափով.:

`mh_metric --{{html|json}} {{path/to/output_file}}`
