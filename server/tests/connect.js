const WebSocket = require("ws");

let socket = new WebSocket("ws://127.0.0.1:4433");
socket.onopen = ()=>{
	console.log("connected");
};

socket.onmessage = (msg)=>{
	// console.log(msg);
	// console.log(Buffer.from(msg).toString());
	// console.log(msg.data);
	console.log(JSON.parse(msg.data));
};