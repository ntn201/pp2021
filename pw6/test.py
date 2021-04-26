import pickle

class Course:
    def __init__(self,id,name,credits):
        if self.validate_id(id):
            self.__id = id
        if self.validate_name(name):
            self.__name = name
        if self.validate_credits(credits):
            self.__credits = credits
        self.__marks = {}

    def __str__(self):
        return self.__name

    def validate_id(self,id):
        return type(id) == int and id > 0

    def validate_name(self,name):
        return type(name) == str and len(name) > 0

    def validate_credits(self,credits):
        return type(credits) == int and credits > 0

    def validate_mark(self,mark):
        return type(mark) == float and 0.0 <= mark <= 20.0

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_student_mark(self,id):
        return self.__marks.get(str(id))
    
    def set_name(self,name):
        if self.validate_name(name):
            self.__name = name
            return True
        return False

    def set_student_mark(self,id,mark):
        try:
            file = open('marks.txt',"r+")
            updated = False
        except:
            print("Something went wrong")
        if self.validate_mark(mark):
            self.__marks[str(id)] = mark
            lines = file.readlines()
            for i, l in enumerate(lines):
               if f"{self.__id} {id}" in l:
                   lines[i] = f"{self.__id} {id} {mark}\n"
                   updated = True
            if updated:
                file = open("marks.txt","w")
                file.writelines(lines)
            else:
                file.write(f"{self.__id} {id} {mark}\n")
            file.close()
            return True
        return False

    def get_average_mark(self):
        return np.array(self.__marks.values()).mean()

    def is_valid(self):
        return self.validate_id(self.__id) and self.validate_name(self.__name) and self.validate_credits(self.__credits)
    
    def save(self, file):
        try:
            pickle.dump(self,file)
        except:
            print("Something went wrong!")


file = open("courses.txt","rb")
data = pickle.load(file)
print(data)