# variables are the applicants
# domain is { spla, lahsa, denied }
# algorithm
# 1. loop through applicants and set the possible values based on constraints.
# 2. keep track of list of candidates that will maximize the efficiency for spla
# 3. loop through list and V

import math

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
        80_percent_full = math.floor(self.num_spaces * 0.8)
        for day_needed in applicant.days_needed:
            if self.taken_beds[day_needed] += 1:
                self.efficiency += 1
            if self.taken_beds[day_needed] > 80_percent_full:
                self.days_at_80_efficiency += 1

    def days_at_80_efficiency(self):
        return self.days_at_80_efficiency

        

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
    # get num beds, num spaces
    num_beds = int(content[0])
    num_spaces = int(content[1])

    # get already chosen ID's
    num_lahsa_chosen = int(content[2])
    lahsa_chosen = set()

    current_index = 3
    for iteration in range(0, num_lahsa_chosen):
        lahsa_chosen.add(content[current_index])
        current_index += 1

    num_spla_chosen = int(content[current_index])
    spla_chosen = set()
    current_index += 1

    for iteration in range(0, num_spla_chosen):
        spla_chosen.add(content[current_index])
        current_index += 1

    # create applicants
    applicants = []
    num_total_applicants = int(content[current_index])
    current_index += 1
    for iteration in range(0, num_total_applicants):
        applicants.append(create_applicant(spla_chosen, lahsa_chosen, content[current_index]))
        current_index += 1

    # do backtracking algorithm

#    output_file = open("output.txt", "w")
#    output_file.write(str(max_activity) + "\n")
#    output_file.close()
    
def create_applicant(spla_chosen, 

