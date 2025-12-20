const characters = [
    {
        name: 'Luke Skywalker',
        height: '172',
        mass: '77',
        eye_color: 'blue',
        gender: 'male',
    },
    {
        name: 'Darth Vader',
        height: '202',
        mass: '136',
        eye_color: 'yellow',
        gender: 'male',
    },
    {
        name: 'Leia Organa',
        height: '150',
        mass: '49',
        eye_color: 'brown',
        gender: 'female',
    },
    {
        name: 'Anakin Skywalker',
        height: '188',
        mass: '84',
        eye_color: 'blue',
        gender: 'male',
    },
];
 

// getting all names from charecter
// let names;

let names=characters.map(function(el){
    return el.name;
});
console.log(names);

let nameAndHeight=characters.map(function(el){
    return {
        name : el.name,
        height:el.height,
    }
})
console.log(nameAndHeight);

// getting an array of all first name

let firstName=characters.map(function(el){
    let temp=el.name.split(" ");
    return temp[0];
})
console.log(firstName);

// map(function(elments,index,array) thi map function taakes 3 arguments

// filter function
// one mejor problem with map function is it creats an array with same length of existing one

// to avoid this problem we use filter function

let numArr=[2,3,4,5,56,55,33,232,44,45,3566,98];
let evenArr=numArr.filter(function(el,idx,arr){
    if (el%2==0) return el;
})
// map and filter if any condition use filter

console.log(evenArr);

// get mass >100

let greate100=characters.filter(function(el){
    if (el.mass>100) return el;
});

console.log(greate100);


// returning male gender

let newGen=characters.filter(function(el){
    if (el.gender=='male') return el
})
console.log(newGen);


