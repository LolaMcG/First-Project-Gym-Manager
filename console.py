from models.client import Client
from models.exercise import Exercise
from models.booking import Booking

import repos.client_repo as client_repo
import repos.exercise_repo as exercise_repo
import repos.booking_repo as booking_repo


booking_repo.delete_all()
exercise_repo.delete_all()
client_repo.delete_all()

client_Bob = Client("Bob", "McJim", "07743986229", "Male", "None")
client_repo.save(client_Bob)
client_Sue = Client("Sue", "Dudley", "07583991992", "Female", "Bad heart")
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


booking1 = Booking(client_Bob, exercise_heavy)
booking_repo.save(booking1)
booking2 = Booking(client_Bob, exercise_kick)
booking_repo.save(booking2)
booking3 = Booking(client_Bob, exercise_spin)
booking_repo.save(booking3)
booking4 = Booking(client_Sue, exercise_spin)
booking_repo.save(booking4)
booking5 = Booking(client_Sue, exercise_punch)
booking_repo.save(booking5)
booking6 = Booking(client_Rita, exercise_spin)
booking_repo.save(booking6)
booking7 = Booking(client_Rita, exercise_heavy)
booking_repo.save(booking7)
booking8 = Booking(client_Rita, exercise_kick)
booking_repo.save(booking8)
booking9 = Booking(client_Jim, exercise_spin)
booking_repo.save(booking9)
booking10 = Booking(client_Jim, exercise_punch)
booking_repo.save(booking10)
booking11 = Booking(client_Jim, exercise_kick)
booking_repo.save(booking11)

# client_list = client_repo.select_all()
# for each_client_that_we_are_currently_looking_at_in_the_loop in client_list:
#     print(each_client_that_we_are_currently_looking_at_in_the_loop.__dict__)

# client_repo.select_client(client_Bob.id)
# print(client_Bob.first_name, client_Bob.last_name, client_Bob.phone_no, client_Bob.gender, client_Bob.medi_cond)

# booked_clients = client_repo.clients_for_exercises(exercise_heavy)
# for each_client_booked_into_a_class in booked_clients:
    # print(each_client_booked_into_a_class.first_name, each_client_booked_into_a_class.last_name)

# booked_client = client_repo.client_for_booking(booking8)
# print(booked_client.first_name, booked_client.last_name)

# client_repo.delete_client(client_Jim.id)

# exercise_list = exercise_repo.select_all()
# for each_exercise in exercise_list:
#     print(each_exercise.description)

# exercise_repo.select_exercise(exercise_spin.id)
# print(exercise_spin.description, exercise_spin.instructor)

# return a list of exercises associated with a client when you enter a client
# list_of_exercises_for_a_client = exercise_repo.exercises_for_clients(client_Sue)
# for each_exercise in list_of_exercises_for_a_client:
#     print(each_exercise.description, each_exercise.instructor, each_exercise.time)

# which_exercise = exercise_repo.exercise_for_booking(booking1)
# print(which_exercise.description, which_exercise.instructor)

# exercise_repo.delete_exercise(exercise_kick.id)

# list_of_bookings = booking_repo.select_all()
# for each_booking in list_of_bookings:
#     print(each_booking.client.first_name, each_booking.exercise.description)