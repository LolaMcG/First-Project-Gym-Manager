class Exercise:
    
    def __init__(self, description, capacity, instructor, time, location, id = None):
        self.description = description
        self._capacity = capacity
        self.instructor = instructor
        self.time = time
        self.location = location
        self.id = id

    def is_full(self, number):
        return self._capacity < number
