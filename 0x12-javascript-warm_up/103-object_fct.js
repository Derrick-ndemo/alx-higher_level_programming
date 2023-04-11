#!/usr/bin/node

const obj = {
  type: 'object',
  value: 12
};

console.log(obj);
obj.increase =() => { obj.value += 1; };
obj.increase();
console.log(obj);
obj.increase();
console.log(obj);
obj.increase();
console.log(obj);
