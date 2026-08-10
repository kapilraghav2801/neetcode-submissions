class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)

        else:
            current_min = min(value, self.min_stack[-1])
            self.min_stack.append(current_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# =================================================
# Companies Asking This Question (Frequency)
# =================================================
# 
# [0 - 3 months -- MAY - JULY 2026]
# - Google: 4
# - Microsoft: 4
# - Amazon: 4
# - Meta: 2
# - Infosys: 2
# 
# [0 - 6 months -- FEB - JULY 2026]
# - Bloomberg: 7
# - Lyft: 2
# - UiPath: 2
# - Odoo: 2
# 
# [6 months ago -- PRIOR TO FEB 2026]
# - Apple: 13
# - Oracle: 12
# - Yandex: 10
# - Paytm: 8
# - Salesforce: 6
# - LinkedIn: 5
# - TCS: 4
# =================================================