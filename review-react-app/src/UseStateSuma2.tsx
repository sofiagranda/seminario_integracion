import { useState } from "react";

function UseStateSuma2() {
    const [numero1, setNumero1] = useState(0);
    const [numero2, setNumero2] = useState(0);

    const suma = numero1 + numero2;

    return (
        <>
            <p>Suma 2</p>
            <input
                type="number"
                value={numero1}
                placeholder="Escribe número 1"
                onChange={(e) => setNumero1(Number(e.target.value))}
            />
            <input
                type="number"
                value={numero2}
                placeholder="Escribe número 2"
                onChange={(e) => setNumero2(Number(e.target.value))}
            />

            <p>La suma es: {suma}</p>
        </>
    );
}

export default UseStateSuma2;
