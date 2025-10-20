from mqns.models.qubit.const import QUBIT_STATE_0
from mqns.models.qubit.gate import CNOT, H, X, Z
from mqns.models.qubit.qubit import Qubit


def test_swapping():
    q0 = Qubit(state=QUBIT_STATE_0, name="q0")
    q1 = Qubit(state=QUBIT_STATE_0, name="q1")
    q2 = Qubit(state=QUBIT_STATE_0, name="q2")
    q3 = Qubit(state=QUBIT_STATE_0, name="q3")

    H(q0)
    CNOT(q0, q1)
    H(q2)
    CNOT(q2, q3)
    CNOT(q1, q2)
    H(q1)

    c0 = q2.measure()
    c1 = q1.measure()

    if c0 == 1 and c1 == 0:
        X(q3)
    elif c0 == 0 and c1 == 1:
        Z(q3)
    elif c0 == 1 and c1 == 1:
        X(q3)
        Z(q3)
    assert q0.measure() == q3.measure()
