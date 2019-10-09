import unittest
from LoanCalc import LoanCalc

class Test(unittest.TestCase):
  def test_LoanCalculator(self):
    amt = 100000; interest = 5.5/ 100 / 12;
    downpayment=20000; term = 30*12;

    lc1 = LoanCalc(amt, interest, downpayment, term)
    lc2 = LoanCalc(amt + 100000, interest, downpayment, term)
    lc3 = LoanCalc(amt + 200000, interest, downpayment, term)

    lc1.calculateOutput()
    self.assertEqual(lc1.returnJSON(),'{"monthly payment": 454.23, "total interest": 83523.23, "total payment": 163523.23}')

    lc2.calculateOutput()
    self.assertEqual(lc2.returnJSON(),'{"monthly payment": 1022.02, "total interest": 187927.27, "total payment": 367927.27}')

    lc3.calculateOutput()
    self.assertEqual(lc3.returnJSON(), '{"monthly payment": 1589.81, "total interest": 292331.31, "total payment": 572331.31}')

  def test_MonthlyPayment(self):
    amt = 100000; interest = 5.5 / 100 / 12;
    downpayment = 20000; term = 30 * 12;
    lc1 = LoanCalc(amt, interest, downpayment, term)
    self.assertEqual(lc1.calculateMonthlyPayment(), (454.23, 454.2312010776004))


    amt=50000; interest=3.5/100/12;
    downpayment=10000; term=15*12;
    lc2 = LoanCalc(amt, interest, downpayment, term)
    self.assertEqual(lc2.calculateMonthlyPayment(), (285.95, 285.9530165372692))


if __name__ == "__main__":
  unittest.main()

