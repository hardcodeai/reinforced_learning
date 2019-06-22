import numpy as np

class Resource():
    def __init__(self,resource_name,resource_avatar,resource_points,is_consumed):
        self.resource_name = resource_name
        self.resource_avatar = resource_avatar
        self.resource_points = resource_points
        self.is_consumed = is_consumed

    def random_resource_spread(self,reference_object):
        if self.is_consumed:
            list_of_res = []
            possible_resource_locations =  list(set(reference_object.grid)-set(reference_object.obstacles))
            list_of_res.append(possible_resource_locations[np.random.randint(0,len(possible_resource_locations))])
            self.resource_location = list_of_res
            return self.resource_location

    def overlaps(self,reference_object,currentPosition,car_dim):
        return reference_object.overlaps(self.resource_location,currentPosition,car_dim)
