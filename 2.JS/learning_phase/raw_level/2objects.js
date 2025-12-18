let person1={
    name: "asif",
    age:18,
    sayHello(){
        console.log(`Hello ${person1.name}`)
        // /acessing name using eithwr person1.name or this.name
    }
}
// person1.sayHello();

let person2={
    name: "mahfuz",
    age:22,
    sayHello(){
        console.log(`Hello ${person1.name}`)
        // /acessing name using eithwr person1.name or this.name
    }
}

// factory function
function ceatePerson(name,age){

    return {
        name:name,
        age:age,
        sayHello(){
            console.log(`hello ${this.name} your age ${this.age}`);
        },
    };
}
// let personA=ceatePerson("setu",18).sayHello();


// constructor function
 function CreatePerson(name,age){
    this.name=name;
    this.age=age;
    this.sayHello=function(){
        console.log(`Hello ${this.name}`);
    }
 }
//  let personB= new CreatePerson("Sarjis",25).sayHello();


// class based object

class Person{
    constructor(name,age){
        this.name=name;
        this.age=age;
        this.sayHello=function(){
            console.log('hello');
            
        };
    };
};


// let personX=new Person("hasnat",23).sayHello()


// rest operator
 function subs(...nums){
    return nums;
    // this nums variable with three dot takes numble number of value as treats as a array

 }
//  console.log(subs(2,3,4));
//  pass by value and pass by referance

// array is pass by referance datatype

let num1=[1,2,3];
let num2 =num1;
num1[0]=10;
// console.log(num1);

// spearding value

let numA = [1,2,3,4];
let numB = [...numA];

console.log(numA==numB);



