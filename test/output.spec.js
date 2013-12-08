var should = require('should');
var output = require('../lib/output');

describe('Console output from Markdown', function() {
  
  it('strips paragraph tags', function() {
    var o = output.fromMarkdown(
      '\nline 1' +
      '\n' +
      '\nline 2' +
      '\n'
    );
    o.should.eql('line 1line 2');
  });

  it('prints bullet points in bold (command description)', function() {
    var o = output.fromMarkdown(
      '\n- archiving utility' +
      '\n- supports optional compression'
    );
    o.should.startWith('  ');
    o.should.include('\u001b[3m\u001b[1marchiving utility\u001b[22m\u001b[23m');
    o.should.include('\u001b[3m\u001b[1msupports optional compression\u001b[22m\u001b[23m');
  });
  
  it('adds a line break after the main description', function() {
    var o = output.fromMarkdown(
      '\n- archiving utility' +
      '\n- supports optional compression'
    );
    o.should.endWith('\n\n');
  });
  
  it('ignores all other Markdown syntax', function() {
    var o = output.fromMarkdown(
      '\n# heading 1' +
      '\n' +
      '\n### heading 3' +
      '\n' +
      '\n> quote' +
      '\n' +
      '\n```' +
      '\ncode block' +
      '\n```'
    );
    o.should.eql('');
  });


  
});
