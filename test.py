
# (())) 4 
def longestValidParentheses(s: str) -> int:
    levels = dict({0: 0})
    lvl_counter = 0
    stack = []
    stack_len = 0
    locals = []

    i = -1
    for p in s:
        i += 1
        if (p == '('):
            lvl_counter += 1
            levels[lvl_counter] = 0
            
            stack.append('(')
            stack_len += 1
            
            #local_len = 0

        elif  (p == ')'):
            if (stack_len > 0 and stack[stack_len-1] == '('):
                # local 
                levels[lvl_counter] += 1
                #local_len += 1
                lvl_counter -= 1

                stack.pop()
                stack_len -= 1

                if (lvl_counter + 1 in levels):
                    levels[lvl_counter] += levels[lvl_counter+1]
                    locals.append(levels[lvl_counter])

                levels[lvl_counter+1] = 0
            else: 
                stack.append(')')
                stack_len += 1
                locals.append(levels[lvl_counter])
                levels[lvl_counter] = 0
            
    return max(locals) * 2

def check(dp: dict, char, p) -> bool:
    drop_keys = []
    oks = dict({})

    for k in dp.keys():
        #print(dp[k], char)
        if (dp[k] == '*'):
            arg = p[k-1]
            if (arg == '.'):
                oks[k] = True
            elif (arg == char):
                oks[k] = True
            else: 
                drop_keys.append(k)
                oks[k] = False

        elif (dp[k] == '.'):
            oks[k] = True
            drop_keys.append(k)
        elif (dp[k] == char):
            oks[k] = True
            drop_keys.append(k)
        else:
            drop_keys.append(k)
            oks[k] = False
    
    res = any(oks.values())

    print("check")
    print(dp)
    print(oks)
    #print("check", dp, )
    for d in drop_keys:
        dp.pop(d)

    return res

def isMatch( str: str, p: str) -> bool:

    w = len(p)+1
    h = len(str) + 1

    dp = [[False for _ in range(w)] for _ in range(h)]
    dp[0][0] = True # ''=''
    
    for i in range(1, w):
        pchar = p[i-1]
        if (pchar == '*'):
            dp[0][i] = dp[0][i-2]

    """
        pattern
string   '' c   .   a   *   b
    ''   1  0   0   0   0   0
    a    0 
    b    0
    """

    for i in range(1, h):
        for j in range(1, w):
            # char . *
            pchar = p[j-1]
            schar = str[i-1]

            if (pchar == schar or pchar == '.'): # char or .
                prevMatch = dp[i-1][j-1]
                dp[i][j] = prevMatch
            
            if (pchar == '*'):
                # need take care zero match or one< match char
                # zero match: check previous pattern match [i-2][j]
                # one and more: check previuos pattern match [i][j-1]
                zeroMatch = dp[i][j-2]
                oneAndMore = dp[i-1][j]
                prevCharMatch = (schar == p[j-2]) or p[j-2] == '.' 
                dp[i][j] = zeroMatch or (oneAndMore and prevCharMatch)

    return dp[h-1][w-1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev = None
        ptr = head

        while(ptr != None):
            next = ptr.next
            ptr.next = prev
            ptr = next
            next.next = prev

        return head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        counter = 0
        res = ListNode(-1, None)
        res_t = res
        rev = []
        while(head != None):
            counter += 1
            rev.append(h)
            h = h.next
            
            if (counter == k):
                rev.reverse()
                for i in rev:
                    res_t.next = ListNode(i.val, None)
                    res_t = res_t.next

                counter = 0
        
        # add others
        for i in rev:
            res_t.next = ListNode(i.val, None)
            res_t = res_t.next

        return res

def print(head):
    ptr = head
    while(ptr != None):
        print(ptr.val)
        ptr = ptr.next

t = Solution()
ls = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
rv = t.reverseLinkedList(ls)
print(rv)

#print(isMatch(".a"))
#print(isMatch("abc"))
#print(isMatch("..."))
#print(isMatch("ab*"))


