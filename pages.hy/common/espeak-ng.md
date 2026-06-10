# espeak-ng

> Բազմալեզու ծրագրային խոսքի սինթեզատոր:.
> Տես նաև՝ `speak-ng`, `espeak`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/espeak-ng/espeak-ng/blob/master/src/espeak-ng.1.ronn>:.

- Բարձրաձայն ասա մի արտահայտություն.:

`espeak-ng "{{text}}"`

- Խոսեք տեքստ `stdin`-ից.:

`echo "{{text}}" | espeak-ng`

- Խոսեք [f] ֆայլի բովանդակությունը.:

`espeak-ng -f {{path/to/file}}`

- Խոսեք հատուկ [v]ձայնով.:

`espeak-ng -v {{voice}} "{{text}}"`

- Խոսեք որոշակի [s] արագությամբ (կանխադրվածը 175 է) և [p]itch (կանխադրվածը 50 է):

`espeak-ng -s {{speed}} -p {{pitch}} "{{text}}"`

- Արտադրեք աուդիոը [w]AV ֆայլ՝ այն ուղղակիորեն խոսելու փոխարեն.:

`espeak-ng -w {{path/to/output.wav}} "{{text}}"`

- Թվարկեք բոլոր հասանելի ձայները.:

`espeak-ng --voices`
