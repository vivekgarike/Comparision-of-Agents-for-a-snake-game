# Comparision of AI agents in snake game

This is the final project for the course of Artificial Intelligence(Spring-2021). This project is implemented by Muvva Mukesh and Garike Vivek.

This project implements snake game using Artificial Intelligence agents. We have developed agents based on search based and reinforcement learning based agents. We have implemented total four agents to implement the game.

## Logic of the snake game:
  1) The snake grows when it eats food.
  2) The snake dies when it hits the wall or if it bites itself.

## Architecture and tech-stack of the snake game:
  This projects uses Pygame to create the snake game UI. All the algorithms and manipulations of the   snake game were done by using python-3.

## Regarding UserInterface(UI) of the game:
  1) The UI is divided into two parts
  2) The first part is a grid of size 8*8.
  3) The snake game is implemented in the first part of the grid.
  4) The remaining part of the grid is used to show important features like length of the snake and        the number of steps it has taken before the snake dies.
  6) The maximum length a snake could grow is 64 as the snake grid is of size 8*8
 
## Performance Evaluation of the snake game:
  1) Average length: Average length of the snake has grown before it does.
  2) Average Steps : Average steps the snake has moved before it dies.

  
## The agents we have choosen are:
1) Breadth First Search
2) Depth First Search
3) Hamilton Search
4) Q-Learning

# Breadth First Search:
  By using the Breadth-First Search technique in the snake game, the snake traverses or explores the adjacent coordinates rather than the deepest coordinates of the game.
  The algorithm uses the queue data structure and append each adjacent nodes recursively and find the path of the fruit coordinates in the snake game. By using the path, the       snake reaches the fruit coordinates in the game. The snake does not visit the coordinates again until it has reached the fruit coordinates in the game.
  
  ## Algorithm:
  1) In this step, the initial coordinates of the snake are pushed on the
     queue and set the initial coordinates as visited coordinates.
  2) In this step, Dequeue the coordinates in the queue one by one, and
     its all unvisited adjacent coordinates are pushed on the queue and set them as visited coordinates.
  3) In this step, the step2 will be repeated continuously until the food coordinates are visited.
  4) In this step, if the fruit coordinates are visited it stop and traces the path and returns it.
  
# Depth First Search:
  By using the Depth-First Search in the game, the snake explores the coordinates to its deepest level, and then it backtracks until unexplored coordinates to reach the
  fruit coordinates in the game. The algorithm uses the stack data structure for the exploration of the coordinates and append each coordinates recursively and find the  
  path for the snake game to reach the fruit coordinates in the game. By using the path, the snake reaches the food coordinates in the game. The snake does not visit
  the coordinates again until it has reached the fruit coordinates in the game. The snake uses more time to reach the food coordinates in the game in many cases. The
  snake traverses the long path by using this algorithm. The average number of visited coordinates in the game is very high by using this algorithm. There is a high chance
  of reaching the dead state in the game when the snake grows higher.
  
  ## Algorithm:
   1) The initial coordinates of the snake are pushed on the stack and set  
      the initial coordinates as visited coordinates.
   2) The next adjacent unvisited coordinates are pushed on to the stack
       recursively and set the coordinates as the visited coordinates.
   3) The step2 will be repeated continuously until the food coordinates are
      visited.
   4) If the fruit coordinates are visited it stop and traces the path and
      returns it.


# Hamilton Search:
  Hamilton path is the path which the node in the graph should visit exactly only once. It is one of the brute force search algorithm. This algorithm is very much
  similar to the depth-first algorithm. In the snake game, it explores all the possible paths and eventually reaches the fruit coordinates. Longest paths are explored by
  using this algorithm. There is a high chance of reaching the dead state in the game when the snake grows higher. The snake does not visit the coordinates again until
  it has reached the fruit coordinates in the game.
 
 ## Algorithm:
   1) The initial coordinates of the snake are pushed on the stack 
            and set the initial coordinates as visited coordinates
   2) The next adjacent unvisited coordinates are pushed on to the stack
            recursively and set the coordinates as the visited coordinates.
   3) If any coordinates are visited already once it backtracks and changes
             the path.
   4) The step 2, step 3 will be repeated continuously until the food coordinates are visited.
   
   5) If the food coordinates are visited it stops and returns the traces path.
    
# Q-Learning:
  Q-learning is a reinforcement learning method that teaches a learning agent how to perform a task by rewarding good behavior and punishing bad behavior. In Snake, 
  for example, moving closer to the food is good. Going off the screen is bad. At each point in the game, the agent will choose the action with the highest expected reward.
  At first, the snake doesn’t know how to eat the food and is less “purposeful”. It also tends to die a lot by going the opposite way that 
  its currently going and immediately     hitting its tail. But it doesn’t take very long for the agent to learn how to play the game. After proper training, 
  it plays quite well. 
    
   ## Algorithm:
   We use the Bellman Equation to compute the total expected reward of an action, and store the information in a Q-Table.
   At each given state, the agent looks at the Q-Table and takes the action that has the highest expected reward. The takeaway here is that there is no 
   pre-defined logic on how the snake should act. It is entirely learned from the data. After each move, we will update our Q Table using the Bellman Equation. 
   If snake has moved closer to the food, or has eaten the food, it will get a positive reward. If the snake hit its tail or a wall, or has moved further from the food,
   it will get a negative reward.
    
# Results:
  ## These results were taken after each agent was run atleast 15 times and the average results were taken.
  
  | SNO | Algorithm/Agent       | Average Length  | Average Steps   | 
  | --- | --------------------  | --------------- |-----------------|
  | 1   | BFS                   | 60/64           |     1000        |
  | 2   | DFS                   | 57/64           |     890         |
  | 3   | Hamilton              | 61/64           |     1120        |
  | 4   | Q-Learning            | 63/64           |     820         |

# Analysis:
  While running Q-learning for the first 5-10 times, the snake died freqently because of the unstable Q-Table. But after training atleast 10 times the snake started growing fast
  and it achieved maximum length. The BFS and DFS were almost same, but the BFS doing better than DFS and Hamilton but less than Q-Learning. With a proper Q-Table 
  the BFS, DFS and hamilton couldn't beat Q-Learning. Although updation of Q-table takes time but a good approach for this game.
  

# Execution:
  Open the run.py file, choose the algorithm from the dictionary, with which you want to run the snake game. After choosing the agent/Algorithm run that run.py file and watch 
  snake game with your desired agent.
  

# Requirements:
  Install Pygame, Tensorflow for the UI part.











    
