# numfmt

> Փոխարկել թվերը մարդու կողմից ընթեռնելի տողերի և դրանցից:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/numfmt-invocation.html>:.

- Փոխարկել 1.5K (SI միավորները) 1500:

`numfmt --from si 1.5K`

- Փոխարկել 1500-ը 1.5K-ի (SI միավորներ).:

`numfmt --to si 1500`

- Փոխարկել 1.5K (IEC միավորները) 1536:

`numfmt --from iec 1.5K`

- Օգտագործեք համապատասխան փոխակերպում, որը հիմնված է վերջածանցի վրա.:

`numfmt --from auto {{1.5Ki}}`

- Փոխակերպեք 5-րդ դաշտը (1-ինդեքսավորված) IEC միավորների՝ առանց վերնագրի վերափոխման.:

`ls -l | numfmt --header=1 --field 5 --to iec`

- Փոխակերպեք IEC միավորների, 5 նիշով պահոց, ձախից հավասարեցված.:

`du {{[-s|--summarize]}} * | numfmt --to iec --format "%-5f"`
