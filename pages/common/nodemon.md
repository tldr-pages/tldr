# nodemon

> Automatically restart node application when watched files are changed.
> More information: <https://nodemon.io>.

- Watch a spesific file for reloads:

`nodemon --inspect filename.js`

- Manually restart nodemon (note nodemon must already be active for this to work):

`rs`

- Ignore specific files:

`nodemon --ignore filename.js`

- Pass arguments to your node application:

`nodemon yournodeargument`

- Running non-node scripts:

`nodemon --exec "python --verbose" filename.py`
