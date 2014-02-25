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

exports.getPaths = function(opts, done) {
  var options = {
    url : "https://api.github.com/repos/rprieto/tldr/contents/pages",
    headers : {
      "User-Agent" : "tldr-puller"
    }
  };
  if (opts.github) {
    var parts = opts.github.split(":");
    if (parts.length === 2) {
      options.auth = {
        "user" : parts[0],
        "password" : parts[1]
      };
    }
  }
  request.get(options, function(err, res, body) {
    if (err) {
      done('tldr not available (check your internet connection)');
    } else if (res.statusCode != 200) {
      console.log("body: " + body);
      console.log("status: " + res.status);
      done('Could not enumerate pages (did you change the structure of the repo?)');
    } else {
      done(null, JSON.parse(body));
    }
  });
}

exports.getFiles = function(opts, done) {
  var options = {
    url : "https://api.github.com/repos/rprieto/tldr/contents/pages/"+opts.name,
    headers : {
      "User-Agent" : "tldr-puller"
    }
  };
  if (opts.github) {
    var parts = opts.github.split(":");
    if (parts.length === 2) {
      options.auth = {
        "user" : parts[0],
        "password" : parts[1]
      };
    }
  }
  request.get(options, function(err, res, body) {
    if (err) {
      done('tldr not available (check your internet connection)');
    } else if (res.statusCode != 200) {
      done('Could not enumerate files (did you change the structure of the repo?)');
    } else {
      done(null, JSON.parse(body));
    }
  });
}

function cachePath(path, contents, done) {
  cache.save(path, contents, function(err) {
    done(null, contents);
  });
}
