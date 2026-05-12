class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        
        # range(start, stop, step) -> starts at last index, ends at 0
        for i in range(len(arr) - 1, -1, -1):
            # We need to save the current value before we overwrite it
            current_val = arr[i]
            
            # Replace current with the max we found earlier
            arr[i] = rightMax
            
            # Update the max for the NEXT element to the left
            if current_val > rightMax:
                rightMax = current_val
                
        return arr