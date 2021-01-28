import gym
from mlagents_envs.environment import UnityEnvironment
from gym_unity.envs import UnityToGymWrapper
from __init__ import MultiUnityWrapper

NUM_AGENTS = 2

unity_env = UnityEnvironment(file_name="two_agents_basic_env")
env = MultiUnityWrapper(unity_env,
                        uint8_visual=True,
                        flatten_branched=True,
                        allow_multiple_obs=True)
# env = UnityToGymWrapper(unity_env,
#                         uint8_visual=True,
#                         flatten_branched=True,
#                         allow_multiple_obs=True)

observation = env.reset()
for _ in range(1000):
    env.render()
    action_dict = {}  # {"agent_1": [0.0, 1.2, 3.0,], "agent_2": ...]
    for agent_id in range(0, NUM_AGENTS):
        action = env.action_space[agent_id].sample()  # your agent here (this takes random actions)
        action_dict[agent_id] = action
    observation, reward, done, info = env.step(action_dict)
    print("These are the observations:", observation)
    print("This is the reward:", reward)
    print("This is done:", done)
    print("This is info:", info)

    is_game_over = False
    for i in done:
        if done[i]:
            print("Agent", i, "is done")
            observation = env.reset()
            is_game_over = True
            break
    if is_game_over:
        break
env.close()
