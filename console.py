from models.client import Client
from models.exercise import Exercise

import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo


exercise_repo.delete_all()
client_repo.delete_all()

client_Bob = Client("Bob", "McJim", "07743986229", "Male", "None")
client_repo.save(client_Bob)
client_Sue = Client("Sue", "Dudley", "07583991992", "Female", "Heart")
client_repo.save(client_Sue)
client_Rita = Client("Rita", "McFadyen", "07979118118", "NB", "None")
client_repo.save(client_Rita)
client_Jim = Client("Jim", "McBob", "07985481481", "Male", "None")
client_repo.save(client_Jim)

exercise_heavy = Exercise("Heavy Stuff Up and Down", 6, "Eddie Hall", "04:00", "Main Gym")
exercise_repo.save(exercise_heavy)
exercise_spin = Exercise("Psycho Spin Class", 5, "Sam Pilgrim", "06:00", "Bike Room")
exercise_repo.save(exercise_spin)
exercise_kick = Exercise("Kicking Stuff", 6, "Craig 'Massive Legs' Crawford", "08:00", "Gym 2")
exercise_repo.save(exercise_kick)
exercise_punch = Exercise("Punching Stuff", 6, "Frank Bruno", "10:00", "Boxing Ring")
exercise_repo.save(exercise_punch)