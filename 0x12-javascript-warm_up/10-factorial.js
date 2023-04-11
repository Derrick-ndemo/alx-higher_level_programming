#!/usr/bin/node

function factorial (val) {
    return val === 0 || isNaN(val) ? 1 : val * factorial(val - 1);
}

console.log(factorial(Number(process.argv[2])));
