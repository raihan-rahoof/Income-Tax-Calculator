from abc import ABC, abstractmethod


# abstract taxSlab class
class TaxSlab(ABC):
    @abstractmethod
    def calculate(self,income:float)->float:
        pass

class GenericTaxSlab(TaxSlab):
    def __init__(self,lower_limit:float,upper_limit:float,rate:float):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.rate = rate
    
    def calculate(self, income: float) -> float:
        if income > self.lower_limit:
            applicable_income = min(income,self.upper_limit) if self.upper_limit else income
            taxable_amount = applicable_income - self.lower_limit
            return taxable_amount * self.rate
        return 0

class IncomeTaxCalculator:
    def __init__(self , slabs:list[TaxSlab]):
        self.slabs = slabs
    
    def calculate_total_tax(self,income:float)->float:
        total_tax = 0
        for slab in self.slabs:
            total_tax +=slab.calculate(income)
        return total_tax
    
        