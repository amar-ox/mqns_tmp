from mqns.models.qubit.const import QUBIT_STATE_0, QUBIT_STATE_1
from mqns.models.qubit.decoherence import DissipationStorageErrorModel
from mqns.models.qubit.factory import QubitFactory
from mqns.models.qubit.gate import CNOT, H


def test_qubit_dissipation_1():
    Qubit = QubitFactory(operate_decoherence_rate=0.2, measure_decoherence_rate=0.2)

    q0 = Qubit(state=QUBIT_STATE_1, name="q0")

    DissipationStorageErrorModel(q0, 1, 0.2)

    print(q0.state)


def test_qubit_dissipation_epr():
    Qubit = QubitFactory(operate_decoherence_rate=0.5, measure_decoherence_rate=0.5)

    q0 = Qubit(state=QUBIT_STATE_0, name="q0")
    q1 = Qubit(state=QUBIT_STATE_0, name="q0")

    H(q0)
    CNOT(q0, q1)

    DissipationStorageErrorModel(q0, 1, 1)

    print(q0.state)
    print(q1.state)
