import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn



class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if not isinstance(other, Coords):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class Directions:
    LEFT = Coords(-1, 0)
    RIGHT = Coords(1, 0)
    UP = Coords(0, -1)
    DOWN = Coords(0, 1)

class Colors:
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

class Game:
    def __init__(self, render=True):
        self.grid = Coords(20,20)

        self.grid_size = 30
        self.framerate = 25

        self.position = Coords(10, 10)
        self.snake = [self.position]
        self.direction = Directions.UP
        self.food = Coords(0, 0)

        self.game_over = False
        self.points = 0
        self.render = render

        if self.render:
            pygame.init()
            self.display = pygame.display.set_mode((self.grid.x * self.grid_size, self.grid.y * self.grid_size))
            self.clock = pygame.time.Clock()

        self.place_food()
         
    def get_events(self):
        action = self.direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    action = Directions.LEFT
                elif event.key == pygame.K_RIGHT:
                    action = Directions.RIGHT
                elif event.key == pygame.K_UP:
                    action = Directions.UP
                elif event.key == pygame.K_DOWN:
                    action = Directions.DOWN

        return action

    def check_collisions(self):
        if self.position.x >= self.grid.x or self.position.x < 0 or self.position.y >= self.grid.y or self.position.y < 0:
            #print("collision")
            self.game_over = True

        for part in self.snake[1:]:
            if self.position.x == part.x and self.position.y == part.y:
                #print("snake collision")
                self.game_over = True

        if self.position.x == self.food.x and self.position.y == self.food.y:
            return True
        else:
            return False
        
    def place_food(self):
        food_x = random.randint(0, self.grid.x-1)
        #rounded_x = round(x / self.grid_size) * self.grid_size
        #food_x = rounded_x - self.grid_size

        food_y = random.randint(0, self.grid.y-1)
        #rounded_y = round(y / self.grid_size) * self.grid_size
        #food_y = rounded_y - self.grid_size

        self.food = Coords(food_x, food_y)
        
        if self.food in self.snake:
            self.place_food()

    def update_display(self):
        self.display.fill(Colors.BLACK)

        for part in self.snake:
            pygame.draw.rect(self.display, Colors.GREEN, pygame.Rect(part.x * self.grid_size, part.y * self.grid_size, self.grid_size, self.grid_size))

        pygame.draw.rect(self.display, Colors.RED, pygame.Rect(self.food.x * self.grid_size, self.food.y * self.grid_size, self.grid_size, self.grid_size))

        pygame.display.update()

    def game_step(self, action):
        #self.get_events()
        if self.render:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True


        self.direction = action
        

        self.position = Coords(self.position.x + self.direction.x, self.position.y + self.direction.y)
        self.snake.insert(0, self.position)

        ate_food = self.check_collisions()


        q_reward = 0

        if ate_food:
            self.place_food()
            self.points += 1
            q_reward = 20
        else:
            self.snake.pop(-1)
            q_reward = 1

        if self.render:
            self.update_display()
            self.clock.tick(self.framerate)

        if self.game_over:
            q_reward = -10
        
        return q_reward

    def get_state(self):
        #direction
        if self.direction == Directions.LEFT:
            direction = 0
        elif self.direction == Directions.RIGHT:
            direction = 1
        elif self.direction == Directions.UP:
            direction = 2
        elif self.direction == Directions.DOWN:
            direction = 3

        #horizontal food pos
        if (self.food.x - self.position.x)<0:
            horizontal_food = 0
        elif (self.food.x - self.position.x)>0:
            horizontal_food = 1
        else:
            horizontal_food = 2

        #vertical food pos
        if (self.food.y - self.position.y)<0:
            vertical_food = 0
        elif (self.food.y - self.position.y)>0:
            vertical_food = 1
        else:
            vertical_food = 2

        #check collision left
        if self.position.x -1 < 0 or (Coords(self.position.x-1, self.position.y) in self.snake):
            left_collision = 1
        else:
            left_collision = 0

        #check collision right
        if self.position.x +1 >= self.grid.x or (Coords(self.position.x+1, self.position.y) in self.snake):
            right_collision = 1
        else:
            right_collision = 0

        #check collision up
        if self.position.y -1 < 0 or (Coords(self.position.x, self.position.y-1) in self.snake):
            up_collision = 1
        else:
            up_collision = 0
        
        #check collision down
        if self.position.y +1 >= self.grid.y or (Coords(self.position.x, self.position.y+1) in self.snake):
            down_collision = 1
        else:
            down_collision = 0

        return direction, horizontal_food, vertical_food, left_collision, right_collision, up_collision, down_collision

