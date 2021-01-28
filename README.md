# Representing Altruism in Multi-agent Theory of Minds

## Overview
This repository contains a stag hunt simulation that implements the AI agents following Composable Team Hierarchies (from https://arxiv.org/abs/1901.06085) in order to cooperate. We are investigating how we can model altruism in these cooperative/competitive games, by changing the reward structure and adding in a partially observable altruism broadcast. We are also interested in adding a play the dictator game option to allow agents to force others to reveal their actual relationship with the other person. Lastly, this game will also be playable by humans, and we want to investigate the association between depression and the choices/trust that the human has in the other agents and their altruistic intentions.

## Prerequisites
I am using a Macbook Pro 2015, with MacOS Mojave, so this is what I have set up.

* Unity 2019.2.4f1 with WebGL support
* pipenv
* And all the other dependencies that are found in the `requirements.txt`, which you can download using `pipenv install`

## Getting Started
1. Download the dependencies mentioned in the pre-requisites
2. Git clone the `ml-agents` repository (https://github.com/Unity-Technologies/ml-agents) onto your local machine.
2. Press `File -> Open Project` in your Unity window, and open the `Project` folder.
3. Navigate to `ML-Agents/Examples/Basic` and open the `Basic` scene
4. Follow the instructions at https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Executable.md to build an environment executable. I checked "Development Build" for "PC, Mac & Linux Standalone.
5. Press Build.
6. If there is one agent in the environment, you can use the `basic_env_gym_unity.py` file to run the environment. Else, if there are two agents, you can use the `two_agents_basic_env_gym_unity.py` file to run the environment.


## Multi-agent Unity
I have modified the `UnityGymWrapper` so that it can be used in discrete action space environments with >1 agents and >1 Behaviors. The code that my wrapper is based on is from here: https://github.com/Unity-Technologies/ml-agents/issues/4228. The modified wrapper can be found in the `examples` folder under `__init__.py`.

## Current Progress
* In the examples folder, I have an example of a one-agent environment to show the simple setup of OpenAI gym interfacing with Unity. I also have an example of using my modified `MultiUnityWrapper` in a two-agent environment with one behavior using the Basic environment.

* NEXT: add in another behavior, as well as a playable agent into the two-agent environment example to use as proof of concept. Try exporting it as a WebGL build and putting it online so that we can try playing it.

* TODO once the proof of concept is done (1/29/21): Import the code from the previous repository and change it so that it links up to Unity and not Pyglet.
