# -*- coding: utf-8 -*-
import gym
import numpy as np  
# Create an environment of Taxi-v3:
env = gym.make('Taxi-v3').env

Q_table=np.zeros((env.observation_space.n,env.action_space.n))
episodes=1000
alpha=0.6
gamma=0.9
epsilon=0.4
for i in range (1,episodes+1):
  state=env.reset()
  epochs=0
  reward=0
  done=False
  while not done :
    if np.random.rand()<epsilon :
      action = env.action_space.sample()
    else :
      action = np.argmax(Q_table[state,:])
    state_2,r,done,_=env.step(action)
    Q_table[state,action]+=alpha*(reward+gamma*np.max(Q_table[state_2,:])-Q_table[state,action])
    state=state_2
    reward+=r
    epochs+=1
  epsilon=0.001+0.399*np.exp(-0.005*episodes)
  if not i%200 :
    print(f"Finished {i}th episode with reward:{reward} and Timesteps taken: {epochs}")

#Illustration of Taxi-v3
from IPython.display import clear_output
from time import sleep
state=env.reset()
done=False
reward=0
env.render()
while not done :
    clear_output(wait=True)
    action=np.argmax(Q_table[state])
    state,r,done,_=env.step(action)
    reward+=r
    env.render()
    sleep(1)
print("Reward:",reward)
