let arr=[1,2,3,4,55,1,2,44,75,333,789,99,68];

let x=arr

console.log(x.sort());

arr.sort(function(a,b){
    return a-b;
    // to sort decending do return b-a  
});
console.log(arr);

let result=arr.reduce(function(acc,el,idx,arr){
    result (acc+=el);
},0);
