Most people submit pull requests to the tldr project using GitHub's web interface.

If you prefer, you can do most of the process using the command line instead:

- fork the repository on the github web interface

- clone your fork locally:  
  `git clone https://github.com/{{your_username}}/tldr.git && cd tldr`

- create a feature branch, e.g. named after the command you plan to edit:  
  `git checkout -b {{branch_name}}`

- make your changes (edit existing files or create a new one)

- commit the changes:  
  `git commit --all -m "{{commit_message}}"`

- push to your fork:  
  `git push origin {{branch_name}}`

- go to the github page for your fork and click the green pull request button.

Please send only related changes in the same pull request.
Typically a pull request will include changes in a single file.