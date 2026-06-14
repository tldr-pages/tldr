# wpscan

> WordPress-ի խոցելիության սկաներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/wpscanteam/wpscan>:.

- Թարմացրեք խոցելիության տվյալների բազան.:

`wpscan --update`

- Սկանավորեք WordPress կայք.:

`wpscan --url {{url}}`

- Սկանավորեք WordPress կայք՝ օգտագործելով պատահական օգտագործողի գործակալներ և պասիվ հայտնաբերում.:

`wpscan --url {{url}} --stealthy`

- Սկանավորեք WordPress-ի վեբկայքը՝ ստուգելով խոցելի հավելումները և նշելով դեպի `wp-content` գրացուցակի ուղին.:

`wpscan --url {{url}} --enumerate {{vp}} --wp-content-dir {{remote/path/to/wp-content}}`

- Սկանավորեք WordPress կայքը վստահված անձի միջոցով.:

`wpscan --url {{url}} --proxy {{protocol://ip:port}} --proxy-auth {{username:password}}`

- Կատարեք օգտվողի նույնացուցիչների թվարկում WordPress կայքում.:

`wpscan --url {{url}} --enumerate {{u}}`

- Կատարեք գաղտնաբառի գուշակման հարձակում WordPress կայքի վրա.:

`wpscan --url {{url}} --usernames {{username|path/to/usernames.txt}} --passwords {{path/to/passwords.txt}} threads {{20}}`

- Սկանավորեք WordPress կայքը՝ հավաքելով խոցելիության տվյալները WPVulnDB-ից (<https://wpvulndb.com/>):

`wpscan --url {{url}} --api-token {{token}}`
