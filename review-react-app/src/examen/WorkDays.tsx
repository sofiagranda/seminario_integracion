type Props = {
    hours: number[];
    setHours: React.Dispatch<React.SetStateAction<number[]>>;
}
export default function WorkDays({ hours, setHours }: Props) {
    const days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"];

    const ChangeHours = (index: number, value: string) => {
        const hour = Number(value) || 0;
        setHours((prev) =>
            prev.map((v, idx) => (idx === index ? hour : v))
        );
    };

    return (
        <>
            <section>

                {days.map((d, i) => (
                    <div key={d}>
                        {d}:{" "}
                        <input
                            min={0}
                            type="number"
                            value={hours[i]}
                            placeholder="escribe texto"
                            onChange={(e) => ChangeHours(i, e.target.value)} />
                    </div>
                ))}
            </section>
        </>
    );
}