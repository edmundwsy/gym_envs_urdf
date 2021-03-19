import gym
import nLinkUrdfReacher
import time
import numpy as np


def main():
    n = 3
    #env = gym.make('nLink-reacher-acc-v0', n=n, dt=0.01)
    env = gym.make('nLink-urdf-reacher-tor-v0', n=n, dt=0.01, render=True)
    defaultAction = np.ones(n) * 8
    n_episodes = 1
    n_steps = 1000
    cumReward = 0.0
    for e in range(n_episodes):
        ob = env.reset()
        print("Starting episode")
        for i in range(n_steps):
            time.sleep(env._dt)
            action = env.action_space.sample()
            action = defaultAction
            ob, reward, done, info = env.step(action)
            cumReward += reward


if __name__ == '__main__':
    main()