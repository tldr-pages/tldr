# կռունկի վավերացում

> Հաստատեք, որ պատկերը լավ ձևավորված է:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>:.

- Վավերացնել պատկերը.:

`crane validate`

- Բաց թողնել շերտերի ներբեռնումը/մարսումը.:

`crane validate --fast`

- Հեռավոր պատկերի անվանումը վավերացնելու համար.:

`crane validate --remote {{image_name}}`

- Ճանապարհ դեպի tarball՝ վավերացնելու համար.:

`crane validate --tarball {{path/to/tarball}}`

- Ցուցադրել օգնությունը.:

`crane validate {{[-h|--help]}}`
