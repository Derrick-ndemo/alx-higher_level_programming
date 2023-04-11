#!/usr/bin/node

const nums = Number(process.argv[2]);
const nums1 = Number(process.argv[3]);
const size = process.argv.length - 2;
if (isNaN(nums) || size === 1 || isNaN(nums1)) {
  console.log('NaN');
} else {
  let res = (a, b) => a + b;
  console.log(res(nums, nums1));
}
