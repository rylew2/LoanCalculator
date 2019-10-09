import json
# Class defining a loan calculator
class LoanCalc:
    def __init__(self, amt=None, interest=None, downpayment=None, term=None):

        #inputs
        self.amt = amt; self.interest = interest; self.downpayment=downpayment; self.term=term;

        #outputs
        self.monthlyPayment = self.monthlyPaymentRaw = self.totalInterest = self.totalPayment = None

        #input user messages, types, and internal input name
        self.inputs = [
            #   [ inputMessage,     inputType,  inputName]
                ['amount: ',        float,      'amt'],
                ['interest: ',      float,      'interest'],
                ['downpayment: ',   float,      'downpayment'],
                ['term: ',          int,        'term']
        ]

    # Input: index corresponding to one of the four inputs
    # Output:  None
    # Sets the 4 input values, repeating until a valid input is entered
    def getInput(self, i):
        inputMessage, inputType, inputName = self.inputs[i]
        while True:
            try:
                rawIn = input(inputMessage)
                if inputName=='interest':
                    rawIn = rawIn.replace('%', '')
                    if inputType(rawIn)<0 or inputType(rawIn)>100:
                        raise ValueError
                val = inputType( rawIn )
            except ValueError:
                print(" That was an invalid input. Please re-enter your input.")
                continue
            else:
                if inputName =='amt':           self.amt = val
                elif inputName=='interest':     self.interest = val / 100 / 12 #interest recorded as monthly
                elif inputName=='downpayment':  self.downpayment = val
                elif inputName=='term':         self.term = val*12

                break; # break out of while loop


    def calculateOutput(self):
        self.monthlyPayment, self.monthlyPaymentRaw = self.calculateMonthlyPayment()
        self.totalPayment = self.calculateTotalPayment()
        self.totalInterest = self.calculateTotalInterest()



    # Input: None (self)
    # Output: Monthly Loan Payment
    def calculateMonthlyPayment(self):
        if not self.amt or not self.downpayment or not self.interest or not self.term: return -1

        # Monthly Payment = L[i(1+i)n] / [(1+i)n-1]
            #   M = Monthly Payment (what were trying to find out)
            #   L = Loan Amount
            #   I = Interest Rate (monthly)
            #   N = Number of Payments (total number of months)

        monthlyPaymentRaw = (self.amt-self.downpayment) * (self.interest * (1 + self.interest)** self.term) /  \
                            ((1 + self.interest) ** self.term - 1)
        monthlyPayment = round(monthlyPaymentRaw, 2)
        return monthlyPayment, monthlyPaymentRaw

    # Input: None (self)
    # Output: Total Paid
    def calculateTotalPayment(self):
        if not self.monthlyPayment or not self.term: return -1
        # Total Payment = Montlhy Raw Payment * Term (months)
        totalPayment = round(self.monthlyPaymentRaw * self.term, 2)
        return totalPayment

    # Input: None (self)
    # Output: Total Interest paid
    def calculateTotalInterest(self):
        if not self.amt or not self.downpayment or not self.totalPayment: return -1
        self.totalInterest = round(self.totalPayment - (self.amt - self.downpayment), 2)
        return self.totalInterest

    # Input: None (self)
    # Output: JSON of monthlyPayment, totalInterest, and totalPayment

    def returnJSON(self):
        j = {
            'monthly payment': self.monthlyPayment,
            'total interest': self.totalInterest,
            'total payment': self.totalPayment
        }
        return json.dumps(j)


    def printAll(self):

        print('INPUTS:')
        print('amt = {}'.format(self.amt))
        print('interest = {} '.format(self.interest))
        print('downpayment = {}'.format(self.downpayment))
        print('term = {}'.format(self.downpayment))

        print('===================================================')

        print('RESULTS:')
        print('monthlyPayment = {}'.format(self.monthlyPayment))
        print('totalInterest = {}'.format(self.totalInterest))
        print('totalPayment = {}'.format(self.totalPayment))
