
class Student:
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(str(tracks))
        self.score = float(score)

    def change_name(self, change_name):
        self.name = change_name
        print(self.name)

    def change_age(self, change_age):
        self.age = change_age
        s = isinstance(change_age, int)
        if s == True:
            print(self.age)
        else:
            print("you did not enter number")

    def add_track(self, add_track):
        self.tracks = add_track
        print(self.tracks)

    def get_score(self):
        print(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=40.95)

# Expected methods
Bob.change_name("Miracle")
Bob.change_age(25)
Bob.add_track("Full-stack")
Bob.get_score()
