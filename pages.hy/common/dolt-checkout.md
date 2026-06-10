# dolt checkout

> Ստուգեք աշխատանքային ծառը կամ աղյուսակները ճյուղին կամ հանձնեք:.
> Լրացուցիչ տեղեկություններ. <https://docs.dolthub.com/cli-reference/cli#dolt-checkout>:.

- Անցում մասնաճյուղի.:

`dolt checkout {{branch_name}}`

- Չբեմադրված փոփոխությունները վերադարձնել աղյուսակ.:

`dolt checkout {{table}}`

- Ստեղծեք նոր մասնաճյուղ և անցեք դրան.:

`dolt checkout -b {{branch_name}}`

- Ստեղծեք նոր մասնաճյուղ՝ հիմնվելով նշված պարտավորության վրա և անցեք դրան.:

`dolt checkout -b {{branch_name}} {{commit}}`
