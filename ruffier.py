# here the lines which produce the result are given
txt_index = "Your Ruffier index: "
txt_workheart = "Heart efficiency: "
txt_nodata = '''there is no data for that age'''
txt_res = []
txt_res.append('''low.Go see your doctor ASAP!''')
txt_res.append('''satisfactory. Go see your doctor!''')
txt_res.append('''average. It might be worth additional tests at the doctor.''')
txt_res.append(''' higher than average''')
txt_res.append('''high''')

def ruffier_index(P1, P2, P3):
   return (4 * (P1+P2+P3) - 200) / 10

def neud_level(age):
   norm_age = (min(age, 15) - 7) // 2  # every two years the from age seven turns into one unit, all the way to age 15
   result = 21 - norm_age * 1.5 # every two years multiply the difference by 1.5, that's how the levels are arranged in the table
   return result
    
def ruffier_result(r_index, level):
   if r_index >= level:
       return 0
   level = level - 4 # this will not run if we already returned the answer “unsatisfactory”
   if r_index >= level:
       return 1
   level = level - 5 # analogously, we end up here if the level is, at minimum, “satisfactory”
   if r_index >= level:
       return 2
   level = level - 5.5 # next level
   if r_index >= level:
       return 3
   return 4 # we end up here if the index is less than all the intermediate levels, that is, the tested circle.

def test(P1, P2, P3, age):
   if age < 7:
       return (txt_index + "0", txt_nodata) # this is a mystery beyond this test
   else:
       ruff_index = ruffier_index(P1, P2, P3) # calculation
       result = txt_res[ruffier_result(ruff_index, neud_level(age))] # the interpretation and conversion of the numeric preparation level into text data
       res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
       return res
