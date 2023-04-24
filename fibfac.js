// sookseon :: Jasmine Yuen, April Li
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2023-04-04t
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.

function fact(num) {
    answer = num;
    while (num > 2) {
        answer = answer * (num-1);
        num --;
    }
    return answer; 
}

fact(1); 
fact(2);
fact(3);
fact(4);
fact(5); 

function fib(num) {
    if (num < 2){
        return num;
    } else {
        return (fib(n-2) + fib(n-1));
    }
}

fib(1);
fib(2);
fib(3);
fib(4);
fib(5);