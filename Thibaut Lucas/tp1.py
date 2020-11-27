"""
    Let's design a simulation of a self-driving cab. The major goal is to demonstrate, in a simplified environment, how you can use RL techniques to develop an efficient and safe approach for tackling this problem.

The Smartcab's job is to pick up the passenger at one location and drop them off in another. Here are a few things that we'd love our Smartcab to take care of:

    Drop off the passenger to the right location.
    Save passenger's time by taking minimum time possible to drop off
    Take care of passenger's safety and traffic rules

There are different aspects that need to be considered here while modeling an RL solution to this problem: rewards, states, and actions.



1. Rewards

Since the agent (the imaginary driver) is reward-motivated and is going to learn how to control the cab by trial experiences in the environment, we need to decide the rewards and/or penalties and their magnitude accordingly. Here a few points to consider:

    The agent should receive a high positive reward for a successful dropoff because this behavior is highly desired
    The agent should be penalized if it tries to drop off a passenger in wrong locations
    The agent should get a slight negative reward for not making it to the destination after every time-step. "Slight" negative because we would prefer our agent to reach late instead of making wrong moves trying to reach to the destination as fast as possible

2. State Space

In Reinforcement Learning, the agent encounters a state, and then takes action according to the state it's in.

The State Space is the set of all possible situations our taxi could inhabit. The state should contain useful information the agent needs to make the right action.

Let's say we have a training area for our Smartcab where we are teaching it to transport people in a parking lot to four different locations (R, G, Y, B):


Let's assume Smartcab is the only vehicle in this parking lot. We can break up the parking lot into a 5x5 grid, which gives us 25 possible taxi locations. These 25 locations are one part of our state space. Notice the current location state of our taxi is coordinate (3, 1).

You'll also notice there are four (4) locations that we can pick up and drop off a passenger: R, G, Y, B or [(0,0), (0,4), (4,0), (4,3)] in (row, col) coordinates. Our illustrated passenger is in location Y and they wish to go to location R.

When we also account for one (1) additional passenger state of being inside the taxi, we can take all combinations of passenger locations and destination locations to come to a total number of states for our taxi environment; there's four (4) destinations and five (4 + 1) passenger locations.

So, our taxi environment has 5×5×5×4=500
total possible states.




3. Action Space

The agent encounters one of the 500 states and it takes an action. The action in our case can be to move in a direction or decide to pickup/dropoff a passenger.

In other words, we have six possible actions:

    south
    north
    east
    west
    pickup
    dropoff

This is the action space: the set of all the actions that our agent can take in a given state.

You'll notice in the illustration above, that the taxi cannot perform certain actions in certain states due to walls. In environment's code, we will simply provide a -1 penalty for every wall hit and the taxi won't move anywhere. This will just rack up penalties causing the taxi to consider going around the wall.


Let's CODE 
"""


import gym

env = gym.make("Taxi-v3").env

env.render()

env.reset() # reset environment to a new, random state
env.render()

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))


"""" 
    The filled square represents the taxi, which is yellow without a passenger and green with a passenger.
    The pipe ("|") represents a wall which the taxi cannot cross.
    R, G, Y, B are the possible pickup and destination locations. The blue letter represents the current passenger pick-up location, and the purple letter is the current destination.

As verified by the prints, we have an Action Space of size 6 and a State Space of size 500. As you'll see, our RL algorithm won't need any more information than these two things. All we need is a way to identify a state uniquely by assigning a unique number to every possible state, and RL learns to choose an action number from 0-5 where:

    0 = south
    1 = north
    2 = east
    3 = west
    4 = pickup
    5 = dropoff

Recall that the 500 states correspond to a encoding of the taxi's location, the passenger's location, and the destination location.

Reinforcement Learning will learn a mapping of states to the optimal action to perform in that state by exploration, i.e. the agent explores the environment and takes actions based off rewards defined in the environment.

The optimal action for each state is the action that has the highest cumulative long-term reward.



"""


state = env.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
## add a command here to display the env


"""
    
    We are using our illustration's coordinates to generate a number corresponding to a state between 0 and 499, which turns out to be 328 for our illustration's state.

Then we can set the environment's state manually with env.env.s using that encoded number. You can play around with the numbers and you'll see the taxi, passenger, and destination move around.

The Reward Table

When the Taxi environment is created, there is an initial Reward table that's also created, called `P`. We can think of it like a matrix that has the number of states as rows and number of actions as columns, i.e. a states × actions

matrix.

Since every state is in this matrix, we can see the default reward values assigned to our illustration's state:



"""


## GO TO gym doc to display the default reward values



