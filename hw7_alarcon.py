
import timeit
import tkFileDialog
import Tkinter



# Author: Mauricio Alarcon <rmalarc@msn.com>


setup = '''
import re
import sys
import csv
import math
from scipy import stats


# Author: Mauricio Alarcon <rmalarc@msn.com>

class BasicStats:
    """
    Misc useful stats such as mean, sum of squares, var, std, cov

    """
    def __init__(self):
        pass

    def mean(self,values):
        return sum(values)/len(values)

    def sum_squares(self,values):
        g = lambda x: x*x
        return sum(map(g, values))

    def sum_xy(self, values):
        g = lambda x,y: (x* y)
        return sum(map(g, values['x'],values['y']))

    def ss_res(self, values):
        g = lambda y,f_x: (y - f_x)*(y - f_x)
        return sum(map(g, values['y'],values['f_x']))

    def var(self,value):
        return self.cov(value,value)

    def std(self,value):
        return math.sqrt(self.cov(value,value))

    def cov(self,x,y):

        if len(x) != len(y):
            return

        x_mean = self.mean(x)
        y_mean = self.mean(y)

        sum = 0

        for i in range(0, len(x)):
            sum += ((x[i] - x_mean) * (y[i] - y_mean))

        return sum/(len(x)-1)

class LinearRegression:
    """
    Calcualtes linear regressions
    """

    def __init__(self):
        self.data = {'x': [], 'y': []}
        self.r = None
        self.beta = None
        self.alpha = None

    def regression(self):
        """
        Perform linear regression

        """
        stats = BasicStats()


        n = len(self.data['x'])
        x2_sum = stats.sum_squares(self.data['x'])
        x_sum2 = sum(self.data['x'])*sum(self.data['x'])
        x_sum = sum(self.data['x'])
        y_sum = sum(self.data['y'])
        xy_sum = stats.sum_xy(self.data)
        self.alpha = (y_sum*x2_sum - x_sum*xy_sum)/(n*x2_sum-x_sum2)
        self.beta = (n*xy_sum - x_sum*y_sum)/(n*x2_sum-x_sum2)

        self.beta = stats.cov(self.data['x'],self.data['y'])/stats.var(self.data['x'])
        self.alpha = stats.mean(self.data['y']) - self.beta * stats.mean(self.data['x'])


    def scipy_regression(self):
        """
        Runs the regression using the scipy module

        """
        slope, intercept, r_value, p_value, std_err = stats.linregress(self.data['x'], self.data['y'])
        self.beta = slope
        self.alpha = intercept

    def add(self,x,y):
        """
        Adds an element to the data matrix

        :param x:
        :param y:
        """
        self.data['x'].append(float(x))
        self.data['y'].append(float(y))

    def show_top(self, n):

        """
        Prints top n- matrix elements

        :param n: Number of rows to display
        """
        i = 1
        for record in self.data:
            print("x: %.2f, y: %.2f"%(record.x, record.y))
            i += 1
            if i > n:
                break

    def show_all(self):
        """
        Prints to the console all available elements in the dataset

        """
        self.show_top(len(self.data))


    def print_equation(self):
        """
        Prints the linear regression results

        """
        print("Regression equation: y = %.2fx %+0.2f" % (self.beta, self.alpha))



    def data_from_csv(self, csv_file_name,x_index,y_index,skip_header=True):
        """
        Loads data for regression from CSV file

        :param csv_file_name:
        :param x_index: index of column that contains the x axis
        :param y_index: index of column that contains the y axis
        :param skip_header: Set to true if the file contains a header row
        :raise:
        :return Number of records loaded:
        """
        records_loaded = 0
        try:
            f = open(csv_file_name)
            first_line = skip_header
            evaluations_reader = csv.reader(f,delimiter=",")
            for record in evaluations_reader:
                if first_line:    #skip first line
                    first_line = False
                    continue
                self.add(record[x_index], record[y_index])
                records_loaded += 1
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        return records_loaded



def regression_from_file(filename):
    lr = LinearRegression()
    lr.data_from_csv(filename,2,1)
    lr.regression()

def regression_from_file_scipy(filename):
    lr = LinearRegression()
    lr.data_from_csv(filename,2,1)
    lr.scipy_regression()

filename = "/Users/malarcon/Google Drive/CUNY/IS602/assignments/brainandbody.csv"

'''

if __name__ == "__main__":

    n = 1000


    t = timeit.Timer("regression_from_file(filename)",setup=setup)
    print 'regression_from_file: ',t.timeit(n)

    t = timeit.Timer("regression_from_file_scipy(filename)",setup=setup)
    print 'regression_from_file_scipy: ',t.timeit(n)


