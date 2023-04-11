#!/usr/bin/node

const nums = Number(process.argv[2]);
const num = Number(process.argv[3]);
const size = process.argv.length - 2;
if (isNaN(nums) || size === 1 || isNaN(num)) {
  console.log('NaN');
} else {
  let res = (a, b) => a + b;
  console.log(res(nums, num));
}
