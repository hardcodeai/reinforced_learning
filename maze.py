import numpy as np

class Maze:

    def __init__(self,width,length,tile_size,level):
        # The length and height should be displayed in number of tiles not units
        self.width = width
        self.length = length
        self.tile_size = tile_size
        self.level = level

    def get_display_width(self):
        return self.width * self.tile_size

    def get_display_length(self):
        return self.length * self.tile_size

    def get_tile_size(self):
        return self.tile_size

    def gridit(self):
        np.random.seed(50)
        list_x = np.linspace(0,self.width * self.tile_size,self.width,dtype=np.int32)
        list_y = np.linspace(0,self.length * self.tile_size,self.length,dtype=np.int32)
        self.grid_points = [(x,y) for x in list_x for y in list_y]
        return self.grid_points

    def map_obstacles(self):
        self.grid = self.gridit()
        # this piece needs to go
        boolean_map1 = np.random.randint(2,size=self.width * self.length)
        boolean_map2 = np.random.randint(2,size=self.width * self.length)
        boolean_map3 = np.random.randint(2,size=self.width * self.length)
        boolean_map4 = np.random.randint(2,size=self.width * self.length)

        boolean_map_filtered1 = np.logical_and(boolean_map1,boolean_map2)
        boolean_map_filtered2 = np.logical_and(boolean_map3,boolean_map4)
        boolean_map = np.logical_and(boolean_map_filtered1,boolean_map_filtered2)

        self.obstacles = [self.grid[i] for i in range(boolean_map.size) if boolean_map[i] == 1]
        return self.obstacles

    def overlaps(self,obstacle_map,current_position,car_dim):
        flag = False
        current_x,current_y = current_position
        car_length,car_width = car_dim

        for point in obstacle_map:
            x,y = point
            if current_x >= x - car_width and current_x <= x + self.tile_size and current_y >= y - car_length and current_y <= y + self.tile_size :
                flag = True
            else:
                pass

        return flag
