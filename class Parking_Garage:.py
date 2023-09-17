class Parking_Garage:
# Compelted
    def __init__(self):
        self.paid = False
        #self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #self.current_ticket = {}
        #self.start_prompt = "\Please Take Ticket"
        #self.pay_prompt = "\Please insert money"
        #self.paid_prompt = "\Your Ticket has been paid, (You now have 15 minutes to leave)"
        #self.success_prompt = "\Thank you have a nice day"
# TODO pop off top of list and associate to class name value
# Example: list.pop(index) [popping off value on list and assining to name]
# spaces.pop(0) [this will assgign the top value in this case 1, to the user]
# Same for tickets
    #Parking Ticket System
    def takeTicket(self):
        self.spaces = [1,2,3,4,5,6,7,8,9,10]
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        my_space = self.spaces.pop()
        my_ticket = self.tickets.pop()
        self.current_ticket = {
            "space" : my_space,
            "ticket" : my_ticket,
            "paid" : False
        }
        print(f"Grab your ticket")
    #Take Ticket
    #Ask for users name(self.name= What's )
    #Using assigned number in dictionary, we set value to be their name
    #Here is your ticket number  Thank you for parking with us
# TODO ask for user's money input
# payment = int(input("Enter payment amount")) DONE
    def payForParking(self):
        if self.current_ticket:
            if not self.current_ticket["paid"]:
                amount = int(input("Enter payment amount: "))  
                if amount >= 15:
                    self.current_ticket["paid"] = True
                    print("Payment successful. You have 15 minutes to leave.")
                else:
                    print("Insufficient payment.")
            else:
                print("No ticket found. Please take a ticket first.")
    #Ask for users name and compare against dictionary (Use input function)
    #If user is still in dictionary ask for payment
    #Verify payment amount
    #Reassign dictionary key to have user value in empty string
# TODO: paid => display message
# not paid => run payForParkign function
# Then exit function
# Add value to spaces and tickets indicating more values in list
    def leaveGarage(self):
          return True
#Empty Dictionary to store info later
current_ticket = {}
################################################
# Main function Method
def main():
    garageSystem = True
    garageUser = Parking_Garage()
    while (garageSystem):
        print("Welcome to the parking garage")
        print("1) Take Ticket")
        print("2) Pay for Parking")
        print("3) Leave Garage")
        choice = input("Select from the following: ")
        if (choice == "1"):
            garageUser.takeTicket()
        elif (choice == "2"):
            garageUser.payForParking()
        elif (choice == "3"):
            garageSystem = False
        else:
            print("Not an option")
    print("Have a nice day!")
# Main loop function
if __name__ == "__main__":
    main()