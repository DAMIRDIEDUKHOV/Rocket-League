txt_index = "Your ruffier index:"
txt_workheart = "Heart efficiency:"
txt_nodata = "No data for this age."
txt_res = []
txt_res.append("Low. Consoult a doctor immedialtely.")
txt_res.append("Satisfactory. Consoult a doctor.")
txt_res.append("Average. It may be worth an additional examination by a doctor.")
txt_res.append("Higher than average.")
txt_res.append("High")

def ruffier_index(P1, P2, P3):
    return (4*(P1 + P2 + P3) - 200) / 10

def neud_level(age):
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age * 1.5
    return result

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level -= 4
    
    if r_index >= level:
        return 1
    level -= 5
    
    if r_index >= level:
        return 2
    level -= 5.5
    
    if r_index >= level:
        return 3
    return 4

def test(P1, P2, P3, age):
    if age < 7:
        return (txt_index + "0", txt_nodata)
    else:
        ruff_index = ruffier_index(P1, P2, P3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + str(ruff_index) + "\n" + txt_workheart + result
        return res