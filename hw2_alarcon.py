# Author: Mauricio Alarcon <rmalarc@msn.com>


class CarEvaluation:
    """
    Stores Car Evaluation Data
    """
    carCount=0
    'A simple class that represents a car evaluation'
    def __init__(self, make, price, safety_rating):
        """

        :rtype : CarEvaluation
        """
        self.price = price
        self.make = make
        self.safety_rating = safety_rating
        CarEvaluation.carCount += 1

    def showEvaluation(self):
        """
        Displays evaluation information about car
        :return:
        """
        print "The %s has a %s price and it's safety is rated a %i" %(self.make,self.price,self.safety_rating)


def sortbyprice(L,order):
    """Sorts list of Car Evaluations. It takes a list of CarEvaluation objects for input and either "asc" or "des".
     If it gets "asc" return a list of car names order by ascending price otherwise by descending price

    :param L: List of Car Evaluations
    :param order: asc or des
    :return: Returns sorted list by price
    """
    reverse_order = (order != "asc")
    price_order = { "High": 3,
                    "Med": 2,
                    "Low": 1
    }
    sorted_list = sorted(L, key=lambda x: price_order[x.price], reverse=reverse_order)

    return [o.make for o in sorted_list]



def searchforsafety(L,v):
    """Search for Vehicles with Safety Rating

    It takes a list for input of CarEvaluation objects and a value to search for it returns true if the value is in the
    safety  attribute of an entry on the list, otherwise false

    :param L: CarEvaluation List of objects
    :param v: Value to search for
    :return: true if value is in list of objects
    """
    return v in (o.safety_rating for o in L)


# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":
    eval1 = CarEvaluation("Ford", "High", 2)
    eval2 = CarEvaluation("GMC", "Med", 4)
    eval3 = CarEvaluation("Toyota", "Low", 3)

    print "Car Count = %d" % CarEvaluation.carCount  # Car Count = 3

    eval1.showEvaluation()  #The Ford has a High price and it's safety is rated a 2
    eval2.showEvaluation()  #The GMC has a Med price and it's safety is rated a 4
    eval3.showEvaluation()  #The Toyota has a Low price and it's safety is rated a 3

    L = [eval1, eval2, eval3]

    print sortbyprice(L, "asc");  #[Toyota, GMC, Ford]
    print sortbyprice(L, "des");  #[Ford, GMC, Toyota]
    print searchforsafety(L, 2);  #true
    print searchforsafety(L, 1);  #false