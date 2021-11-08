class Contact():
    def __init__(self, name, number):
        if name == None or number == None:
            print("Missing input!")
            return None
        self.name = name
        self.number = number

    def __str__(self):
        return self.name+" "+str(self.number)

    def get_row(self):
        return [self.name, self.number]

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number
