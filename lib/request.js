var request = require('request');
var cache   = require('./cache');
var config  = require('./config');

if(config.proxy){
  request = request.defaults({'proxy':config.proxy});
}

exports.get = function(path, done) {
 request.get(config.remote.url+"/"+path, function(err, res, body){
    if (err) {
      done('tldr not available (check your internet connection)');
    } else if (res.statusCode != 200) {
      done(path + ' documentation is not available\n' +
        'Consider contributing Pull Request to https://github.com/rprieto/tldr');
    } else {
      cachePath(path, body, done);
    }
 });
}

function cachePath(path, contents, done) {
  cache.save(path, contents, function(err) {
    done(null, contents);
  });
}
