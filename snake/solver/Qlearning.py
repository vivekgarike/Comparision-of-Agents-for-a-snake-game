def act(self, snake, food):
    state = self._GetState(snake, food)

    # Epsilon greedy
    rand = random.uniform(0,1)
    if rand < self.epsilon:
        action_key = random.choices(list(self.actions.keys()))[0]
    else:
        state_scores = self.qvalues[self._GetStateStr(state)]
        action_key = state_scores.index(max(state_scores))
    action_val = self.actions[action_key]

    # Remember the actions it took at each state
    self.history.append({
        'state': state,
        'action': action_key
        })
    return action_val


    def UpdateQValues(self, reason):
    history = self.history[::-1]
    for i, h in enumerate(history[:-1]):
        if reason: # Snake Died -> Negative reward
            sN = history[0]['state']
            aN = history[0]['action']
            state_str = self._GetStateStr(sN)
            reward = -1
            self.qvalues[state_str][aN] = (1-self.lr) * self.qvalues[state_str][aN] + self.lr * reward # Bellman equation - there is no future state since game is over
            reason = None
        else:
            s1 = h['state'] # current state
            s0 = history[i+1]['state'] # previous state
            a0 = history[i+1]['action'] # action taken at previous state

            x1 = s0.distance[0] # x distance at current state
            y1 = s0.distance[1] # y distance at current state

            x2 = s1.distance[0] # x distance at previous state
            y2 = s1.distance[1] # y distance at previous state

            if s0.food != s1.food: # Snake ate a food, positive reward
                reward = 1
            elif (abs(x1) > abs(x2) or abs(y1) > abs(y2)): # Snake is closer to the food, positive reward
                reward = 1
            else:
                reward = -1 # Snake is further from the food, negative reward

            state_str = self._GetStateStr(s0)
            new_state_str = self._GetStateStr(s1)
            self.qvalues[state_str][a0] = (1-self.lr) * (self.qvalues[state_str][a0]) + self.lr * (reward + self.discount*max(self.qvalues[new_state_str])) # Bellman equation