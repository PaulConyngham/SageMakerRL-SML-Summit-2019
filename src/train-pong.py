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
              "episode_reward_mean": 18,
            },
            "config": {
                "monitor": True,  # Record videos.
                # V-trace params (see vtrace.py).
#                 "vtrace": True,
#                 "vtrace_clip_rho_threshold": 1.0,
#                 "vtrace_clip_pg_rho_threshold": 1.0,

                # System params.
                #
                # == Overview of data flow in IMPALA ==
                # 1. Policy evaluation in parallel across `num_workers` actors produces
                #    batches of size `sample_batch_size * num_envs_per_worker`.
                # 2. If enabled, the replay buffer stores and produces batches of size
                #    `sample_batch_size * num_envs_per_worker`.
                # 3. If enabled, the minibatch ring buffer stores and replays batches of
                #    size `train_batch_size` up to `num_sgd_iter` times per batch.
                # 4. The learner thread executes data parallel SGD across `num_gpus` GPUs
                #    on batches of size `train_batch_size`.
                #
#                 "sample_batch_size": 50,
#                 "train_batch_size": 500,
#                 "min_iter_time_s": 10,
                "num_workers": (self.num_cpus-1),
                "num_gpus": self.num_gpus,
#                 # set >1 to load data into GPUs in parallel. Increases GPU memory usage
#                 # proportionally with the number of buffers.
#                 "num_data_loader_buffers": 1,
#                 # how many train batches should be retained for minibatching. This conf
#                 # only has an effect if `num_sgd_iter > 1`.
#                 "minibatch_buffer_size": 1,
#                 # number of passes to make over each train batch
#                 "num_sgd_iter": 1,
#                 # set >0 to enable experience replay. Saved samples will be replayed with
#                 # a p:1 proportion to new data samples.
#                 "replay_proportion": 0.0,
#                 # number of sample batches to store for replay. The number of transitions
#                 # saved total will be (replay_buffer_num_slots * sample_batch_size).
#                 "replay_buffer_num_slots": 0,
#                 # max queue size for train batches feeding into the learner
#                 "learner_queue_size": 16,
#                 # level of queuing for sampling.
#                 "max_sample_requests_in_flight_per_worker": 2,
#                 # max number of workers to broadcast one set of weights to
#                 "broadcast_interval": 1,

#                 # Learning params.
#                 "grad_clip": 40.0,
#                 # either "adam" or "rmsprop"
#                 "opt_type": "adam",
#                 "lr": 0.0005,
#                 "lr_schedule": None,
#                 # rmsprop considered
#                 "decay": 0.99,
#                 "momentum": 0.0,
#                 "epsilon": 0.1,
#                 # balancing the three losses
#                 "vf_loss_coeff": 0.5,
#                 "entropy_coeff": 0.01,
            }
          }
        }

if __name__ == "__main__":
    MyLauncher().train_main()
