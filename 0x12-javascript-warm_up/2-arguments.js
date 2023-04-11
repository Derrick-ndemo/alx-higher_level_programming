#!/usr/bin/node

/*
 * Script that prints a message depending on the number of args passed
 * If only one argument is passed print "Argument found"
 * Otherwise print "Arguments found"
 * */

const myArgs = process.argv.length - 2;

switch (myArgs) {
  case 0:
    console.log('No argument');
    break;
  case 1:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
