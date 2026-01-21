import { useCallback, useState } from "react";

function UseCallbackResta() {
    const [a, setA] = useState(0);
    const [b, setB] = useState(0);

    const total = useCallback(() => {
        console.log('Recalculando total')
        return a - b
    }, [a, b]);


    return (
        <>
            <input
                type="number"
                value={a}
                placeholder="valor A"
                onChange={(e) => setA(Number(e.target.value))}
            />
            <input
                type="number"
                value={b}
                placeholder="valor B"
                onChange={(e) => setB(Number(e.target.value))}
            />

            <p>La suma es: {total() || '0'}</p>
        </>
    );
}

export default UseCallbackResta;
