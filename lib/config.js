var ms   = require('ms');
var os   = require('os');
var path = require('path');

function configPath() {
  if (process.env.NODE_ENV === 'development') {
    return './conf/local.json';
  }  else {
    return './conf/prod.json';
  }
}

var conf = require(configPath());

if (typeof(conf.remote.maxAge) === 'string') {
  conf.remote.maxAge = ms(conf.remote.maxAge) * 1000;
}

conf.proxy = process.env.HTTP_PROXY || process.env.http_proxy;

var CACHE_FOLDER = path.join(os.tmpdir ? os.tmpdir() : os.tmpDir(), 'tldr-cache');
conf.local = conf.local || {};
conf.local.cacheFolder = conf.local.cacheFolder || CACHE_FOLDER;

module.exports = conf;
