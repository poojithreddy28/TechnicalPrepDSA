# Problem 1: Manage Performance Stage Changes
# At a cultural festival, multiple performances are scheduled on a single stage. However, due to last-minute changes, some performances need to be rescheduled or canceled. The festival organizers use a stack to manage these changes efficiently.

# You are given a list changes of strings where each string represents a change action. The actions can be:

# "Schedule X": Schedule a performance with ID X on the stage.
# "Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
# "Reschedule": Reschedule the most recently canceled performance to be the next on stage.
# Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

def manage_stage_changes(changes):
    stack = []
    for change in changes:
        if change[0] == "S":
            stack.append(change[-1])
        elif change[0] == "C":
            if stack:
                temp  = stack.pop()
        elif change[0] == "R":
            if stack:
                stack.append(temp)
    return stack

# Example Usage:

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

# Example Output:

# ["A", "C", "B", "D"]
# []
# ["Z"]



# Problem 2: Queue of Performance Requests
# You are organizing a festival and want to manage the queue of requests to perform. Each request has a priority. Use a queue to process the performance requests in the order they arrive but ensure that requests with higher priorities are processed before those with lower priorities. Return the order in which performances are processed.
import heapq
def process_performance_requests(requests):
    heap = []
    for priority, request in requests:
        heapq.heappush(heap, (-priority, request))
    return [request for _, request in heap]

# Example Usage:

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
# Example Output:

# ['Music', 'Dance', 'Drama']
# ['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
# ['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']
