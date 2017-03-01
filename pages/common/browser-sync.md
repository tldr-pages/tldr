#  browser-sync

>  Starts local server that updates browser on file changes  

-  Start a server from the DIR directory:

`browser-sync start --server {{DIR}} --files {{DIR}}`

-  Start a server from local directory, watching css file in DIR:

`browser-sync start --server --files {{DIR/style.css}}`

-  Create configuration file:

`browser-sync init`

-  Start browser-sync from config file:

`browser-sync start --config {{config_file}}`
