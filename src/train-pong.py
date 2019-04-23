import json
import os

import gym
import ray
from ray.tune import run_experiments
from ray.tune.registry import register_env

from sagemaker_rl.ray_launcher import SageMakerRayLauncher


def create_environment(env_config):
    # This import must happen inside the method so that worker processes import this code
    return gym.make('PongNoFrameskip-v4')


class MyLauncher(SageMakerRayLauncher):

    def register_env_creator(self):
        register_env("PongNoFrameskip-v4", create_environment)

    def get_experiment_config(self):
        return {
          "training": { 
            "env": "PongNoFrameskip-v4",
            "run": "IMPALA",
            "stop": {
              "episode_reward_mean": 19,
            },
            "config": {
                "monitor": True,  # Record videos.

#                 "num_workers": (self.num_cpus-1),
#                 "num_gpus": self.num_gpus,

                "sample_batch_size": 50,
                "train_batch_size": 1000,
                "num_envs_per_worker": 5,
                "broadcast_interval": 5,
                "max_sample_requests_in_flight_per_worker": 1,
                "num_data_loader_buffers": 4,
                # set >0 to enable experience replay. Saved samples will be replayed with
                # a p:1 proportion to new data samples.
                "replay_proportion": 0.5,
                # number of sample batches to store for replay. The number of transitions
                # saved total will be (replay_buffer_num_slots * sample_batch_size).
                "replay_buffer_num_slots": 3000,
                "lr": 0.0005,
                "model": {
                  "dim": 42,
                },
            }
          }
        }

if __name__ == "__main__":
    MyLauncher().train_main()
