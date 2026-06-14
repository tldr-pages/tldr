# git check-ref-format

> Ստուգեք՝ արդյոք հղման անվանումն ընդունելի է, և դուրս եկեք ոչ զրոյական կարգավիճակով, եթե դա այդպես չէ:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-check-ref-format>:.

- Ստուգեք նշված տեղեկանքի անվան ձևաչափը.:

`git check-ref-format {{refs/head/refname}}`

- Տպեք վերջին ստուգված մասնաճյուղի անունը.:

`git check-ref-format --branch @{-1}`

- Նորմալացնել վերանվանումը.:

`git check-ref-format --normalize {{refs/head/refname}}`
