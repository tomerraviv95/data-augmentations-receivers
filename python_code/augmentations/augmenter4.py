from python_code.utils.trellis_utils import calculate_states
from python_code.utils.config_singleton import Config
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

conf = Config()


class Augmenter4:
    @staticmethod
    def augment(received_word, transmitted_word):
        #### first calculate estimated noise pattern
        gt_states = calculate_states(conf.memory_length, transmitted_word)
        noise_samples = torch.empty_like(received_word)
        centers_est = torch.empty(2 ** conf.memory_length).to(device)
        std_est = torch.empty(2 ** conf.memory_length).to(device)
        for state in torch.unique(gt_states):
            state_ind = (gt_states == state)
            state_received = received_word[0, state_ind]
            centers_est[state] = torch.mean(state_received)
            std_est[state] = torch.std(state_received)
            # centers_est[state] = classes_centers[15 - state]
            noise_samples[0, state_ind] = state_received - centers_est[state]

        new_transmitted_word = torch.rand_like(transmitted_word) >= 0.5
        new_gt_states = calculate_states(conf.memory_length, new_transmitted_word)
        new_received_word = torch.empty_like(received_word)
        for state in torch.unique(new_gt_states):
            state_ind = (new_gt_states == state)
            new_received_word[0, state_ind] = centers_est[state] + std_est[state] * torch.randn_like(transmitted_word)[0,state_ind]
        return new_received_word, new_transmitted_word
