import numpy as np

class Environment:
    
    def __init__(self,Map,random_start=True):
        

        for i in range(Map.shape[0]):
            for j in range(Map.shape[1]):
                if Map[i,j] == 'g':
                    self.goal_position  = [i,j]
                    
        self.NA = 4
        self.rand_start = random_start
        self.selected_map = Map
        self.start_position = (0,0)
        self.current_position = [0,0]
        self.actions = ['r','l','d','u']
        self.reward_dict = {
            'g':10,
            'f':-1,
            's':0,
            'h':-15
        }
        
    def reset(self):
        if self.rand_start == False:
            self.current_position = [0,0]
            return tuple(self.current_position.copy())
        else:
            self.current_position = [np.random.randint(0,self.selected_map.shape[0]),np.random.randint(0,self.selected_map.shape[1])]
            return tuple(self.current_position.copy())
    
    def randomReset(self):
        self.current_position[0] = np.random.randint(0,self.selected_map.shape[0])
        self.current_position[1] = np.random.randint(0,self.selected_map.shape[1])
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
            return (self.current_position[0],self.current_position[1]),self.reward_dict['g'],flag
        elif self.getState() == 'h':
            return (self.current_position[0],self.current_position[1]),self.reward_dict['h'],flag
        elif self.getState() == 'f' or self.getState() == 's':
            return (self.current_position[0],self.current_position[1]),self.reward_dict['f'],flag
            
    def setPosition(self,x,y):
        self.current_position[0] = x
        self.current_position[1] = y
        
    def mapToHeatMap(self):
        reward_map = np.zeros(self.selected_map.shape).astype(np.uint8)
        reward_map = np.where(self.selected_map == 'g',self.reward_dict['g'],reward_map)
        reward_map = np.where(self.selected_map == 'h',self.reward_dict['h'],reward_map)
        reward_map = np.where(self.selected_map == 'f',self.reward_dict['f'],reward_map)
        reward_map = np.where(self.selected_map == 's',self.reward_dict['s'],reward_map)
        
        heat_map = np.zeros([self.selected_map.shape[0],self.selected_map.shape[1],3]).astype(np.uint8)
        
        for i in range(self.selected_map.shape[0]):
            for j in range(self.selected_map.shape[1]):
                if self.selected_map[i,j] == 'g':
                    heat_map[i,j,:] = [0,255,0]
                elif self.selected_map[i,j] == 'h':
                    heat_map[i,j,:] = [165,42,42]
                elif self.selected_map[i,j] == 'f':
                    heat_map[i,j,:] = [120,120,120]
                elif self.selected_map[i,j] == 's':
                    heat_map[i,j,:] = [0,200,200]
        
        return heat_map,reward_map
        
        
    def getState(self):
        return self.selected_map[self.current_position[0],self.current_position[1]].copy()