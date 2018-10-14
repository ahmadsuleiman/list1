def first_last6(nums):
  return nums[0]==6 or nums[-1]==6

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
    return True
  return False
  
def make_pi():
  return [3,1,4]

def common_end(a, b):
  return a[0]==b[0] or a[-1]==b[-1]
  
def sum3(nums):
  return nums[0]+nums[1]+nums[2]
  
def rotate_left3(nums):
  nums[0],nums[1],nums[2]=nums[1],nums[2],nums[0]
  return nums

def reverse3(nums):
  a=nums[:]
  a.reverse()
  return a
  
def max_end3(nums):
  if nums[0]>nums[2]:
    nums[1]=nums[0];nums[2]=nums[0]
  else: nums[0]=nums[2];nums[1]=nums[2]
  return nums
  
def sum2(nums):
  if len(nums) >= 2:
    return nums[0]+nums[1]
  if len(nums)>0:
    return nums[0]
  return 0
  
def middle_way(a, b):
  x=[a[1],b[1]]
  return x
  
def make_ends(nums):
  n=[nums[0],nums[-1]]
  return n
  
def has23(nums):
  return 2 in nums or 3 in nums
  