""" 
This dictionary has the structure {action: [(probability, nextstate, reward, done)]}.

A few things to note:

    The 0-5 corresponds to the actions (south, north, east, west, pickup, dropoff) the taxi can perform at our current state in the illustration.
    In this env, probability is always 1.0.
    The nextstate is the state we would be in if we take the action at this index of the dict
    All the movement actions have a -1 reward and the pickup/dropoff actions have -10 reward in this particular state. If we are in a state where the taxi has a passenger and is on top of the right destination, we would see a reward of 20 at the dropoff action (5)
    done is used to tell us when we have successfully dropped off a passenger in the right location. Each successfull dropoff is the end of an episode

Note that if our agent chose to explore action two (2) in this state it would be going East into a wall. The source code has made it impossible to actually move the taxi across a wall, so if the taxi chooses that action, it will just keep accruing -1 penalties, which affects the long-term reward.
"""


""" 
Solving the environment without Reinforcement Learning

Let's see what would happen if we try to brute-force our way to solving the problem without RL.

Since we have our P table for default rewards in each state, we can try to have our taxi navigate just using that.

We'll create an infinite loop which runs until one passenger reaches one destination (one episode), or in other words, when the received reward is 20. The env.action_space.sample() method automatically selects one random action from set of all possible actions.

"""

env.s = 328  # set environment to illustration's state

epochs = 0
penalties, reward = 0, 0

frames = [] # for animation

done = False

while not done:
    action = env.action_space.sample()
    _, _, _, _ = env.step(action) # go to gym doc to find the right params

    if reward == -10:
        ## increment penalties
    
    # Put each rendered frame into dict for animation
    frames.append({
        'frame': env.render(mode='ansi'),
        'state': #,
        'action': #,
        'reward': #
        }
    )

    epochs += 1
    

### Display the time steps and the penalties 




""" 
Ok now let's visualize it 

"""

from IPython.display import clear_output
from time import sleep

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'].getvalue())
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)
        
print_frames(frames)


"""
NOW let's Learn from the process 


Breaking it down into steps, we get:

        - Initialize the Q-table by all zeros.
        - Start exploring actions: For each state, select any one among all possible actions for the current state (S).
        - Travel to the next state (S') as a result of that action (a).
        - For all possible actions from the state (S') select the one with the highest Q-value.
        - Update Q-table values using the equation.
        - Set the next state as the current state.
        - If goal state is reached, then end and repeat the process.




"""

import numpy as np

q_table = np.zeros([env.observation_space.n, env.action_space.n]) # initializing the Q table


""" 
We can now create the training algorithm that will update this Q-table as the agent explores the environment over thousands of episodes.

In the first part of while not done, we decide whether to pick a random action or to exploit the already computed Q-values. 
This is done simply by using the epsilon value and comparing it to the random.uniform(0, 1) function, which returns an arbitrary number between 0 and 1.

We execute the chosen action in the environment to obtain the next_state and the reward from performing the action. After that, we calculate the maximum Q-value for the actions corresponding to the next_state, and with that, we can easily update our Q-value to the new_q_value:


"""


import random
from IPython.display import clear_output

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = # parametre qui détermine si nous allons préviligié l'exploration ou l'utilisation des valeurs apprise, le mettre entre 0.05 et 0.2

# For plotting metrics
all_epochs = []
all_penalties = []

for i in range(1, 100001):
    state = env.reset()

    epochs, penalties, reward, = # initialize the params to 0
    done = False
    
    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(q_table[state]) # Exploit learned values

        next_state, reward, done, info = env.step(action) 
        
        old_value = q_table[state, action]
        next_max = np.max(q_table[]) # /!\ trouver l'index pour acceder a l'action d'apres
        
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max) #C'est la formule que nous avons vu précédemment
        q_table[state, action] =  # updater la table par la nouvelle valeur

        if reward == -10:
            penalties  ## update la valeur des penalités

        state = next_state
        epochs += 1
        
    if i % 100 == 0:
        clear_output(wait=True)
        print(f"Episode: {i}")

print("Training finished.\n")



""" 
Ok now let's evaluate the agent 

We don't need to explore actions any further, so now the next action is always selected using the best Q-value:
"""

total_epochs, total_penalties = 0, 0
episodes = # choisir le nombre d'épisode

frames = []
for _ in range(episodes):
    state = env.reset()
    epochs, penalties, reward = 0, 0, 0
    
    done = False
    
    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

        if reward == -10:
            penalties += 1

        frames.append({
                'frame': env.render(mode='ansi'),
                'state': state,
                'action': action,
                'reward': reward
                }
            )
        epochs += 1

    total_penalties += penalties
    total_epochs += epochs

print(f"Results after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episode: {total_penalties / episodes}")


print_frames(frames)