#խոսել-նգ

> Բազմալեզու ծրագրային խոսքի սինթեզատոր:.
> Տես նաև՝ `espeak-ng`, `espeak`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/espeak-ng/espeak-ng/blob/master/src/speak-ng.1.ronn>:.

- Բարձրաձայն ասա մի արտահայտություն.:

`speak-ng "{{text}}"`

- Խոսեք տեքստ `stdin`-ից.:

`echo "{{text}}" | speak-ng`

- Խոսեք [f] ֆայլի բովանդակությունը.:

`speak-ng -f {{path/to/file}}`

- Խոսեք հատուկ [v]ձայնով.:

`speak-ng -v {{voice}} "{{text}}"`

- Խոսեք որոշակի [s] արագությամբ (կանխադրվածը 175 է) և [p]itch (կանխադրվածը 50 է):

`speak-ng -s {{speed}} -p {{pitch}} "{{text}}"`

- Արտադրեք աուդիոը [w]AV ֆայլ՝ այն ուղղակիորեն խոսելու փոխարեն.:

`speak-ng -w {{path/to/output.wav}} "{{text}}"`

- Թվարկեք բոլոր հասանելի ձայները.:

`speak-ng --voices`
