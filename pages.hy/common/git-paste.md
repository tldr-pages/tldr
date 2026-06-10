#git paste

> Ուղարկեք պարտավորություններ pastebin կայք՝ օգտագործելով `pastebinit`:.
> `git-extras`-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tj/git-extras/blob/main/Commands.md#git-paste>:.

- Ընթացիկ ճյուղի և դրա վերին հոսքի միջև ընկած հատվածներն ուղարկեք pastebin՝ օգտագործելով `pastebinit`:

`git paste`

- Փոխանցեք ընտրանքները `git format-patch`-ին, որպեսզի ընտրեք այլ կոմիտացիաներ (`@^`-ն ընտրում է `HEAD`-ի մայրը, և այդպիսով ուղարկվում է ընթացիկ ստուգված հանձնառությունը):

`git paste {{@^}}`
