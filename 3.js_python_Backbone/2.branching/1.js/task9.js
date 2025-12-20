let hourW=-9;

if (hourW>168 || hourW<0){
    console.log("Invalid Time");
    
}else{
    if (hourW <=40){
        console.log(hourW*200);
        
    }
    else{
        let salery=8000+(hourW-40)*300;
        console.log(salery);
    }
}