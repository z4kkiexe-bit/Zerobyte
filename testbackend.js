            async function LoadBackend() {
                    try {
                        const response = await fetch("https://supersimplebackend.dev/hello")
                        if(!response.ok){
                            console.log(response.status)
                        }
                        console.log(response)
                    } catch(error) {
                        console.log("Unexpected error")
                    }
                }