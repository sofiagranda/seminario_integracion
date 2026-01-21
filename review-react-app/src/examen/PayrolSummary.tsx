type Props = {
    totalHours: number;
    extra: number;
    pay: number;
};

export default function PayrollSummary({
    totalHours,
    extra,
    pay,
}: Props) {
    return (
        <section>
            <h2>Resumen</h2>
            <p>Total Horas: {totalHours}</p>
            <p>Horas Extras: {extra}</p>
            <p>Total Pago: ${pay.toFixed(2)}</p>
        </section>
    );
}
