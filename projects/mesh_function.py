import numpy as np
from collections.abc import Callable


def mesh_function(f: Callable[[float], float], t: float) -> np.ndarray:
    result=np.zeros(len(t))
    for i in range (len(t)):
        result[i]=f(t[i])
    return result
   # raise NotImplementedError


def func(t: float) -> float:
    if (t<=3) and (t>=0):
        return np.exp(-t)
    else:
        return np.exp(-3*t)
    
   # raise NotImplementedError


def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == "__main__":
    test_mesh_function()
