# Dalton Wright
# 10/31/24
# MergeSort

def merge_sort(nums):
  if len(nums) <= 1:
    return nums

  mid = int(len(nums)/2)

  left = (merge_sort(nums[:mid]))
  right = (merge_sort(nums[mid:]))

  return merge(left, right)

def merge(left,right):
  sorted_list = []
  left_index = 0
  right_index = 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] <= right[right_index]:
      sorted_list.append(left[left_index])
      left_index +=1
    else:
      sorted_list.append(right[right_index])
      right_index +=1
  
  while left_index < len(left):
    sorted_list.append(left[left_index])
    left_index +=1

  while right_index < len(right):
    sorted_list.append(right[right_index])
    right_index +=1

  return sorted_list















def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = merge_sort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()