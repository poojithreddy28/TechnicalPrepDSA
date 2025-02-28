def most_endangered(species_list):
    min_population = species_list[0]["population"]
    for species in species_list:
        if species["population"] < min_population:
            min_population = species["population"]
            most_endangered_species = species["name"]
            
    return most_endangered_species

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))


def navigate_research_station(station_layout, observations):
    dic = {}
    counter = 0
    for i,j in enumerate(station_layout):
        dic[j] = i
    counter = dic[observations[0]]
    for i in range(len(observations)-1):
        counter += abs(dic[observations[i]] - dic[observations[i+1]])
    return counter
    
    

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

# 45
# 4
# Example 2 explanation: The index moves from 0 to 2 to observe 'c', then to 1 for
# 'b', then to 0 again for 'a'.
# Total time = 2 + 1 + 1 = 4.


# Problem 4: Prioritizing Endangered Species Observations
# In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.

# Write a function prioritize_observations() that sorts the elements of observed_species such that the relative ordering of items in observed_species matches that of priority_species. Species that do not appear in priority_species should be placed at the end of observed_species in ascending order.

def prioritize_observations(observed_species, priority_species):
    prioritized_list = []
    
    # Add all occurrences of each priority species to the prioritized list
    for species in priority_species:
        while species in observed_species:
            prioritized_list.append(species)
            observed_species.remove(species)
    
    # Sort the remaining species and extend the prioritized list with them
    prioritized_list.extend(sorted(observed_species))
    
    return prioritized_list


observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

# Expected Output:
# ["🐯", "🐯", "🐯", "🦌", "🐘", "🦁", "🦁", "🐍", "🐻", "🦑", "🐼"]
# ["cardinal", "sparrow", "bluejay", "crow", "robin"]