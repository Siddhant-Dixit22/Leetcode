## Container With Most Water - Medium

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## Solution Submitted

        left_poi = 0
        right_poi = len(height) - 1
        curr_area = min(height[left_poi], height[right_poi]) * (right_poi - left_poi)
        max_area = curr_area

        while (left_poi != right_poi):
            if (height[left_poi] <= height[right_poi]):
                left_poi += 1
            elif (height[left_poi] > height[right_poi]):
                right_poi -= 1

            curr_area = min(height[left_poi], height[right_poi]) * (right_poi - left_poi)

            if (curr_area > max_area):
                max_area = curr_area
                print("New max area: " + str(max_area))
        

        return max_area


        ## Second Attempt

        # second_list = [] * len(height)
        # for i in height:
        #     second_list.append(i)

        # max_height = max(height)
        # second_list.remove(max_height)
        # second_highest_height = max(second_list)

        # if (second_highest_height < max_height/2):
        #     width = abs(height.index(second_highest_height) - height.index(max_height))
        #     return second_highest_height * width

        # curr_area = 0
        # max_area = 0

        # for i in range(len(height)):
        #     if height[i] < max_height / 2:
        #         continue
        #     for j in range(len(height)):
        #         if height[j] < max_height / 2:
        #             continue
        #         if i == j:
        #             continue
        #         if i > j:
        #             continue
        #         width = j - i
        #         if height[i] > height[j]:
        #             curr_area = height[j] * width
        #         elif height[j] > height[i]:
        #             curr_area = height[i] * width
        #         else:
        #             curr_area = height[i] * width

        #         if curr_area > max_area:
        #             max_area = curr_area

        # return max_area


        ## Brute Force

        # curr_area = 0
        # max_area = 0

        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         if (i == j):
        #             continue
        #         if (i > j):
        #             continue
        #         width = j - i
        #         if (height[i] > height[j]):
        #             curr_area = height[j] * width
        #         elif (height[j] > height[i]):
        #             curr_area = height[i] * width
        #         else:
        #             curr_area = height[i] * width
                
        #         if (curr_area > max_area):
        #             max_area = curr_area
        
        # return max_area