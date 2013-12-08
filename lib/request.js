var request = require('request');
var repo = require('./repo');

exports.get = function(command, done) {
  // TODO: add local disk cache that respects HTTP headers
  // for example https://github.com/matteoagosti/node-request-caching
  request.get(repo.url(command), function(err, res, body) {
    if (err || res.statusCode != 200) {
      done(command + ' command not available');
    } else {
      done(null, body);
    }
  })
};
