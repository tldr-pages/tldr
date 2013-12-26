var ms   = require('ms');

function path() {
  if (process.env.NODE_ENV === 'development') {
    return './conf/local.json';
  }  else {
    return './conf/prod.json';
  }
}

var conf = require(path());

if (typeof(conf.remote.maxAge) === 'string') {
  conf.remote.maxAge = ms(conf.remote.maxAge) * 1000;
}

module.exports = conf;
