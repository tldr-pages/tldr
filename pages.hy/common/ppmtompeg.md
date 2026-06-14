# ppmtompeg

> Կոդավորեք MPEG-1 հոսքը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtompeg.html>:.

- Արտադրեք MPEG-1 հոսք՝ օգտագործելով պարամետրային ֆայլը՝ մուտքերը և ելքերը նշելու համար.:

`ppmtompeg {{path/to/parameter_file}}`

- Կոդավորեք GOP-ը միայն նշված համարով.:

`ppmtompeg {{[-g|-gop]}} {{gop_num}} {{path/to/parameter_file}}`

- Նշեք կոդավորման առաջին և վերջին շրջանակը.:

`ppmtompeg {{[-fr|-frames]}} {{first_frame}} {{last_frame}} {{path/to/parameter_file}}`

- Միավորել բազմաթիվ MPEG շրջանակներ մեկ MPEG-1 հոսքի մեջ.:

`ppmtompeg -combine_frames {{path/to/parameter_file}}`
