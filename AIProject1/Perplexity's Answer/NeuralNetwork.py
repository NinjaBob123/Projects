import numpy as np
import gym

class PPO:
        def __init__(self, state_dim, action_dim, lr=0.0003, gamma=0.99, epsilon=0.2, epochs=10):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.epochs = epochs

        # Initialize policy and value function parameters
        self.policy_params = np.random.randn(state_dim, action_dim) * 0.1
        self.value_params = np.random.randn(state_dim, 1) * 0.1

    def policy(self, state):
        logits = np.dot(state, self.policy_params)
        return np.exp(logits) / np.sum(np.exp(logits))

    def value(self, state):
        return np.dot(state, self.value_params)

    def get_action(self, state):
        probs = self.policy(state)
        return np.random.choice(self.action_dim, p=probs)

    def update(self, states, actions, rewards, next_states, dones):
        states = np.array(states)
        actions = np.array(actions)
        rewards = np.array(rewards)
        next_states = np.array(next_states)
        dones = np.array(dones)

        # Compute advantages and returns
        values = self.value(states)
        next_values = self.value(next_states)
        deltas = rewards + self.gamma * next_values * (1 - dones) - values
        advantages = self.compute_gae(deltas, dones)
        returns = advantages + values

        # Compute old action probabilities
        old_probs = self.policy(states)[np.arange(len(actions)), actions]

        for _ in range(self.epochs):
            # Compute new action probabilities
            new_probs = self.policy(states)[np.arange(len(actions)), actions]

            # Compute ratio
            ratio = new_probs / old_probs

            # Compute surrogate losses
            surrogate1 = ratio * advantages
            surrogate2 = np.clip(ratio, 1 - self.epsilon, 1 + self.epsilon) * advantages

            # Compute actor and critic losses
            actor_loss = -np.mean(np.minimum(surrogate1, surrogate2))
            critic_loss = np.mean((returns - self.value(states)) ** 2)

            # Update policy and value function parameters
            policy_grad = self.compute_policy_gradient(states, actions, advantages)
            value_grad = self.compute_value_gradient(states, returns)

            self.policy_params -= self.lr * policy_grad
            self.value_params -= self.lr * value_grad

    def compute_gae(self, deltas, dones, lambda_=0.95):
        advantages = np.zeros_like(deltas)
        last_advantage = 0
        for t in reversed(range(len(deltas))):
            if dones[t]:
                last_advantage = 0
            advantages[t] = deltas[t] + self.gamma * lambda_ * last_advantage * (1 - dones[t])
            last_advantage = advantages[t]
        return advantages

    def compute_policy_gradient(self, states, actions, advantages):
        probs = self.policy(states)
        grad = np.zeros_like(self.policy_params)
        for i in range(len(states)):
            grad[i] = probs[i] - np.eye(self.action_dim)[actions[i]]
        return np.dot(states.T, grad * advantages[:, np.newaxis])

    def compute_value_gradient(self, states, returns):
        return np.dot(states.T, self.value(states) - returns)

    def save_weights(self, filename):
        """Save the policy and value function parameters to a .npy file."""
        np.save(filename, {
            'policy_params': self.policy_params,
            'value_params': self.value_params
        })

    def load_weights(self, filename):
        """Load the policy and value function parameters from a .npy file."""
        weights = np.load(filename, allow_pickle=True).item()
        self.policy_params = weights['policy_params']
        self.value_params = weights['value_params']

# Training loop
env = gym.make('CartPole-v1')
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

agent = PPO(state_dim, action_dim)
num_episodes = 1000

for episode in range(num_episodes):
    state, _ = env.reset()
    done = False
    total_reward = 0
    states, actions, rewards, next_states, dones = [], [], [], [], []

    while not done:
        action = agent.get_action(state)
        next_state, reward, done, _, _ = env.step(action)
        
        states.append(state)
        actions.append(action)
        rewards.append(reward)
        next_states.append(next_state)
        dones.append(done)

        state = next_state
        total_reward += reward

    agent.update(states, actions, rewards, next_states, dones)

    if episode % 10 == 0:
        print(f"Episode {episode}, Total Reward: {total_reward}")

# Save weights after training
agent.save_weights('ppo_weights.npy')

env.close()

# Example of how to load the weights
# new_agent = PPO(state_dim, action_dim)
# new_agent.load_weights('ppo_weights.npy')
