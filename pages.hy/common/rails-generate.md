# ռելսեր են առաջացնում

> Ստեղծեք նոր Rails կաղապարներ գոյություն ունեցող նախագծում:.
> Լրացուցիչ տեղեկություններ. <https://guides.rubyonrails.org/command_line.html#bin-rails-generate>:.

- Թվարկեք բոլոր առկա գեներատորները.:

`rails generate`

- Ստեղծեք նոր մոդել, որը կոչվում է Post, ատրիբուտների վերնագրով և մարմնով.:

`rails generate model {{Post}} {{title:string}} {{body:text}}`

- Ստեղծեք նոր վերահսկիչ, որը կոչվում է Գրառումներ՝ գործողությունների ցուցիչով, ցուցադրելով, նորով և ստեղծեք.:

`rails generate controller {{Posts}} {{index}} {{show}} {{new}} {{create}}`

- Ստեղծեք նոր միգրացիա, որն ավելացնում է կատեգորիայի հատկանիշ գոյություն ունեցող Փոստ կոչվող մոդելին:

`rails generate migration {{AddCategoryToPost}} {{category:string}}`

- Ստեղծեք փայտամած Փոստ անունով մոդելի համար՝ նախապես սահմանելով ատրիբուտների անվանումը և մարմինը.:

`rails generate scaffold {{Post}} {{title:string}} {{body:text}}`
