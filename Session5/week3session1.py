def is_valid_post_format(posts):
    opens = []
    for post in posts:
        if post == "(" or post == "[" or post == "{":
            opens.append(post)
        else:
            if not opens:
                return False
            elif post == ")" and opens[-1]=="(":
                opens.pop()
            elif post == "]" and opens[-1]=="[":
                opens.pop()
            elif post == "}" and opens[-1]=="{":
                opens.pop()
    return True if not opens else False


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}"))
print(is_valid_post_format("(]"))
print(is_valid_post_format("([)]")) # False


# True
# True
# False


# Problem 2: Reverse User Comments Queue

def reverse_comments_queue(comments):
    comments_queue = []
    for i in range(len(comments)):
        comments_queue.append(comments.pop())
    return comments_queue

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
# Example Output:

# ['Thanks for sharing.', 'Love it!', 'Great post!']
# ['Well written.', 'Interesting read.', 'First!']


# Problem 3: Check Symmetry in Post Titles
# As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):
    title = title.lower().replace(" ", "")
    left =0
    right = len(title)-1
    while left<right:
        if title[left]!=title[right]:
            return False
        left+=1
        right-=1
    return True
        

# Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
# Example Output:

# True
# False


# Problem 4: Engagement Boost
# You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

# Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Your Task:

# Read through the existing solution and add comments so that everyone in your pod understands how it works.
# Modify the solution below to use the two-pointer technique.
def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

# Example Usage:

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
# Example Output:

# [0, 1, 9, 16, 100]
# [4, 9, 9, 49, 121]

