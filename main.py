class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        print("Details:")
        print("Name: ", name)
        print("Age: ", age)
        print("Tracks: ", tracks)
        print("Score: ", score)
    def info(self):
        pass
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

class Bob:
    def __init__(self, change_name, change_age, add_track, get_score):
        self.change_name = change_name
        self.change_age = change_age
        self.add_track = add_track
        self.get_score = get_score
        print("Details:")
        print("change_name: ", change_name)
        print("change_age: ", change_age)
        print("add_track: ", add_track)
        print("get_score:", get_score)
        pass
Peter = Bob(change_name="Peter", change_age="34", add_track=["FE","BE"] +["UI/UX"], get_score=20.90)