class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Time Complexity: O(N) -  Need to iterate over all letters in s
        # Space Complexity O(N) - Need to iterate over all elements in stack, which could be all n elements in s
        
        # store matching closing pairs
        stack = []

        # Store the match pair of brackets for each letter
        close_to_open = { ']': '[', '}':'{', ')':'('}

        # Iterate across the letters in the string S
        for letter in s:
            # Check if the current letter is a closing 
            if letter in close_to_open:
                # if closing, check top of stack if it exists and matches corresponding open
                # for closing
                if stack and stack[-1] == close_to_open[letter]:
                    # IF matching open and close, pop the top of the stack
                    stack.pop()
                else:
                    # Otherwise mismatch which means paranthesis input is invalid, must return
                    # False
                    return False
            # Encounter open paranthesis, can add to stack
            else:
                stack.append(letter)

        # Finally, valid paranthesis only occurs when open/closing pairs cancels 
        # and stack is empty. Only return true if stack is empty otherwise return
        # False.
        return True if not stack else False

