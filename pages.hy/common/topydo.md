# topydo

> Անելիքների ցանկի ծրագիր, որն օգտագործում է todo.txt ձևաչափը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/topydo/topydo>:.

- Տվյալ համատեքստով կոնկրետ նախագծին անելիքներ ավելացրեք.:

`topydo add "{{todo_message}} +{{project_name}} @{{context_name}}"`

- Ավելացրեք վաղվա վերջնաժամկետ ունեցող անելիքներ՝ `A` առաջնահերթությամբ.:

`topydo add "(A) {{todo _message}} due:{{1d}}"`

- Ավելացրեք անելիքներ ուրբաթ օրվա վերջնաժամկետով.:

`topydo add "{{todo_message}} due:{{fri}}"`

- Ավելացրեք ոչ խիստ կրկնվող անելիք (հաջորդ ժամկետը = հիմա + rec):

`topydo add "water flowers due:{{mon}} rec:{{1w}}"`

- Ավելացրեք խիստ կրկնվող անելիքներ (հաջորդ ժամկետը = ընթացիկ ժամկետը + rec):

`topydo add "{{todo_message}} due:{{2020-01-01}} rec:{{+1m}}"`

- Վերադարձեք վերջին `topydo` կատարված հրամանը.:

`topydo revert`
