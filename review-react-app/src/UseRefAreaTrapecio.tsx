import { useRef, useState } from "react";

function UseRefAreaTrapecio() {
    const basemenorRef = useRef<HTMLInputElement | null>(null);
    const basemayorRef = useRef<HTMLInputElement | null>(null);
    const alturaRef = useRef<HTMLInputElement | null>(null);

    const [area, setArea] = useState(0);

    const calculateArea = () => {
        const base_menor = Number(basemenorRef.current?.value || 0);
        const base_mayor = Number(basemayorRef.current?.value || 0);
        const altura = Number(alturaRef.current?.value || 0);
        setArea(((base_menor + base_mayor)*altura)/2)
    }

    return (
        <>
            <p>Area de un Trapecio</p>
            <input
                type="number"
                ref={basemenorRef}
                placeholder="Escribe la base"
            />
            <input
                type="number"
                ref={basemayorRef}
                placeholder="Escribe la altura"
            />
            <input
                type="number"
                ref={alturaRef}
                placeholder="Escribe la altura"
            />
            <button onClick={calculateArea}> Calcular Area </button>
            <p>El Area es: {area || '0'}</p>
        </>
    );
}

export default UseRefAreaTrapecio;
