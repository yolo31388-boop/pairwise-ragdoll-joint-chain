import pytest
import gameplay.ragdoll_joint_chain as mod

CASES = [
    ("substep_iterations", (1,)),
    ("joint_stretch", (1,)),
    ("bone_recycle", (1,)),
    ("async_physics", (1,)),
    ("collision_group", (1,)),
    ("determinism", (1,)),
    ("solve", (1,)),
    ("validation", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("damping", (1,)),
    ("metrics", (1,)),
    ("constraint", (1,)),
    ("teleport", (1,)),
    ("budget", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
