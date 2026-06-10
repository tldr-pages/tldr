# odpscmd auth

> Օգտատիրոջ լիազորությունները ODPS-ում (Տվյալների մշակման բաց ծառայություն):.
> Տես նաև՝ `odpscmd`:.
> Լրացուցիչ տեղեկություններ. <https://www.alibabacloud.com/help/en/maxcompute/user-guide/maxcompute-client>:.

- [Ինտերակտիվ] Ավելացրեք օգտվող ընթացիկ նախագծին.:

`add user {{username}};`

- [Ինտերակտիվ] Օգտատիրոջը լիազորությունների մի շարք շնորհեք.:

`grant {{action_list}} on {{object_type}} {{object_name}} to user {{username}};`

- [Ինտերակտիվ] Ցույց տալ օգտվողի լիազորությունները.:

`show grants for {{username}};`

- [Ինտերակտիվ] Ստեղծեք օգտվողի դեր.:

`create role {{role_name}};`

- [Ինտերակտիվ] Տրամադրել լիազորությունների մի շարք դերի.:

`grant {{action_list}} on {{object_type}} {{object_name}} to role {{role_name}};`

- [Ինտերակտիվ] Նկարագրեք դերի լիազորությունները.:

`desc role {{role_name}};`

- [Ինտերակտիվ] Օգտատիրոջը դեր հատկացրեք.:

`grant {{role_name}} to {{username}};`
