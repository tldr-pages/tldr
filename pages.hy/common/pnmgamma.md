# pnmgamma

> Կատարեք գամմա ուղղում PNM պատկերների վրա:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmgamma.html>:.

- Փոխակերպեք պատկերը BT.709 պայծառությունից դեպի պայծառություն կամ sRGB լուսավորություն:

`pnmgamma -{{bt709tolinear|bt709tosrgb}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Փոխակերպեք պատկերը պայծառությունից կամ sRGB պայծառությունից BT.709 պայծառության:

`pnmgamma -{{lineartobt709|srgbtobt709}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Նշեք գամմայի արժեքը, որն օգտագործվում է գամմա փոխանցման ֆունկցիայի համար.:

`pnmgamma {{[-ga|-gamma]}} {{value}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Նշեք գամմա արժեքը, որն օգտագործվում է գամմա փոխանցման ֆունկցիայի համար մեկ գունավոր բաղադրիչի համար.:

`pnmgamma {{[-rg|-rgamma]}} {{value}} {{[-gg|-ggamma]}} {{value}} {{[-bg|-bgamma]}} {{value}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
