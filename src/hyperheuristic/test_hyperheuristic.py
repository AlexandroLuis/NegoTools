# test_hyperheuristic.py
from hyperheuristic import ThompsonSampling as TS

def test_thompson_sampling():
    labels = ["Arm 1", "Arm 2", "Arm 3"]
    ts = TS(labels)
    chosen_arm = ts.draw_arm()
    ts.update_arm(False, chosen_arm)

    # Add assertions to check the behavior of the code
    assert chosen_arm in labels
    assert ts.arms[chosen_arm]['successes'] == 0
    assert ts.arms[chosen_arm]['failures'] == 1
