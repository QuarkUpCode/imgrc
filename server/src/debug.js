// export {verbosity, debug, warn, err};


var verbosity = 2;

function debug(str){
	if(verbosity>=2){
		console.log(str);
	}
}

function warn(str){
	if(verbosity>=1){
		console.log("\x1b[42m", str, "\x1b[0m");
	}
}

function err(str){
	if(verbosity>=0){
		console.log(str);
	}
}

