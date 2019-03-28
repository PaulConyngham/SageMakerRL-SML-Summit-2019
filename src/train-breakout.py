import json
import os

import gym
import ray
from ray.tune import run_experiments
from ray.tune.registry import register_env

from sagemaker_rl.ray_launcher import SageMakerRayLauncher


def create_environment(env_config):
    # This import must happen inside the method so that worker processes import this code
    return gym.make('BreakoutDeterministic-v4')


class MyLauncher(SageMakerRayLauncher):

    def register_env_creator(self):
        register_env("BreakoutDeterministic-v4", create_environment)

    def get_experiment_config(self):
        return {
          "training": { 
            "env": "BreakoutDeterministic-v4",
            "run": "IMPALA",
            "stop": {
              "episode_reward_mean": 300,
            },
            "config": {
                "monitor": True,  # Record videos.
                "num_workers": (self.num_cpus-1),
                "num_gpus": self.num_gpus,
            }
          }
        }

if __name__ == "__main__":
    MyLauncher().train_main()
