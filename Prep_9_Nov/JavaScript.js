let sum = 0;
let count = 0;

while (count < 5) {
  let number = Math.random() * 100;
  console.log(number);

  sum = sum + number;
  count++;
}

console.log(sum);
