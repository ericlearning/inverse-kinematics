import jax
import random
import jax.numpy as np
from jax import jit


def rand_theta():
    key = jax.random.PRNGKey(random.randint(0, 10000))
    return jax.random.uniform(key, minval=0, maxval=np.pi*2)

def rand_arm():
    key = jax.random.PRNGKey(random.randint(0, 10000))
    return jax.random.uniform(key, minval=50, maxval=np.pi*2)

@jit
def forward_kinematics(thetas, arms):
    thetas = thetas.reshape(1, -1)

    thetas_acc = thetas @ np.tri(len(arms)).T
    thetas_acc = thetas_acc.flatten()

    x = np.cos(thetas_acc) @ arms
    y = np.sin(thetas_acc) @ arms

    return x, y