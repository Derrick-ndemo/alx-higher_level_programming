#!/usr/bin/node

/*
 * Script that prints a message depending on the number of args passed
 * If only one argument is passed print "Argument found"
 * Otherwise print "Arguments found"
 * */

let myArgs = process.argv.length;

switch (myArgs) {
	case 0:
		console.log('No argument');
	case 1:
		console.log('Argument found');
		break;
	default:
		console.log('Arguments found');
}
