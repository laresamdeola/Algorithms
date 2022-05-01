/*
Create a function that takes an integer as an argument and
returns "Even" for even numbers or "Odd" for odd numbers.
*/

/*
function even_or_odd(number) {
  return number % 2 == 0 ? 'Even' : 'Odd';
}

*/


function findUniq(arr) {
  console.log(arr.map((a,b) => { if(a != b){ return a } }))
}

findUniq([ 1, 0, 0 ])