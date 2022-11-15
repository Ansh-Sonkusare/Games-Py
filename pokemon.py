class Pokemon:
    __slots__ = ["name" , "type" , "health_points" , "damage_points"]
    def __init__(self, name , tp , hp , dp) -> None:
        self.name = name
        self.type = tp
        self.health_points = hp
        self.damage_points = dp

    def get_damage(self):
        return self.damage_points
    
    def lose_round(self , dp):
        # print( self.health_points - dp )
        self.health_points = self.health_points - dp
    
    
    def is_fainted(self):
        if(self.health_points <=0):
            return True
        return False
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"{self.name}:{self.type}:{self.health_points}"
    
    def __hash__(self) -> int:
        return hash(self.name)



