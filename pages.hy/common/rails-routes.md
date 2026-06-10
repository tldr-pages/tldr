# ռելսային երթուղիներ

> Նշեք երթուղիները Rails հավելվածում:.
> Լրացուցիչ տեղեկություններ. <https://guides.rubyonrails.org/routing.html>:.

- Նշեք բոլոր երթուղիները.:

`rails routes`

- Թվարկեք բոլոր երթուղիները ընդլայնված ձևաչափով.:

`rails routes {{[-E|--expanded]}}`

- Ցուցակե՛ք URL-ի օգնականի մեթոդի անունը, HTTP բայը կամ URL ուղին մասամբ համապատասխանող երթուղիները.:

`rails routes {{[-g|--grep]}} {{posts_path|GET|/posts}}`

- Թվարկեք երթուղիները, որոնք քարտեզագրվում են նշված վերահսկիչին.:

`rails routes {{[-c|--controller]}} {{posts|Posts|Blogs::PostsController}}`
