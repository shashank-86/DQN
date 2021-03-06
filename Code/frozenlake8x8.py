# -*- coding: utf-8 -*-


import gym
import numpy as np

"""#Approach
In frozen lake the agent gets 1.0 reward for reaching the goal and 0.0 reward in all other cases involving falling in hole. So we will try to redefine reward for falling in hole. This is a basic approach more better methods can be thought off.
"""

fl=gym.make('FrozenLake8x8-v0').env
q_table=np.zeros((fl.observation_space.n,fl.action_space.n))
episodes=5000
alpha=0.6
gamma=0.9
epsilon=1.0
for i in range (1,episodes+1):
  state=fl.reset()
  epochs=0
  reward=0
  done=False
  while not done :
    if np.random.rand()<epsilon :
      action = fl.action_space.sample()
    else :
      action = np.argmax(q_table[state])
    state_2,r,done,_=fl.step(action)
    if done and not r :
      r=-100
    elif r==1.0 :
      r=20
    q_table[state,action]+=alpha*(r+gamma*np.max(q_table[state_2])-q_table[state,action])
    state=state_2
    r=int((r+100)/120)*1.0
    reward+=r
    epochs+=1
  epsilon=0.01+0.99*np.exp(-0.001*episodes)
  if not i%200 :
    print(f"Finished {i}th episode with reward:{reward} and Timesteps taken: {epochs}")

#Illustration of FrozenLake8x8-v0
from IPython.display import clear_output
from time import sleep
state_2=fl.reset()
done=False
reward=0
fl.render()
while not done :
    clear_output(wait=True) 
    action=np.argmax(q_table[state])
    state,r,done,_=fl.step(action)
    reward+=r
    fl.render()
    sleep(0.1)
print("Reward:",reward)
