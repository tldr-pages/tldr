var util = require('util');
var http = require('http');
var connect = require('connect');

if (process.env.NODE_ENV != 'development') {
  util.log('For local development only.');
  process.exit(1);
}

var port = process.env.PORT || 3000;
connect().use(connect.static(__dirname)).listen(port);
console.log('Local server listening on port ' + port);
