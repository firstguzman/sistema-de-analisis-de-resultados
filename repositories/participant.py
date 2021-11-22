import datetime

class Participant:
    def __init__(self, ci, first_lastname, second_lastname, first_name, middle_initial, 
        gender, age, hours, minutes, seconds
    ):
        self.ci = ci
        self.first_lastname = first_lastname
        self.second_lastname = second_lastname
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.gender = gender
        self.age = age
        self.time = datetime.time(hours, minutes, seconds)
    
    def name(self):
        return self.first_name + '' + self.middle_initial + '. ' + self.first_lastname + ' ' + self.second_lastname
    
    def __iter__(self):
        return iter([self.ci, self.name(), self.gender, self.age, self.time])

    def age_group(self):
        if self.age in range (1,26):
            return 'Junior'
        elif self.age in range(26, 41):
            return 'Senior'
        else:
            return 'Master'

