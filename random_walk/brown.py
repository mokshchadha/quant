import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt

#weiner process is brownian motion
def brownian_motion(dt=0.1, x0=0, n =10000):
    #ds = mue * S * dt + sigma * S *dW
    #step 1 initialse W(t) with zeros
    W = np.zeros(n+1)

    # we create N+1 timesteps: t =0,1,2,3,4
    t = np.linspace(x0,n ,n+1)

    # we have to use cummulative sum: on every step thae additional value is
    # drawn from a normal distribution with mean 0 and variance dt...N(0,dt)
    # by the way : N(0, dt)= sqrt(dt) * N(0,1) usually this formula is used!!
    W[1:n+1] = np.cumsum(np.random.normal(0, np.sqrt(dt), n))

    return t, W

def plot_process(t, W):
    plt.plot(t,W)
    plt.xlabel('Time(t)')
    plt.ylabel('Wiener-Process W(t)')
    plt.title('Wiener Process')
    plt.show()

if __name__ == '__main__':
    time, data = brownian_motion()
    plot_process(time,data) # in the graph u can see that sometimes the value is -ve hence IT IS NOT USED beacues stock price cant be negative