import numpy as np

class Environment:
    
    def __init__(self,Map):
        
        self.MAPS ={
               '4x4':np.array([['s','f','f','f'],
                               ['h','f','f','h'],
                               ['f','h','f','f'],
                               ['f','f','f','g']])
        }
        
        self.NA = 4
        self.selected_map = self.MAPS[Map]
        self.start_position = [0,0]
        self.goal_position  = [3,3]
        self.current_position = [0,0]
        self.actions = ['r','l','d','u']
        
    def reset(self):
        self.current_position = [0,0]
        
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
            
        if self.selected_map[self.current_position[0],self.current_position[1]] == 'g':
            return self.current_position[0],self.current_position[1],0,flag
        else:
            return self.current_position[0],self.current_position[1],-1,flag
            
    def setPosition(self,x,y):
        self.current_position[0] = x
        self.current_position[1] = y
        
        
    def getState(self):
        return self.selected_map[self.current_position[0],self.current_position[1]]