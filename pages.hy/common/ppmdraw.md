# ppmdraw

> PPM պատկերի վրա գծեր, տեքստ և ավելին գծիր՝ կատարելով սցենար:.
> Օգտագործված սկրիպտավորման լեզվի վերաբերյալ փաստաթղթերը կարելի է գտնել՝ հետևելով ստորև նշված հղմանը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmdraw.html>:.

- Նկարեք նշված PPM պատկերի վրա՝ գործարկելով տրամադրված սցենարը.:

`ppmdraw -script '{{setpos 50 50; text_here "hello!"; }}' {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Նկարեք նշված PPM պատկերի վրա՝ գործարկելով սկրիպտը նշված ֆայլում.:

`ppmdraw -scriptfile {{path/to/script}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
