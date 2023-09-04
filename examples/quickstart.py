import d4rl_slim

dataset_id = "walker2d-medium-expert-v2" # See d4rl_slim.list_datasets() for full list of available datasets
env = d4rl_slim.get_environment(dataset_id)
dataset = d4rl_slim.get_dataset(dataset_id)

# env is a Gymnasium environment
obs, info = env.reset()
obs, rew, term, trunc, info = env.step(env.action_space.sample())

# dataset is a dict
print(dataset.keys())