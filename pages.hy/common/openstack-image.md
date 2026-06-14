# openstack պատկեր

> OpenStack Image ծառայությունը, որը կոչվում է OpenStack Glance, թույլ է տալիս օգտվողներին վերբեռնել և հայտնաբերել տվյալների ակտիվներ, որոնք նախատեսված են այլ ծառայությունների հետ օգտագործելու համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.openstack.org/python-openstackclient/latest/cli/command-objects/image-v2.html>:.

- Ցուցակեք առկա պատկերները.:

`openstack image list {{--private|--shared|--all}}`

- Ցուցադրել պատկերի մանրամասները.:

`openstack image show --human-readable {{image_id}}`

- Ստեղծեք/վերբեռնեք պատկեր.:

`openstack image create --file {{path/to/file}} {{--private|--shared|--all}} {{image_name}}`

- Ջնջել պատկեր(ներ).:

`openstack image delete {{image_id1 image_id2 ...}}`

- Պահպանեք պատկերը տեղում.:

`openstack image save --file {{filename}} {{image_id}}`
