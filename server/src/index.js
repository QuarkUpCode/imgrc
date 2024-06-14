// const debug = require("./js");


var verbosity = 2;

function debug(str){
	if(verbosity>=2){
		console.log('', str, '');
	}
}

function warn(str){
	if(verbosity>=1){
		console.log("\x1b[32m", str, "\x1b[0m");
	}
}

function err(str){
	if(verbosity>=0){
		console.log("\x1b[35m", str, "\x1b[0m");
	}
}


const WebSocket = require("ws");

const WSport = 4433;


let sockets = [];
let naughty = [];

let publicURL = "";
let naughtyURL = "";

let publicSignature = "null";
let naughtySignature = "null";

let publicTimestamp = 0;
let naughtyTimestamp = 0;


// let imgConstData;
// let servedImageData;
// let imgTempData = [];

// let imgConst = "";
// let signatureConst = "";
// let timestampConst = 0;
// let tempcounter = 0;
// let imgTemp = "";
// let signatureTemp = "";
// let timestampTemp = 0;


(async () => {

	//sockets will be in ram
	//they could also be stored in a file and streamed
	
	const server = new WebSocket.Server({
		port: WSport,
	});
	
	// let sockets = [];
	// let sockchannels = [];

	server.on("connection", (socket, req)=>{
		debug("new connection");
		debug(sockets);
		sockets.push(socket);

		socket.on("message", async (msg) => {
			const messageContent = Buffer.from(msg).toString();
			if(messageContent.startsWith("naughty")){
				if(messageContent.indexOf("join") != -1){
					naughty.push(socket);
				}
				else if(messageContent.indexOf("leave") != -1){
					naughty = naughty.filter((s) => s!== socket);
				}
			}
		});
		socket.on("close", ()=>{
			sockets = sockets.filter((s)=>(s !== socket));
		});
	});


})();

// function sendConst(){
// 	debug(sockets);
// 	sockets.forEach(s=>{
// 		s.send(JSON.stringify({
// 			url: imgConst,
// 			duration: -1,
// 			signature: signatureConst,
// 			timestamp: timestampConst,
// 			tempcounter: tempcounter,
// 		}));
// 	});
// }


function sendUpdate(url, duration, signature, timestamp, origin, feed){
	debug(sockets);
	sockets.forEach(s=>{
		s.send(JSON.stringify({
			url: url,
			duration: duration,
			signature: signature,
			timestamp: timestamp,
			tempcounter: tempcounter,
			origin: origin,
			feed: feed,
		}));
	});
}



// setInterval(sendConst, 1000);

function timeoutTemp(){
	servedImageData = imgConstData;
	sendUpdate();
}


const http = require("http");

const port = 4432;

const MAX_FILE_SIZE = 10*1000*1000;
const MAX_TEMP_DURATION = 15;
const MAX_TEMP_QUEUE = 4;

const FEED_PUBLIC = "127.0.0.1:4432/feed/public";
const FEED_NAUGHTY = "127.0.0.1:4432/feed/naughty";

const server = http.createServer((req, res)=>{

	console.log(req);
	
	// if(req.headers["content-type"].startsWith("image/")){

	// }
	if(req.method == 'POST'){
		if(req.headers["content-type"].startsWith("image/")){
			let rawData = [];
			let totalSize = 0;
			
			req.on("data", (chunk)=>{
				console.log(chunk);
				totalSize = rawData.length;
				if(totalSize<= MAX_FILE_SIZE){
					rawData.push(chunk);
				}
				else{
					console.log("size :", totalSize);
					res.statusCode = 413;
					res.end("Fwile twoo bwig :3 :p");
					// req.destroy();
				}
			});

			req.on("end", ()=>{
				let feed = req.headers["Target-Feed"];
				if(feed != "public"){
					feed = "naughty";
				}
				let duration = req.headers["Image-Duration"];
				// console.log(duration);
				if(!duration) duration = -1;
				if(duration>MAX_TEMP_DURATION) duration=MAX_TEMP_DURATION;
				console.log(rawData);
				if(duration<0){
					// imgConstData = Buffer.concat(rawData);
				}
				else{
					// servedImageData = Buffer.concat(rawData);
					res.statusCode = 200;
					res.end();
					setTimeout(timeoutTemp, 1000*duration);
					// if(tempcounter<MAX_TEMP_QUEUE){
						// tempcounter++;
						// imgTempData.push([Buffer.concat(rawData, )])
					// }
				}
			});

		}
	}
	
	res.statusCode = 200;
	res.end();

});

server.listen(port, ()=>{
	debug("http server running (better catch it)");
});

// setInterval(()=>console.log(sockets), 1000);