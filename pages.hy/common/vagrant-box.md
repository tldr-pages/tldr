# թափառաշրջիկ տուփ

> Կառավարեք Vagrant տուփերը (վիրտուալ մեքենայի պատկերներ):.
> Տես նաև՝ `vagrant`:.
> Լրացուցիչ տեղեկություններ. <https://developer.hashicorp.com/vagrant/docs/cli/box>:.

- Նշեք բոլոր տեղադրված տուփերը.:

`vagrant box list`

- Ավելացնել նոր տուփ.:

`vagrant box add {{hashicorp/bionic64}}`

- Ավելացրեք տուփ հատուկ URL-ից.:

`vagrant box add {{my-box}} {{https://example.com/my-box.box}}`

- Հեռացրեք տեղադրված տուփը.:

`vagrant box remove {{hashicorp/bionic64}}`

- Թարմացրեք բոլոր տուփերը, որոնք օգտագործվում են ընթացիկ Vagrant միջավայրում.:

`vagrant box update`

- Թարմացրեք որոշակի տուփ.:

`vagrant box update --box {{bento/debian-12}}`

- Ստուգեք, արդյոք առկա է նոր տարբերակ ձեր օգտագործած տուփի համար.:

`vagrant box outdated`

- Մաքրել տեղադրված տուփերի հին տարբերակները.:

`vagrant box prune`
