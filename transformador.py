class Transforma(object):
    def __init__(self, keys):
        self.keys = keys.split(",") #separo las llaves

    def strtoDict(self, values):
        values = values.strip()
        file = values.split(",")
        if len(file) != len(self.keys):
            return None 
        d = {}
        i = 0
        while i < len(self.keys):
            d[self.keys[i]] = file[i] #igualo las filas en ambos
            i = i + 1
        return d 


    def in_values(self): #ingresar valores para crear dict
        print("ingrese valores: ")
        file = []
        i = 0
        while i < len(self.keys):
            val = input(f"{self.keys[i]}: ")
            file.append(val) #
            i = i + 1
        values = ",".join(file)
        return self.strtoDict(values)
        
