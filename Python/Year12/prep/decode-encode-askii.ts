function convertStringToAscii(input: string) {
    let output = "";
    for (let i = 0; i < input.length; i++) {
        output += input.charCodeAt(i) + " ";
    }
    return output;
}

function convertAsciiToString(input: string) {
    let output: string = "";
    let ascii_array: string[] = input.split(" ");
    for (const element of ascii_array) {
        output += String.fromCharCode(parseInt(element));
    }
    return output;
}

let input = "Hello world";
let ascii = convertStringToAscii(input);

let ascii_2 = "72 101 108 108 111 32 119 111 114 108 100"
let string = convertAsciiToString(ascii_2);

console.log("Input converted to ascii: " + ascii);
console.log("Ascii converted back to string: " + string);