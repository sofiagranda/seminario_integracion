import './App.css'
import UseCallbackResta from './UseCallBackResta'
import UseMemoTotal from './UseMemoTotal'
import UseRefAreaRectangulo from './UseRefAreaRectangulo'
import UseRefAreaTrapecio from './UseRefAreaTrapecio'
import { UseStateInput } from './UseStateInput'
import UseStateSuma from './UseStateSuma'
import UseStateSuma2 from './UseStateSuma2'
import { useState, useMemo } from "react";
import WorkDays from "./examen/WorkDays";
import PayrollSummary from "./examen/PayrolSummary";

export default function App() {
  const [hours, setHours] = useState<number[]>([0, 0, 0, 0, 0]);

  const [rate, setRate] = useState<number>(0);

  const payroll = useMemo(() => {
    const totalHours = hours.reduce((sum, h) => sum + h, 0);
    const extra = Math.max(0, totalHours - 40);
    const pay = Math.min(totalHours, 40) * rate + extra * rate * 1.5;

    return { totalHours, extra, pay };
  }, [hours, rate]);

  return (
    <div style={{ padding: "1rem", fontFamily: "Arial" }}>
      <h1>Calculadora de Nómina</h1>

      <WorkDays hours={hours} setHours={setHours} />

      <div style={{ marginTop: "1rem" }}>
        <label>
          Pago por hora:{" "}
          <input
            type="number"
            min={0}
            value={rate}
            onChange={(e) => setRate(Number(e.target.value))}
          />
        </label>
      </div>

      <PayrollSummary
        totalHours={payroll.totalHours}
        extra={payroll.extra}
        pay={payroll.pay}
      />
    </div>
  );
}
