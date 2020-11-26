import gym
env = gym.make("MountainCar-v0") # Create a MountainCar environment
env.reset()

for _ in range(2000): # Run for 2000 steps
    env.render()
    env.step(env.action_space.sample()) # Send a random action}