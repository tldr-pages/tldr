# պոչի սանդղակ

> Անձնական WireGuard ցանցային ծառայություն:.
> Որոշ ենթահրամաններ, ինչպիսիք են `up`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ՝ <https://tailscale.com/kb/1080/cli>:.

- Թույլ տվեք ընթացիկ օգտագործողին գործել Tailscale daemon-ի վրա.:

`sudo tailscale set --operator $USER`

- Միացեք Tailscale-ին.:

`tailscale up`

- Անջատեք Tailscale-ից.:

`tailscale down`

- Ցուցադրել Tailscale-ին միացված բոլոր սարքերը (իրենց IP հասցեներով).:

`tailscale status`

- Պինգ կատարեք գործընկերային հանգույց Tailscale շերտում և ցուցադրեք, թե որ երթուղին է անցել յուրաքանչյուր պատասխանի համար.:

`tailscale ping {{ip|hostname}}`

- Վերլուծեք տեղական ցանցի պայմանները և ցուցադրեք արդյունքը.:

`tailscale netcheck`

- Սկսեք վեբ սերվեր Tailscale daemon-ը կառավարելու համար.:

`tailscale web`

- Ցուցադրել համօգտագործվող նույնացուցիչ, որը կօգնի ախտորոշել խնդիրները.:

`tailscale bugreport`
