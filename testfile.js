const user = localStorage.getItem("namaUser") || "Kamu belum memasukkan nama."
let array = ["Abdul","Rahman","jamal","kino"]

array.forEach((value,index)=>{
        const text = document.createElement("p")
        const div = document.querySelector(".outputLocation1")
        text.textContent = value
        div.append(text)
        console.log(value)
})
    

            function hoverNotif(){
                alert("WOY JANGAN TINGGALIN HOVER")
                document.querySelector(".button-hover").innerHTML = "gua bilang apa coba"
            }

            function simpanNama(){
                let nama = document.querySelector(".input").value
                localStorage.setItem("namaUser", nama)
            }
            
            function tampilNama(){
                document.querySelector(".hasil").innerHTML = `Namamu:${user}`
            }
            

            let value = 0
            function AddButton(){
                value++
                document.querySelector(".valueShow").innerHTML = value
                const htmlElement = '<img src="ImagesFile/haimiya.png" class="gambarSatu">'
                const textBelowImg = "<p>Istri gua tuh</p>"
                if (value === 15){
                    document.querySelector(".imgBox").innerHTML = htmlElement
                    document.querySelector(".istri").innerHTML = textBelowImg
                }
            }

            function RemoveButton(){
                value--
                const htmlElement2 = '<img src="ImagesFile/sansWalpaper.jpg" class="gambarDua">'
                document.querySelector(".valueShow").innerHTML = value
                if (value === -15){
                    document.querySelector(".imgBox").innerHTML = htmlElement2
                    document.querySelector(".istri").remove()
                }
            }
            function showin(){
                document.querySelector(".outputLocation1").innerHTML = user
                document.querySelector(".inputButtonShow").innerHTML = "Show input"
            }
            function ResetButton(){
                value = 0
                document.querySelector(".valueShow").innerHTML = value
            }
            function showOutput(){
                document.querySelector(".inputButtonShow").innerHTML = "Loading"
                setTimeout(showin,3000)
            }
            const eventHandler = document.querySelector(".placeholderButtonBro")
            eventHandler.addEventListener("click",()=>{
                document.querySelector(".placeholderButtonBro").innerHTML = "WORKS"
            })

            document.body.addEventListener("keydown", (event)=>{
                console.log(event.key)
            })
            const container = document.querySelector(".MenuElement")
            const AudioFun = new Audio("bark-fart-sound.mp3")
            let Bark;
            const arrayHTML = [{
                Menu: {
                    Product: "Nasi goreng",
                    Recipe: "Telur, Ayam, Masako",
                    Harga:"Rp 12.000",
                }
            },{ Menu: {
                    Product: "ayam Bakar",
                    Recipe: "Ayam, Masako",
                    Harga:"Rp 17.000"
                }   
            },{
                Menu: {
                    Product: "Mie Ayam",
                    Recipe: "Masako, Ayam, Mie",
                    Harga:"Rp 12.000"
                }
            }].forEach((items)=>{
                const MenuElement = document.createElement("p")
                MenuElement.textContent = `Cek resep kita dan biayanya ya!
                ${items.Menu.Product},${items.Menu.Recipe},${items.Menu.Harga}`
                
                container.append(MenuElement)
                MenuElement.addEventListener("click",()=>{
                    AudioFun.play()
                    document.querySelector
                    Bark = document.createElement("span")
                    Bark.textContent = "BARK!!"
                    Bark.classList.add("fart-Text")
                    MenuElement.append(Bark)
                    AudioFun.currentTime = 0
                    setTimeout(()=>{
                        const remover = document.querySelectorAll(".fart-Text")
                        remover.forEach((elemen)=>{
                            elemen.remove()
                        })
                    },1000)
                })
            })