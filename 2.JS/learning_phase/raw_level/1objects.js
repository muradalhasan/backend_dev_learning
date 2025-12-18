let person={
    name: "Murad",
    age: 18,
    location: "Dhaka",
    func: function(){
        console.log("Say hello");
    },
};

// console.log(person.name);
// person.func();
// console.log(person["name"]);
let x="name";
// console.log(person[x]);
person.interest=["python","django","flask"];
// console.log(person.interest[2]);
delete person.interest;
// console.log(person);
let calc={
    add:function(num1,num2){
        return num1+num2;
    },
    subs:
    function(num1,num2){
        return num1-num2;
    },
    multi:function(num1,num2){
        return num1*num2;
    },
    devide:function(num1,num2){
        return num1/num2;
    },
};
// console.log(calc.add(3,2));

let them={
    name: "sumi",
    age:18,
    // interest:['js','php','python'],
    addr:{
        city:"dk",
        zip:1212,
    },
};
// console.log(them.addr.zip)
// for( let elem in person ){
//     console.log(person[elem]);
// }
let person1={
    name: "Murad",
    age: 18,
    location: "Dhaka",
    // method-->this refers same objects
    func: function(){
        console.log("Say hello "+this.name );
        
    },
};
person1.func();
function sayHey(){
    console.log(this);
    //function-->this refers global/window objects
}
sayHey();

let person2={
    name: "Murad",
    age: 18,
    location: "Dhaka",
    interest:['js','php'],
    // method-->this refers same objects
    // func: function(){
    //     console.log("Say hello "+this.name );
        
    // },


    // showint(){
    //     this.interest.forEach(function(el){
    //         console.log(el,this.name)
    //     },this);
    // },

    // to solve the above problem we can use arror function

    showInterest(){
        this.interest.forEach((el)=> {
            console.log(el,this.name);
        });
    },
};

// person2.showInterest();
let str = "hello world";

function replaceword(str,wordRe,newWoed){
   let new1=str.split(" ");
   let newarr=[];
   new1.forEach( el=>{
     if (el==wordRe){
        newarr.push(newWoed);
     }
     else{
        newarr.push(el);
     };
   });
   return newarr.join( );
};
console.log(replaceword(str,"world","earth"));