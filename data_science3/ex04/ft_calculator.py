

class calculator:
    
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        # print(f"Dot product is:  {V1}")
        # print(f"Dot product is:  {V2}")
        # v3 = zip(V1, V2)
        print(f"Dot product is:  {sum([x*y for x,y in zip(V1,V2)])}")
                
        
        # answer = 
        # print(f"Dot product is:  {answer}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        answer = [x+y for x,y in zip(V1,V2)]
        print(f"Sous Vector is: {['{:.1f}'.format(elem) for elem in answer]}")
        

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        answer = [x-y for x,y in zip(V1,V2)]
        print(f"Sous Vector is: {['{:.1f}'.format(elem) for elem in answer]}")
