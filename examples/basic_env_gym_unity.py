import gym

from mlagents_envs.environment import UnityEnvironment
from gym_unity.envs import UnityToGymWrapper

unity_env = UnityEnvironment(file_name="basic_env")
env = UnityToGymWrapper(unity_env,
                        uint8_visual=True,
                        flatten_branched=True,
                        allow_multiple_obs=True)

observation = env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample(
    )  # your agent here (this takes random actions)
    print("This is the action:", action)
    observation, reward, done, info = env.step(action)

    if done:
        print("I'm done")
        observation = env.reset()
        break
env.close()
