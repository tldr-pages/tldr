# doctl տվյալների բազաներ db

> Կառավարեք տվյալների բազաները, որոնք սպասարկվում են տվյալների բազայի կլաստերի կողմից:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/db/>:.

- Գործարկեք `doctl databases db` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} db {{command}} {{[-t|--access-token]}} {{access_token}}`

- Վերցրեք տվյալ տվյալների բազայի անունը, որը տեղակայված է տվյալ տվյալների բազայի կլաստերում.:

`doctl {{[d|databases]}} db {{[g|get]}} {{database_id}} {{database_name}}`

- Թվարկեք առկա տվյալների բազաները, որոնք տեղակայված են տվյալների բազայի տվյալ կլաստերում.:

`doctl {{[d|databases]}} db {{[ls|list]}} {{database_id}}`

- Տվյալ տվյալների բազայի կլաստերում ստեղծել տվյալ անունով տվյալների բազա.:

`doctl {{[d|databases]}} db {{[c|create]}} {{database_id}} {{database_name}}`

- Ջնջել տվյալների բազան տվյալ անունով տվյալների բազայի կլաստերի մեջ.:

`doctl {{[d|databases]}} db {{[rm|delete]}} {{database_id}} {{database_name}}`
