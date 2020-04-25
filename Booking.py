#add new choaches
def add_Coach(coach_destination, coach_no_seats):
  coach_destination = []
  for i in range (coach_no_seats):
    coach_destination.append(i)
  return coach_destination

#create a new coach as a list
London = []
Glasgow = []
Birmingham = []
NewCastle = []

#price ranges
def pricerange():
  ListPriceRanges = []
  LONDON = 15.80
  GLASGOW = 22.00
  BIRMINGHAM = 5.67
  NEWCASTLE = 32.58
  ListPriceRanges.append(LONDON)
  ListPriceRanges.append(GLASGOW)
  ListPriceRanges.append(BIRMINGHAM)
  ListPriceRanges.append(NEWCASTLE)
  print ("The Prices range for London is of ", LONDON)
  print ("The Prices range for Glasgow is of ", GLASGOW)
  print ("The Prices range for Birmingham is of ", BIRMINGHAM)
  print ("The Prices range for NewCastle is of ", NEWCASTLE)


#check if seat is empty or booked 
def checkSeatEmpty (coach, seatNumber):
  seat = coach[seatNumber]
  if type(seat) == int:
    return True
  else:
    return False


#define number of available seats in a coach
def check_seat(coach):
  count = 0
  for seat in coach:
    if type(seat) == int:
      count = count + 1
  return count

#define of booking a seat 
def booking(name, coach, seatNo):
  #check if seat is available
  if checkSeatEmpty(coach,seatNo):
    #if the seat is empty bookit with its NameError
    coach[name] = name
    print("the seat", seatNo, "is now booked on the name of", name, ", towards the destination: ", coach)
  else:
    print("the seat is already booked!")

#add Spaces
for i in range(30):
  London.append(i)
  Glasgow.append(i)
  Birmingham.append(i)
  NewCastle.append(i)

#add some default seat taken
London[5] = "Sunny"
London[6] = "Ron"
London[7] = "Harry"

Glasgow[5] = "Sunny"
Glasgow[6] = "Ron"
Glasgow[7] = "Harry"

NewCastle[5] = "Sunny"
NewCastle[6] = "Ron"
NewCastle[7] = "Harry"
  
#menu
def menu():
 # print the starting of the app
  print("WELCOME TO TRIPBUY!!!! \n here you can: \n 1. view destinations,\n 2. Book a seat \n 3. view Price Ranges \n 4. remove any bookings")

  #input the choice
  choice = input("Please enter the number of the option: ")

  #when 1 show the destinations
  if choice == "1":
    print("in this section you can view the destinations available:")
    print("1.London \n2.Glasgow \n3.Birmingham \n4.NewCastle")
    coachChoice = input("to view the seats of a destination insert the number of the destination:")

    #if it is 1 show the seats available for london
    if coachChoice == "1":
      check_seat(London)
      print(London)
      print("these are the seats. \n where you see a number, the seat is available and where you see a name, the seat is booked ")
      print("going back to menu")
      menu()

    #if it is 2 show the seats available for Glasgow
    if coachChoice == "2":
      check_seat(Glasgow)
      print(Glasgow)
      print("these are the seats. \n where you see a number, the seat is available and where you see a name, the seat is booked ")
      print("going back to menu")
      menu()

    #if it is 3 show the seats available for Birmingham
    if coachChoice == "3":
      check_seat(Birmingham)
      print(Birmingham)
      print("these are the seats. \n where you see a number, the seat is available and where you see a name, the seat is booked ")
      print("going back to menu")
      menu()

    #if it is 4 show the seats available for NewCastle
    if coachChoice == "4":
      check_seat(NewCastle)
      print(NewCastle)
      print("these are the seats. \n where you see a number, the seat is available and where you see a name, the seat is booked ")
      print("going back to menu")
      menu()


  #when 2 execute the booking function
  if choice == "2":
    print("Ok, initializing booking..... \n Please follow the instructions given.")
    name = input("Please Enter a Name for the booking: ")
    coach = input("Please Enter the Destination(for example London): ")
    seatNo = input("Please enter the seat number you want: ")
    booking(name, coach, seatNo)
    print(coach)
    print("Booking Complete")
    print("Going back to Main Menu")
    menu()
  
  if choice == "3":
    pricerange()
    print("here you can view the price ranges")
    print("Please note that the prices may vary every time of the day")
    print("going back to the menu")
    menu()

  if choice == "4":
    print("do 4 ")

menu()
