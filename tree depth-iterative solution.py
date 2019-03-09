#How deep is our tree ?
#Iterative solution------
def depth(tree):
    result = 0
    #our "queue" will strore nodes at each level
    queue = [tree]
    print(queue)
    #we loop as long as there are nodes to explore
    while queue:
        #count the number of child nodes
        count_level = len(queue)
        for child_count in range(0, count_level):
            #loop through each child
            child = queue.pop(0)
            #add its children to queue if they exist
            if child["left_child"]:
                queue.append(child["left_child"])
            if child["right_child"]:
                queue.append(child["right_child"])
        #count the levels
        result += 1

    return result
# TESTING
two_level_tree = {
"data": 6,
"left_child":
    {"data": 2},
"right_child":
{"data": 1}
}

four_level_tree = {
"data":54,
"right_child":
    {"data": 93,
     "left_child":
        {
         "data": 63,
         "left_child":
            {
            "data": 59
            }
        }
    }

}
depth(four_level_tree)
