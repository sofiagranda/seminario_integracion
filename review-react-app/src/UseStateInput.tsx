import { useState } from "react";

export function UseStateInput(){
    const [numero1, setNumero1] = useState("");
    const [numero2, setNumero2] = useState("");
    const suma = Number(numero1) + Number(numero2);
    return(
        <>
            <input 
                value={numero1}
                placeholder="Escribe un número 1"
                onChange={(e) => setNumero1(e.target.value)}
            />
            <input 
                value={numero2}
                placeholder="Escribe un número 2"
                onChange={(e) => setNumero2(e.target.value)}
            />
            <p>la suma es :{suma || '0'}</p>
        </>
    )
}