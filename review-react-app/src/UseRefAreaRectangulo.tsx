import { useRef, useState } from "react";

function UseRefAreaRectangulo() {
    const baseRef = useRef<HTMLInputElement | null>(null);
    const heightRef = useRef<HTMLInputElement | null>(null);

    const [area, setArea] = useState(0);
    const calculateArea = () => {
        const base = Number(baseRef.current?.value || 0);
        const height = Number(heightRef.current?.value || 0);
        setArea(base * height)
    }

    return (
        <>
            <p>Area de un Rectangulo</p>
            <input
                type="number"
                ref={baseRef}
                placeholder="Escribe la base"
            />
            <input
                type="number"
                ref={heightRef}
                placeholder="Escribe la altura"
            />
            <button onClick={calculateArea}> Calcular Area </button>
            <p>El Area es: {area || '0'}</p>
        </>
    );
}

export default UseRefAreaRectangulo;
