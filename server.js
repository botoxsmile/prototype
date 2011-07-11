var host = '0.0.0.0';
var port = process.env.C9_PORT;

var express = require('express'),
    app=express.createServer();

app.configure(function(){
    app.use(express.methodOverride());
    app.use(express.bodyParser());
    app.use(app.router);
});

app.get('/', function(req, res){
  res.send('Hello world');
});

app.post('/', function(req, res) {
  now = new Date();
  console.log(now.toTimeString(),'-',req.method,'-',req.header('Content-Length'),'-',req.body);
  res.header('Content-Type', 'text/plain');
  res.send('POST ok');
});

app.listen(port);
console.log('Server running...');
