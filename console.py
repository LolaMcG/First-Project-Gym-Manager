from models.client import Client
from models.exercise import Exercise

import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo

client_repo.delete_all()

client_Bob = Client("Bob", "McJim", "07743986229", "Male", "None")
client_repo.save(client_Bob)
client_Sue = Client("Sue", "Dudley", "07583991992", "Female", "Heart")
client_repo.save(client_Sue)
client_Rita = Client("Rita", "McFadyen", "07979118118", "NB", "None")
client_repo.save(client_Rita)
client_Jim = Client("Jim", "McBob", "07985481481", "Male", "None")
client_repo.save(client_Jim)