# git stamp

> Az utolsó commit üzenet bélyegzése, a hibakövetőből való hivatkozással a problémák számára, vagy a felülvizsgálat oldalára való hivatkozással. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-stamp>.

- Bélyegezze le az utolsó commit üzenetet, hivatkozva a hibakövető rendszerben található problémaszámmal:

`git stamp {{issue_number}}`

- Bélyegezze le az utolsó commit üzenetet, hivatkozva annak felülvizsgálati oldalára:

`git stamp {{Review https://example.org/path/to/review}}`

- Bélyegezze le az utolsó commit üzenetet, amely a korábbi issue-eket egy újjal helyettesíti:

`git stamp --replace {{issue_number}}`
