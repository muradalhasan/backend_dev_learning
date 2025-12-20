// every,some methods

let arr=[3,4,5,6];
//every(everythig) and some(at least one) return bolean value
 

let allEven=arr.every(function(el,idx,arr){
    return el%2==0;
})

console.log(allEven);


