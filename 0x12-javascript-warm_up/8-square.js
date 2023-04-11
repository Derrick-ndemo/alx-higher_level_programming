#!/usr/bin/node

const x = Number(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let res = '';
    for (let j = 0; j < x; j++) {
      res += 'x';
	}
	console.log(res);
  }
}
