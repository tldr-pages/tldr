# sg_raw

> Ուղարկեք կամայական SCSI հրամանը միացված սարքին:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sg_raw>:.

- Ուղարկեք հրաման օպտիկական SCSI սարքին, որը նշանակված է `sr0`-ին՝ մեդիան իր սկուտեղում բեռնելու համար.:

`sg_raw /dev/sr0 EA 00 00 00 00 01`

- Կարդացեք տվյալներ `IFILE`-ից՝ `stdin`-ի փոխարեն:

`sg_raw {{[-i|--infile]}} {{path/to/IFILE}} {{/dev/sgX}} {{scsi_command}}`

- Բաց թողեք մուտքագրված տվյալների առաջին `LEN` բայթը՝:

`sg_raw {{[-k|--skip]}} {{LEN}} {{/dev/sgX}} {{scsi_command}}`

- Կարդացեք `SLEN` բայթ տվյալներ և ուղարկեք սարքին՝:

`sg_raw {{[-s|--send]}} {{SLEN}} {{/dev/sgX}} {{scsi_command}}`

- Սպասեք մինչև `SEC` վայրկյան, մինչև `sg_raw` մշակումն ավարտվի:

`sg_raw {{[-t|--timeout]}} {{SEC}} {{/dev/sgX}} {{scsi_command}}`

- Բարձրացնել խոսակցական մակարդակը 1-ով:

`sg_raw {{[-v|--verbose]}} {{/dev/sgX}} {{scsi_command}}`

- Վերադարձված տվյալները թափեք երկուական ձևով.:

`sg_raw {{[-b|--binary]}} {{/dev/sgX}} {{scsi_command}}`

- Նշված սարքից ստացված տվյալները գրեք `OFILE`.:

`sg_raw {{[-o|--outfile]}} {{path/to/OFILE}} {{/dev/sgX}} {{scsi_command}}`
