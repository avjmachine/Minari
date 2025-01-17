import gymnasium as gym
import numpy as np

import minari
from minari import get_normalized_score
from minari.data_collector.data_collector import DataCollectorV0
from tests.common import create_dummy_dataset_with_collecter_env_helper


def test_ref_score():
    local_datasets = minari.list_local_datasets()
    if "cartpole-test-v0" in local_datasets:
        minari.delete_dataset("cartpole-test-v0")

    env = gym.make("CartPole-v1")

    env = DataCollectorV0(env)
    num_episodes = 10

    ref_min_score, ref_max_score = -1, 100
    dataset = create_dummy_dataset_with_collecter_env_helper(
        "cartpole-test-v0",
        env,
        num_episodes=num_episodes,
        ref_min_score=ref_min_score,
        ref_max_score=ref_max_score,
    )

    scores = np.linspace(ref_min_score, ref_max_score, num=10)
    norm_scores = np.linspace(0, 1, num=10)

    assert np.allclose(get_normalized_score(dataset, scores), norm_scores)
