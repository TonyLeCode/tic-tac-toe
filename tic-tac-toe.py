import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

import test

import math
import random

from collections import namedtuple, deque
from itertools import count


# Transition = namedtuple('Transition',
#                         ('state', 'action', 'next_state', 'reward'))

# class ReplayMemory(object):

#     def __init__(self, capacity):
#         self.memory = deque([], maxlen=capacity)

#     def push(self, *args):
#         """Save a transition"""
#         self.memory.append(Transition(*args))

#     def sample(self, batch_size):
#         return random.sample(self.memory, batch_size)

#     def __len__(self):
#         return len(self.memory)

# class DQN(nn.Module):
#   def __init__(self, n_observations, n_actions):
#     super(DQN, self).__init__()
#     self.layer1 = nn.Linear(n_observations, 128)
    
#   def forward(self, x):
#     x = F.relu(self.layer1(x))
#     x = F.relu(self.layer2(x))
#     return self.layer3(x)

# BATCH_SIZE = 128
# GAMMA = 0.99
# EPS_START = 0.9
# EPS_END = 0.05
# EPS_DECAY = 1000
# TAU = 0.005
# LR = 1e-4


# Define the neural network
class TicTacToeNet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(9, 18)
        self.fc2 = torch.nn.Linear(18, 9)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Initialize the neural network and optimizer
net = TicTacToeNet()
optimizer = torch.optim.SGD(net.parameters(), lr=0.1)

def game_loop():
  # 0 means nothing, 1 is win, 2 is draw
  def check_win(board, current_player):
    # Check for horizontal win
    for i in range(3):
      if board[(i*3)] == current_player and board[(i*3)+1] == current_player and board[(i*3)+2] == current_player:
        return 1
    # Check for vertical win
    for i in range(3):
      if board[i] == current_player and board[i+3] == current_player and board[i+6] == current_player:
        return 1
    # Check for diagonal win
    if board[0] == current_player and board[4] == current_player and board[8] == current_player:
      return 1
    if board[2] == current_player and board[4] == current_player and board[6] == current_player:
      return 1
    
    for i in range(9):
      if board[i] == 0:
        return 0
    return 2
  
  def is_valid_move(board, index):
    return board[index] == 0
  
  def toggle_player(player):
    if player == 1:
      return 2
    return 1
  
  def prompt_move():
    return int(input("make a move"))
  
  def print_board(board):
    print(decode(board[0]), decode(board[1]), decode(board[2]))
    print(decode(board[3]), decode(board[4]), decode(board[5]))
    print(decode(board[6]), decode(board[7]), decode(board[8]))
    
  def decode(int):
    if int == 0:
      return "-"
    elif int == 1:
      return "X"
    elif int == 2:
      return "O"
  
  # 0 is empty, 1 is X, 2 is O
  board = [
    0,0,0,
    0,0,0,
    0,0,0
    ]
  current_player = 1
  won_player = -1
  
  while won_player == -1:
    print_board(board)
    
    index = prompt_move()
    is_valid = is_valid_move(board, index)
    if is_valid:
      board[index] = current_player
      win_bool = check_win(board, current_player)
      if win_bool == 2:
        won_player = 0
      elif win_bool == 1:
        won_player = current_player
      current_player = toggle_player(current_player)
  
  print("game ended")
  if won_player == 0:
    print("tie")
  elif won_player == 1:
    print("X won")
  elif won_player == 2:
    print("O won")
  print_board(board)

game_loop()