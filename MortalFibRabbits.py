#! python3
# The idea this time is to create a running track of the number of youths
# born each month and use that to calculate the number of deaths each month

from sys import argv


def morfibrab(months, lifespan):
    # Primer
    adults = 0
    youth = 1
    dead = 0
    counter = [youth]
    lifespan = int(lifespan - 1)  # Turning it into base zero

    # Primary loop
    for i in range(months):
        pop = adults + youth
        print(f'''month = {i+1} \nadults = {adults} \nyouth = {youth} \ndead = {dead} \npop = {pop} \n-----------''')

        # Calculations for next months
        # adults, youth = adults + youth - dead, adults

        if i >= int(lifespan):
            dead = counter[int(i - lifespan)]
            adults, youth = adults + youth - dead, adults
            counter.append(youth)
        else:
            adults, youth = adults + youth - dead, adults
            counter.append(youth)

            # TODO: Try turning the 'counter' list into an iterable rather
            # than relying on i


months = int(argv[1])
lifespan = int(argv[2])
morfibrab(months, lifespan)
