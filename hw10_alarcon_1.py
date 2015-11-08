import re
import sys
import csv
import matplotlib.pyplot as plt
from numpy.random import normal
import numpy

# Author: Mauricio Alarcon <rmalarc@msn.com>


class CarEvaluation:
    """
    Stores Car Evaluation Data
    """

    values_buying_price = {
        "vhigh": 4,
        "high": 3,
        "med": 2,
        "low": 1
    }

    values_maintenance_price = {
        "vhigh": 4,
        "high": 3,
        "med": 2,
        "low": 1
    }

    values_doors = {
        "5more": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    values_persons_capacity = {
        "more": 6,
        "4": 4,
        "2": 2
    }

    values_luggage_capacity = {
        "big": 3,
        "med": 2,
        "small": 1
    }

    values_safety_rating = {
        "high": 3,
        "med": 2,
        "low": 1
    }

    values_car_acceptability = {
        "vgood": 4,
        "good": 3,
        "acc": 2,
        "unacc": 1
    }

    'A simple class that represents a car evaluation'

    def __init__(self, buying_price, maintenance_price, doors, persons_capacity
                 , luggage_capacity, safety_rating, car_acceptability):
        """

        :param buying_price:
        :param maintenance_price:
        :param doors:
        :param persons_capacity:
        :param luggage_capacity:
        :param safety_rating:
        :param car_acceptability:
        """
        self.buying_price = buying_price
        self.maintenance_price = maintenance_price
        self.doors = doors
        self.persons_capacity = persons_capacity
        self.luggage_capacity = luggage_capacity
        self.safety_rating = safety_rating
        self.car_acceptability = car_acceptability

    def show_evaluation(self):
        """
        Displays evaluation information about the evaluation
        :return:
        """
        print [self.buying_price
            , self.maintenance_price
            , self.doors
            , self.persons_capacity
            , self.luggage_capacity
            , self.safety_rating
            , self.car_acceptability]


class CarEvaluations:
    """
    Stores and manages a set of car evaluations
    """

    def __init__(self):
        self.evaluations = []

    def validate_values(self, buying_price, maintenance_price, doors, persons_capacity
                        , luggage_capacity, safety_rating, car_acceptability):
        return (buying_price in CarEvaluation.values_buying_price
                and maintenance_price in CarEvaluation.values_maintenance_price
                and doors in CarEvaluation.values_doors
                and persons_capacity in CarEvaluation.values_persons_capacity
                and luggage_capacity in CarEvaluation.values_luggage_capacity
                and safety_rating in CarEvaluation.values_safety_rating
                and car_acceptability in CarEvaluation.values_car_acceptability)

    def add(self, buying_price, maintenance_price, doors, persons_capacity
            , luggage_capacity, safety_rating, car_acceptability):
        """
        Creates a new CarEvaluation and loads it into the evaluations array.

        :param buying_price:
        :param maintenance_price:
        :param doors:
        :param persons_capacity:
        :param luggage_capacity:
        :param safety_rating:
        :param car_acceptability:
        """
        validation_results_pass =  self.validate_values(buying_price, maintenance_price, doors, persons_capacity
                                                   , luggage_capacity, safety_rating, car_acceptability)
        if validation_results_pass:
            self.evaluations.append(CarEvaluation(buying_price, maintenance_price, doors, persons_capacity
                                                  , luggage_capacity, safety_rating, car_acceptability))
        else:
            raise NameError("There are invalid values in record: [%s,%s,%s,%s,%s,%s,%s]" % (buying_price
                                                                                            , maintenance_price
                                                                                            , doors
                                                                                            , persons_capacity
                                                                                            , luggage_capacity
                                                                                            , safety_rating
                                                                                            , car_acceptability))

    def show_top(self, n):

        """
        Prints top n- elements of evaluation array

        :param n: Number of rows to display
        """
        i = 1
        for evaluation in self.evaluations:
            evaluation.show_evaluation()
            i += 1
            if i > n:
                break

    def show_all(self):
        """
        Prints to the console all available evaluations

        """
        self.show_top(len(self.evaluations))


    def sort_by(self, variable_name, sort_order):

        """
        Sorts the evaluations list by the given variable name in the specified sort order

        :param variable_name:
        :param sort_order:
        :return:
        """
        order_by = getattr(CarEvaluation, "values_" + variable_name)

        reverse_order = (sort_order != "asc")

        self.evaluations = sorted(self.evaluations
                                  , key=lambda x: order_by[getattr(x, variable_name)]
                                  , reverse=reverse_order)

        return self

    def to_csv(self, csv_file_name):
        """
        Export evaluations to a CSV file

        :param csv_file_name:
        :return: :raise:
        """
        records_saved = 0
        try:
            f = open(csv_file_name, "w")
            a = csv.writer(f)
            for s in self.evaluations:
                a.writerow([s.buying_price, s.maintenance_price, s.doors, s.persons_capacity
                    , s.luggage_capacity, s.safety_rating, s.car_acceptability])
                records_saved += 1
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        return records_saved


    def from_csv(self, csv_file_name):
        """
        Loads car evaluation data from the specified csv file name in the format:

                http://archive.ics.uci.edu/ml/datasets/Car+Evaluation

        :param csv_file_name:
        :raise:
        :return Number of records loaded:
        """
        records_loaded = 0
        try:
            f = open(csv_file_name)
            evaluations_reader = csv.reader(f,delimiter=",")
            for evaluation in evaluations_reader:
                evaluations.add(evaluation[0], evaluation[1], evaluation[2], evaluation[3]
                                , evaluation[4], evaluation[5], evaluation[6])
                records_loaded += 1
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        return records_loaded

    def search(self, pattern):
        """Search for a specific pattern within the evaluations list. The results are returned as a new
        instance of CarEvaluations

        It takes a list for input of CarEvaluation objects and a value to search for it returns true if the value
        is in the safety  attribute of an entry on the list, otherwise false

        :param pattern: Pattern to search for in the form of a dictionary as follows:
            {"field_name_1":"regex_for_field_1"
            ,"field_name_2":"regex_for_field_2"
            .......
            ,"field_name_n":"regex_for_field_n")
        :return CarEvaluations: Returns matched evaluations as a CarEvaluations object
        """

        matched = False
        matches = []
        numbers_of_field_to_match = len(pattern)
        for evaluation in self.evaluations:
            fields_matched_in_evaluation = 0
            for field in pattern:
                match_regex= pattern[field]
                field_value = getattr(evaluation, field)
                matched_field_value = re.search(match_regex,field_value)
                if matched_field_value:
                    fields_matched_in_evaluation += 1
            if fields_matched_in_evaluation == numbers_of_field_to_match:
                matches.append(evaluation)
        search_results = CarEvaluations()
        search_results.evaluations = matches
        return search_results

    def array_from_field(self, field, use_values = False):
        matches = []
        for evaluation in self.evaluations:
            value =getattr(evaluation, field)
            if use_values:
                attr_value = getattr(CarEvaluation,"values_"+field)
                value = attr_value[value]
            matches.append(value)
        return numpy.array(matches)

    def plot_data(self):
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
        axes[0, 0].hist(self.array_from_field("safety_rating",True))
        axes[0, 0].set_title("Safety Rating")

        axes[0, 1].hist(self.array_from_field("buying_price",True))
        axes[0, 1].set_title("Buying Rating")

        axes[1, 0].hist(self.array_from_field("maintenance_price",True))
        axes[1, 0].set_title("Maintenance Price")

        axes[1, 1].hist(self.array_from_field("doors",True))
        axes[1, 1].set_title("Doors")

        for ax in axes.flatten():
            ax.set_yticklabels([])

        fig.suptitle("Car Data Histograms")
        fig.subplots_adjust(hspace=0.4)

        plt.show()

if __name__ == "__main__":

    filename="cars.data.csv"

    evaluations = CarEvaluations()

    print "1. Loading from "+filename

    records_loaded = evaluations.from_csv(filename)

    print "%i evaluations loaded" %(records_loaded)

    print "2a. Top 10 by safety rating (hi->lo)"
    evaluations.sort_by("safety_rating", "desc")
    evaluations.show_top(10)

    evaluations.plot_data()

    #print evaluations.search({"doors":"4"}).show_all()