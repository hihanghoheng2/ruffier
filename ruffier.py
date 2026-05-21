
# here you can specify the strings representing the result:
txt_index = "Your Ruffier Index: "
txt_workheart = "Cardiac performance: "
txt_nodata = ''' no data for this age'''
txt_res = []
txt_res.append('''low.Urgently consult the doctor!''')
txt_res.append('''satisfactory.Consult the doctor!''')
txt_res.append('''average.It may be worth an additional consultation of the doctor.''')
txt_res.append('''above average''')
txt_res.append('''high''')


def ruffier_index(P1, P2, P3):
   return (4 * (P1+P2+P3) - 200) / 10


def neud_level(age):
   norm_age = (min(age, 15) - 7) // 2  # for the age up to 15, every 2 years of the difference between the age and 7 years should be taken as 1
   result = 21 - norm_age * 1.5 # every 2 years of the difference should be multiplied by 1.5; this way the levels in the table are distributed
   return result
  
def ruffier_result(r_index, level):
   if r_index >= level:
       return 0
   level = level - 4 # this will not be executed if we have already returned the "unsatisfactory" response
   if r_index >= level:
       return 1
   level = level - 5 # similarly, we get here if the level is at least "satisfactory"
   if r_index >= level:
       return 2
   level = level - 5.5 # next level
   if r_index >= level:
       return 3
   return 4 # we are here if the index is less than all the intermediate levels; i.e. the tested person has great results.


def test(P1, P2, P3, age):
   if age < 7:
       return (txt_index + "0", txt_nodata) # the enigma not intended for this test
   else:
       ruff_index = ruffier_index(P1, P2, P3) # calculation
       result = txt_res[ruffier_result(ruff_index, neud_level(age))] # the interpretation; conversion the numeric value of the fitness level into a text
       res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
       return res
