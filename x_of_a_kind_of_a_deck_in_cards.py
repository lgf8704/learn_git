class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        # # deck中只有1个元素，返回False
        # if len(deck) == 1:
        #     return False

        # # 定义纸牌频数的字典，也可以用
        # dic = {}

        # for i in deck:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1

        # nums = []
        # for v in dic.values():
        #     # 某个元素的个数为1，无法分组，返回False
        #     if v == 1:
        #         return False
        #     nums.append(v)

        # min_num = min(nums)
        # j = 2
        # while j <= min_num:
        #     for i in nums:
        #         if i % j == 0:
        #             continue
        #         else:
        #             break
        #     else:
        #         return True
            
        #     j += 1
        
        # return False

        from math import gcd
        from functools import reduce
        import collections

        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2
		

if __name__ == "__main__":

	# 测试
	Solution.hasGroupsSizeX([1,2,3,4,4,3,2,1])