class Solution:
    def maxArea(self, height: List[int]) -> int:
        wall_left = 0
        wall_right = len(height) - 1
        V_max = 0
        V = 0
        while wall_left < wall_right:
            width = wall_right - wall_left
            V = width * min(height[wall_left], height[wall_right])
            if V > V_max:
                V_max = V
            if height[wall_left] < height[wall_right]:
                wall_left += 1
            else:
                wall_right -= 1
        return V_max
            