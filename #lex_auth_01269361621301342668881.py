#lex_auth_01269361601342668881
no_of_adult=3
no_of_children=4
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    rate=37550
    rate_adult_tax=(107/100)*rate
    rate_child_tax=(rate/3)*1.07
    total_ticket_cost=rate_child_tax*no_of_children+rate_adult_tax*no_of_adult
    total_ticket_cost=.9*total_ticket_cost
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program

total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)