class NeuralNetwork(nn.Module):
    def __init__(self, input_size=2, h1_size=8, h2_size=8, output_size=4):
        super(NeuralNetwork, self).__init__()

        self.input = nn.Linear(input_size, h1_size)
        self.h1 = nn.Linear(h1_size, h2_size)
        #self.h2 = nn.Linear(h2_size, h2_size)
        self.o = nn.Linear(h2_size, output_size)

    def forward(self, x):
        x = nn.functional.relu(self.input(x))
        x = nn.functional.relu(self.h1(x))
        #x = nn.functional.relu(self.h2(x))
        x = self.o(x)
        return x

class DQAgent():
    def __init__(self, learning_rate=0.1, gamma=0.95, initial_exploration_rate=1, min_exploration_rate=0.001, exploration_decay_time=3000, max_moves=1500):
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.exploration_rate = initial_exploration_rate
        self.max_exploration_rate = initial_exploration_rate
        self.min_exploration_rate = min_exploration_rate
        self.exploration_decay_rate = (self.max_exploration_rate - self.min_exploration_rate) / exploration_decay_time
        self.max_moves = max_moves

        self.action_list = [Directions.LEFT, Directions.RIGHT, Directions.UP, Directions.DOWN]
        self.index_to_action = {0: Directions.LEFT, 1: Directions.RIGHT, 2: Directions.UP, 3: Directions.DOWN}
        self.action_to_index = {Directions.LEFT: 0, Directions.RIGHT: 1, Directions.UP: 2, Directions.DOWN: 3}

        self.network = NeuralNetwork(7, 8, 8, 4)
        self.loss_function = nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.network.parameters(), lr=self.learning_rate)


    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            action = random.choice(self.action_list)
            action_index = self.action_to_index[action]
            output = [0,0,0]
            output.insert(action_index, 1)
            output = torch.tensor(output, dtype=torch.float)
            return action, output, action_index
        else:
            output = self.network.forward(state)
            action_index = torch.argmax(output).item()
            action = self.index_to_action[action_index]
            return action, output, action_index
        

    def train(self, predicted_q_values, next_predicted_q_values, action_index, reward):
        #predicted_q_values = self.network(state)
        #next_predicted_q_values = self.network(next_state)

        # Q-value of the current state-action pair
        current_q_value = predicted_q_values[action_index].item()
        current_q_value = torch.tensor(current_q_value, dtype=torch.float, requires_grad=True)

        # Q-value of the next state-action pair
        max_next_q_value = torch.max(next_predicted_q_values).item()

        # Compute the target Q-value
        target_q_value = reward + self.gamma * max_next_q_value
        target_q_value = torch.tensor(target_q_value, dtype=torch.float, requires_grad=True)

        # Compute loss
        loss = self.loss_function(current_q_value, target_q_value)

        # Backpropagation
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        
def human():
    if __name__ == "__main__":
        game = Game(render=True)

        while not game.game_over:
            action = game.get_events()
            game.game_step(action)
        
        print(f"Game over, points: {game.points}")
        pygame.quit()


if __name__ == "__main__":
    agent = DQAgent(learning_rate=0.1, gamma=0.95, initial_exploration_rate=0.1, min_exploration_rate=0.001, exploration_decay_time=3000, max_moves=1500)

    performance = []
    q_performance = []
    for epoch in range(500):
        
        game = Game(render=False)
        step = 0

        state = torch.tensor(game.get_state(), dtype=torch.float)
        action, q_values, action_index = agent.choose_action(state)

        while not game.game_over and step < 600:
            reward = game.game_step(action)
            next_state = torch.tensor(game.get_state(), dtype=torch.float)
            next_action, next_q_values, next_action_index = agent.choose_action(next_state)

            agent.train(q_values, next_q_values, action_index,  reward)

            state = next_state
            action = next_action
            q_values = next_q_values
            action_index = next_action_index

            step += 1
            q_performance.append(reward)

        performance.append(game.points)

    plt.plot(q_performance)
    plt.show()

    game = Game(render=True)
    while not game.game_over:
        state = torch.tensor(game.get_state(), dtype=torch.float)
        action, action_index, _ = agent.choose_action(state)
        #action = agent.action_list[action_index]
        game.game_step(action)