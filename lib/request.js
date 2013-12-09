var request = require('request');
var cache   = require('./cache');
var remote  = require('./remote');

exports.get = function(command, done) {
  cache.get(command + '.md', function(err, contents) {
    if (err) {
      getRemote(command, done);
    } else {
      done(null, contents);
    }
  });
};

function getRemote(command, done) {
  var url = remote.url(command);
  request.get(url, function(err, res, body) {
    if (err) {
      done('tldr not available (check your internet connection)');
    } else if (res.statusCode != 200) {
      done(command + ' command not available');
    } else {
      cache.save(command + '.md', body, function(err) {
        done(null, body);
      });
    }
  });
}
