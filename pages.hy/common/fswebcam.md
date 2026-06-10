# fswebcam

> Փոքր և պարզ վեբ-տեսախցիկ *nix-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.sanslogic.co.uk/fswebcam/>:.

- Նկարիր.:

`fswebcam {{filename}}`

- Լուսանկարեք հատուկ լուծաչափով.:

`fswebcam {{[-r|--resolution]}} {{width}}x{{height}} {{filename}}`

- Լուսանկարեք ընտրված սարքից (կանխադրված է `/dev/video0`):

`fswebcam {{[-d|--device]}} {{device}} {{filename}}`

- Լուսանկարեք ժամանակի դրոշմակնիքով (ժամանականիշի տողը ձևաչափված է strftime-ով):

`fswebcam --timestamp {{timestamp}} {{filename}}`
