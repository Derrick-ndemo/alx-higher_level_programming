#!/usr/bin/node

const num = Number(process.argv[2]);

function factorial (val) {
    return val === 0 || isNaN(val) ? 1 : val * factorial(val - 1);
}


console.log(factorial(num));
