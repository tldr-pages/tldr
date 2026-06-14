#մանիմ

> Մաթեմատիկական բացատրական տեսանյութերի անիմացիոն շարժիչ:.
> Լրացուցիչ տեղեկություններ. <https://docs.manim.community/en/stable/tutorials/quickstart.html>:.

- Պատկերացրեք տեսարան Python սցենարից՝ օգտագործելով լռելյայն կարգավորումները.:

`manim {{path/to/file.py}} {{SceneName}}`

- Պատկերացրեք ուղիղ նախադիտմամբ (ավտոմատ բացում է վիդեո ֆայլը ցուցադրումից հետո).:

`manim {{[-pql|--preview --quality low]}} {{path/to/file.py}} {{SceneName}}`

- Վերարտադրել բարձր որակով (1080p 60fps):

`manim {{[-pqh|--preview --quality high]}} {{path/to/file.py}} {{SceneName}}`

- Նշեք մաքսային ելքային ֆայլի անունը.:

`manim {{[-o|--output_file]}} {{output_file_name}} {{path/to/file.py}} {{SceneName}}`

- Ներկայացրեք՝ օգտագործելով որոշակի լուծաչափ և կադրային արագություն.:

`manim {{[-r|--resolution]}} {{1920,1080}} --fps {{60}} {{path/to/file.py}} {{SceneName}}`

- Թվարկեք հասանելի տեսարանները ֆայլում առանց մատուցման.:

`manim --list_scenes {{path/to/file.py}}`

- Ցուցադրել օգնությունը.:

`manim --help`
