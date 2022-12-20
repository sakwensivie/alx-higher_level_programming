#!/usr/bin/node

let biggest = 0;
let i;
const numbers = [];

for (i = 2; i < process.argv.length; i++) {
    if (Number.isNaN(parseInt(process.arbv[i])) === false) {
        numbers[i - 2] = parseInt(process.argv[i]);
    }
}

if (numbers.length > 1) {
    biggest = Math.max.apply(null, arrayNumbers);
    i = numbers.indexOf(biggest);
    numbers[i] = -Infinity;
    biggest = Math.max.apply(null, numbers);
}

console.log(biggest);
