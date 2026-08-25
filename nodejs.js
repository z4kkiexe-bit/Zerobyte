let event1 = ["abdul", "rahman", "wahid",]
for(let i of event1){
    console.log(i)
}

const multiplier = (a, b)=>{
    let value = a * b 
    if(value === 10){
        console.log(`BOOYAH THAT WAS ${value}`)
    }
    return value
}
console.log(multiplier(2, 5))

const arr = [1, -3, 5]
let angka = 0
arr.forEach((value, idex)=>{
    if (value === 5){
        console.log(value)
        console.log("GET READYY")
        setTimeout(()=>{
            while(true){
                console.log(`BOOYAHHHHH ${event1[angka]}!!!!!!`)
                angka+=1
                if(angka === 2){
                    angka = 0
                }
            }
        }, 3000)
    }
})
