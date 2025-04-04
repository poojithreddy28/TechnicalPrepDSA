# Problem 1: Finding the Perfect Cruise
# It's vacation time! Given an integer vacation_length and a list of integers cruise_lengths sorted in ascending order, use binary search to return True if there is a cruise length that matches vacation_length and False otherwise.

# def find_cruise_length(cruise_lengths, vacation_length):
# 	left, right = 0, len(cruise_lengths) - 1
# 	while left <= right:
# 		mid = (left + right) // 2
# 		if cruise_lengths[mid] == vacation_length:
# 			return True
# 		elif cruise_lengths[mid] < vacation_length:
# 			left = mid + 1
# 		else:
# 			right = mid - 1
# 	return False

# # Example Usage:

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
# # Example Output:

# # True
# # False



# def find_cabin_index(cabins, preferred_deck, left=None, right=None):
    # if left is None:
    #     left = 0
    # if right is None:
    #     right = len(cabins) - 1
    # mid = (left + right) // 2
    # if right < left:
    #     return mid+1
    # if cabins[mid] > preferred_deck:
    #     return find_cabin_index(cabins, preferred_deck, left, mid - 1)
    # elif cabins[mid] < preferred_deck:
    #     return find_cabin_index(cabins, preferred_deck, mid + 1, right)
    # else:
    #     return mid

# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))


# Problem 3: Count Checked In Passengers
# As a cruise ship worker, you're in charge of tracking how many passengers have checked in to their rooms thus far. You are given a list of rooms where passengers are either checked in (represented by a 1) or not checked in (represented by a 0). The list is sorted, so all the 0s appear before any 1s.

# Write a function count_checked_in_passengers() that efficiently counts and returns the total number of checked-in passengers (1s) in the list in O(log n) time.

# def count_checked_in_passengers(rooms):
#     left, right = 0, len(rooms) -1
#     while left<=right:
#         mid = (left + right) // 2
#         if rooms[mid] == 1 and rooms[mid-1]==0:
#             return len(rooms)-mid
#         elif rooms[mid] == 1:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return 0
# # left,right =0,len(rooms)-1
# # while left<=right:
# # Example Usage:

# rooms1 = [0, 1, 1, 1, 1, 1, 1] # 
# rooms2 = [0, 0, 0, 0, 0, 1]
# rooms3 = [0, 0, 0, 0, 0, 0]

# print(count_checked_in_passengers(rooms1)) 
# print(count_checked_in_passengers(rooms2))
# print(count_checked_in_passengers(rooms3))
# # Example Output:

# # 4
# # 1
# # 0





def is_profitable(excursion_counts, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(excursion_counts)
        
    if left > right:
        return -1
        
    mid = (left + right) // 2
    
    # Count excursions with at least mid passengers
    count = sum(1 for x in excursion_counts if x >= mid)
    
    if count == mid:
        return mid
    elif count > mid:
        return is_profitable(excursion_counts, mid + 1, right)
    else:  # count < mid
        return is_profitable(excursion_counts, left, mid - 1)


print(is_profitable([3, 5]))
print(is_profitable([0, 0]))