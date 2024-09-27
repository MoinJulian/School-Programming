function convertStringToAscii(input) {
    var output = "";
    for (var i = 0; i < input.length; i++) {
        output += input.charCodeAt(i) + " ";
    }
    return output;
}
function convertAsciiToString(input) {
    var output = "";
    var asciiArray = input.split(" ");
    for (var _i = 0, asciiArray_1 = asciiArray; _i < asciiArray_1.length; _i++) {
        var element = asciiArray_1[_i];
        output += String.fromCharCode(parseInt(element));
    }
    return output;
}
var input = "Hello world";
var ascii = convertStringToAscii(input);
var ascii_2 = "72 101 108 108 111 32 119 111 114 108 100";
var string = convertAsciiToString(ascii_2);
console.log(ascii);
console.log(string);
