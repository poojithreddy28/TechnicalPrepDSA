# def get_artist_info(artist, festival_schedule):
#     if artist in festival_schedule:
#         return festival_schedule[artist]
#     else:
#         return {'message': 'Artist not found'}

# #TC : O(1)=
# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  


# Problem 4 Identify schedule conflicts

# Problem 5: Best set
def best_set(votes):
    count = {}
    max_votes = 0
    for vote in votes.values():
        if vote in count:
            count[vote] += 1
        else:
            count[vote] = 1
        if count[vote]>max_votes:
            max_votes = count[vote]
            max_singer = vote
    return max_singer
        
    # for i in count:
    #     if count[i]==max_votes:


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
}

print(best_set(votes1))
print(best_set(votes2))

#SZA
#Ethel Cain
#Note: SZA and Ethel Cain would both be acceptable answers for the second example
