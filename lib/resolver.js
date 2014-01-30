var request = require('./request');
var cache   = require('./cache');
var os      = require('os');
var async   = require('async');

var osDirectories = {
    darwin  : 'osx',
    linux   : 'linux',
    sunos   : 'sunos'
};

function path(command, platform) {
  return (platform || osDirectories[os.platform()]) + '/' + command + '.md';
}

function getForPlatform(repository, command, platform, done) {
  var pathCommon = path(command, "common");
  var pathPlatform = path(command, platform);

  async.parallel([
    function(callback) {
      repository.get(pathCommon, function() { callback(null, arguments); });
    },
    function(callback) {
      repository.get(pathPlatform, function() { callback(null, arguments); });
    }
  ], function(err, results){
    var errCommon = results[0][0];
    var errPlatform = results[1][0];
    var contentsCommon = results[0][1];
    var contentsPlatform = results[1][1];
    if(errCommon && errPlatform) {
      done([errCommon, errPlatform].join('\n'));
    } else {
      done(null, contentsPlatform || contentsCommon);
    }
  });

}

exports.get = function(command, options, done) {
  options = options || {};
  var resolver = this;
  resolver.getLocal(command, options.os, function(err, contents) {
    if (err) {
      resolver.getRemote(command, options.os, done);
    } else {
      done(null, contents);
    }
  });
};

exports.getLocal = function(command, platform, done) {
  getForPlatform(cache, command, platform, done);
};

exports.getRemote = function(command, platform, done) {
  getForPlatform(request, command, platform, done);
};
