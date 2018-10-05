# variables are the applicants
# domain is { spla, lahsa, denied }
# algorithm
# 1. loop through applicants and set the possible values based on constraints.
# 2. keep track of list of candidates that will maximize the efficiency for spla
# 3. loop through list and V

class SPLA:
    def __init__(self, num_spaces):
        self.num_spaces = num_spaces
        self.taken_spaces = {
                "monday": 0,
                "tuesday":0,
                "wednesday":0,
                "thursday":0,
                "friday":0,
                "saturday":0,
                "sunday":0 }
        self.efficiency = 0
        self.days_at_80_efficiency = 0

    def can_fit(self, applicant):
        for day_needed in applicant.days_needed:
            if self.taken_beds[day_needed] > num_spaces:
                return False
        return True

    def add_applicant(self, applicant):
        80_percent_full = self.taken_beds
        for day_needed in applicant.days_needed:
            if self.taken_beds[day_needed] += 1:
            self.efficiency += 1
            if self.taken_beds[day_needed] > num
        

class LAHSA:
    def __init__(self, num_beds):
        self.num_beds = num_beds
        self.taken_beds = {
                "monday": 0,
                "tuesday":0,
                "wednesday":0,
                "thursday":0,
                "friday":0,
                "saturday":0,
                "sunday":0 }
        self.efficiency = 0


def next_SPLA_applicant():
    input_file = open("input.txt")
    content = input_file.readlines()
    content = [line.strip() for line in content]
    num_beds = int(content[0])
    num_spaces = int(content[1])
    num_lahsa_chosen = int(content[2])

    # index for num_spla_chosen is 3 + num_lahsa_chosen.
    spla_chosen_index = 3 + num_lahsa_chosen
    num_spla_chosen = int(content[spla_chosen_index])
    
#    output_file = open("output.txt", "w")
#    output_file.write(str(max_activity) + "\n")
#    output_file.close()

