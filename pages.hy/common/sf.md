#սֆ

> Հրամանի տող հզոր ինտերֆեյս, որը հեշտացնում է զարգացումը և կառուցման ավտոմատացումը ձեր Salesforce կազմակերպության հետ աշխատելիս:.
> Լրացուցիչ տեղեկություններ. <https://developer.salesforce.com/tools/salesforcecli>:.

- լիազորել Salesforce կազմակերպությանը.:

`sf force:auth:web:login --setalias {{organization}} --instanceurl {{organization_url}}`

- Նշեք բոլոր լիազորված կազմակերպությունները.:

`sf force:org:list`

- Բացեք որոշակի կազմակերպություն լռելյայն վեբ դիտարկիչում.:

`sf force:org:open --targetusername {{organization}}`

- Ցուցադրել տեղեկատվություն կոնկրետ կազմակերպության մասին.:

`sf force:org:display --targetusername {{organization}}`

- Աղբյուրի մետատվյալները փոխանցեք կազմակերպությանը.:

`sf force:source:push --targetusername {{organization}}`

- Քաղեք աղբյուրի մետատվյալները Կազմակերպությունից.:

`sf force:source:pull --targetusername {{organization}}`

- Ստեղծեք գաղտնաբառ կազմակերպության մուտք գործած օգտվողի համար.:

`sf force:user:password:generate --targetusername {{organization}}`

- Կազմակերպության մուտք գործած օգտվողի համար նշանակեք թույլտվությունների հավաքածու.:

`sf force:user:permset:assign --permsetname {{permission_set_name}} --targetusername {{organization}}`
