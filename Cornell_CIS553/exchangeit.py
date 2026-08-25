"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Amelia Litvak
Date: 07/17/2025
"""
import currency
src=input("3-letter code for original currency: ")
dst=input("3-letter code for the new currency: ")
amt=input("Amount of the original currency: ")
amt_float=float(amt)
result=currency.exchange(src,dst,amt_float)
rounded_result=round(result,3)
result_string=str(rounded_result)
print("You can exchange "+amt+" "+src+" for "+result_string+" "+dst+".")