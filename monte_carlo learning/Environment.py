import numpy as np

class Environment:
    
    def __init__(self,Map,random_start=True):
        
        self.MAPS ={
               '4x4':np.array([['s','f','f','h'],
                               ['h','h','f','h'],
                               ['h','f','f','h'],
                               ['h','f','f','g']])
        }
        
        self.NA = 4
        self.rand_start = random_start
        self.selected_map = self.MAPS[Map]
        self.start_position = (0,0)
        self.goal_position  = [3,3]
        self.current_position = [0,0]
        self.actions = ['r','l','d','u']
        
    def reset(self):
        if self.rand_start == False:
            self.current_position = [0,0]
            return tuple(self.current_position.copy())
        else:
            self.current_position = [np.random.randint(0,4),np.random.randint(0,4)]
            return tuple(self.current_position.copy())
    
    def randomReset(self):
        self.current_position[0] = np.random.randint(0,4)
        self.current_position[1] = np.random.randint(0,4)
        return self.current_position.copy()
        
    def render(self):
        print(self.selected_map)
        
    def step(self,action):
        flag = False
        if action == 'u' and self.current_position[0] != 0:
            self.current_position[0] -= 1
            flag = True
        
        if action == 'd' and self.current_position[0] != self.selected_map.shape[0]-1:
            self.current_position[0] += 1
            flag = True
            
        if action == 'r' and self.current_position[1] != self.selected_map.shape[0]-1:
            self.current_position[1] += 1
            flag = True
            
        if action == 'l' and self.current_position[1] != 0:
            self.current_position[1] -= 1
            flag = True
            
        if self.getState() == 'g':
            return (self.current_position[0],self.current_position[1]),10,flag
        elif self.getState() == 'h':
            return (self.current_position[0],self.current_position[1]),-5,flag
        elif self.getState() == 'f' or self.getState() == 's':
            return (self.current_position[0],self.current_position[1]),0,flag
            
    def setPosition(self,x,y):
        self.current_position[0] = x
        self.current_position[1] = y
        
        
    def getState(self):
        return self.selected_map[self.current_position[0],self.current_position[1]].copy()