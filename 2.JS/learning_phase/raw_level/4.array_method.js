// map,filter,sort,every,some,reduce

let arr=[1,2,3,4];

let newArr=[];

for (let i=0 ;i<arr.length;i++){
    newArr.push(arr[i]**2);
};
console.log(newArr);
let newArr1=[]

newArr1=arr.map(function(elem,idx,arr){
//    console.log(elem);
     return elem **2;
})
 console.log(newArr1);
 


 