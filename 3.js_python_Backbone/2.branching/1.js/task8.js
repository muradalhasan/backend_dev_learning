let secC=500;

let temp=secC%3600;

let hour=(secC-temp)/3600;

let temp1=temp%60;
let min=(temp-temp1)/60

console.log(`Hours: ${hour} Minutes: ${min} Seconds: ${temp1}`);
