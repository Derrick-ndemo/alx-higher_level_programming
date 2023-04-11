#!/usr/bin/node

/*
 * Script that prints the first argumet passed to it
 * */

const [arg] = process.argv.slice(2);

if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
