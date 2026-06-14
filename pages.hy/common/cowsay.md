# կովսեյ

> Տպել ASCII արվեստը (լռելյայն կով) ինչ-որ բան ասելով կամ մտածելով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/cowsay>:.

- Տպեք ASCII կով, որն ասում է «բարև, աշխարհ».:

`cowsay "{{hello, world}}"`

- Տպեք ASCII կով, որն ասում է տեքստ `stdin`-ից.:

`echo "{{hello, world}}" | cowsay`

- Թվարկեք արվեստի բոլոր առկա տեսակները.:

`cowsay -l`

- Տպեք նշված ASCII արվեստը՝ ասելով «բարև, աշխարհ».:

`cowsay -f {{art}} "{{hello, world}}"`

- Տպեք մեռած մտածող ASCII կով.:

`cowthink -d "{{I'm just a cow, not a great thinker...}}"`

- Տպեք ASCII կովը հատուկ աչքերով, ասելով «բարև աշխարհ»:

`cowsay -e {{characters}} "{{hello, world}}"`
