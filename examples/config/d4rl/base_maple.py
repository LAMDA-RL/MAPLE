from copy import deepcopy
base_params = {
    'type': 'MAPLE',
    'universe': 'gym',
    'kwargs': {
        'epoch_length': 1000,
        'train_every_n_steps': 1,
        'n_train_repeat': 1,
        'eval_render_mode': None,
        'eval_n_episodes': 10,
        'eval_deterministic': True,

        'discount': 0.99,
        'tau': 5e-3,
        'reward_scale': 1.0,

        'model_train_freq': 1000,
        'model_retain_epochs': 5,
        'rollout_batch_size': 50e3,
        'deterministic': False,
        'num_networks': 7,
        'num_elites': 5,
        'real_ratio': 0.05,
        'target_entropy': -3,
        'max_model_t': None
    }
}

maple_params = deepcopy(base_params)
maple_params['kwargs'].update({
    'separate_mean_var': True,
    'penalty_learned_var': True,
})