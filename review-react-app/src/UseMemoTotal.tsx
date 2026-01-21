import { useMemo, useState } from "react";

function UseMemoTotal() {
    const [price, setPrice] = useState(0);
    const [qty, setQty] = useState(0);

    const total = useMemo(()=> 
    {
        console.log('Recalculando total')
        return price * qty
    },[price,qty]);


    return (
        <>
            <input
                type="number"
                value={price}
                placeholder="precio"
                onChange={(e) => setPrice(Number(e.target.value))}
            />
            <input
                type="number"
                value={qty}
                placeholder="cantidad"
                onChange={(e) => setQty(Number(e.target.value))}
            />

            <p>La suma es: {total || '0'}</p>
        </>
    );
}

export default UseMemoTotal;
