# 常用枚举技巧
## 枚举右、维护左
对于双变量问题，例如两数之和 $a_i+a_j=target$ ，可以枚举右边的 $a_j$ ，转换成单变量问题，也就是在 $a_j$ 左边查找是否有 $a_i=target-a_j$ ，这种查找遍历过的元素的思想，可以使用哈希表解决。
### 1. [两数之和](https://leetcode.cn/problems/two-sum/description/)
**题目描述**：给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** _`target`_  的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

**示例 1：**
**输入：**` nums = [2,7,11,15], target = 9`
**输出：**`[0,1]`
**解释：** `因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。`

#### 算法思路与总结
暴力算法很好想到，这里不做解释，主要解释一下为什么本题可以使用哈希表解决。

#### 算法实现
```java
class Solution {  
    public int[] twoSum(int[] nums, int target) {  
  
        HashMap<Integer, Integer> hashMap = new HashMap<>();  
        for(int j = 0; ;j++){  // 枚举右边的 j
	        // 判断左边是否存在 ai，ai+aj=target
            if(hashMap.containsKey(target - nums[j])){  
                return new int[]{hashMap.get(target - nums[j]),j};  
            }else{ 
	            // 如果不存在这样的ai，就把已经遍历到的元素作为新的 (key,value) 加入哈希表中
                hashMap.put(nums[j],j);  
            }  
        }  
    }  
}
```
# 基础算法 - 滑动窗口
## 什么是滑动窗口 Sliding Window
滑动窗口算法可以用来解决数组/字符串的子元素问题，它可以将嵌套的循环问题，转换为单循环问题，解决时间复杂度。
**如何识别滑动窗口？**
1. 连续的元素，比如：string, subarray, LinkedList
2. min, max, longest, shortest, key word
### 基本题型
1. Easy, size fixed. 窗口长度确定， 比如 max sum of size = k
2. Median, size 可变，单限制条件
3. Median, size 可变，双限制条件，比如 longest substring with distinct character
4. Hard, size fix, 单限制条件


## 定长滑动窗口
通用套路：[[灵茶山艾府基础算法笔记整理#定长滑动窗口|定长滑动窗口的固定套路以 1456 为例]]
### 209.[长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)
给定一个含有 `n` 个正整数的数组和一个正整数 `target` **。**

找出该数组中满足其总和大于等于 `target` 的长度最小的 **子数组** `[numsl, numsl+1, ..., numsr-1, numsr]` ，并返回其长度。**如果不存在符合条件的子数组，返回 `0` 。

**示例 1：**
**输入：** `target = 7, nums = [2,3,1,2,4,3]`
**输出：** `2`
**解释：** `子数组[4,3]是该条件下的长度最小的子数组。`

#### 算法思路与总结
**暴力解法：** 分别遍历子数组的左端点和右端点，遍历过程中对子数组求和，记录每个子数组的长度，从而找到和大于 target 的子数组的最短长度。这种解法虽然直观，但是时间复杂度非常高 $O(n^2)$，暴力解法会超过题目的时间复杂度。

**滑动窗口解法：**
暴力解法其实没有用到数组中的都是正整数这个性质，也就是说，如果某个子数组元素和是大于 target 的，那么拓展右端点后所有子数组的和都是大于 target 的，因为希望找到子数组的最短长度，所以这部分拓展右端点是没有意义的。拓展右端点行不通的话，我们可以尝试缩短左端点，每次缩短左端点以后再求子数组的和是否大于 target。
这种情况下，原问题就可以通过遍历右端点，然后缩短左端点，每次记录下满足题目要求的子数组的长度。因为在窗口滑动过程中，最多只会遍历一次数组，所以时间复杂度为 $O(n)$，相比于暴力解法，时间复杂度上优化了很多。

#### 算法实现
```java
class Solution {  
    public int minSubArrayLen(int target, int[] nums) {  
        // 滑动窗口模板题  
        // 首先枚举右端点，查找 >= target 的子数组  
        int sum = 0;  
        int left = 0;  
        int min = Integer.MAX_VALUE;  
        for(int right = 0; right < nums.length; right++){  
            sum += nums[right];  
            // 找到一个右端点, 判断左端点是否可以移动  
            while(sum - nums[left] >= target){  
                // 移动左端点  
                sum -= nums[left];  
                left++;  
            }
            // 移动完左端点，判断一下当前子数组是否满足要求，计算该子数组的长度。
            if(sum >= target){  
                min = Math.min(min, right - left + 1);  
            }
        }
        // 如果最小值记录的是初始值，说明没有能够满足条件的子数组，返回 0
        if(min == Integer.MAX_VALUE){  
            return 0;  
        }else{  
	        // 否则，返回满足条件的子数组的长度
            return min;  
        }  
    }  
}
```

### 1456. [定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/)
#### 算法思路与总结
标准的定长滑动窗口题目，在写过 209 变长滑动窗口以后，定长滑动窗口就很简单了。
#### 算法实现
```java
class Solution {  
    public int maxVowels(String s, int k) {  
        int ans = Integer.MIN_VALUE;  
        int left = 0;  
        int res = 0;  
        // 计算初始窗口中的元音个数  
        for(int i = 0; i < k; i++){  
            if(isVowel(s.charAt(i))){  
                res++;  
            }  
        }  
        ans = res;  
        // 滑动定长窗口  
        for(int right = k; right < s.length(); right++){  
            // 避免索引越界  
            if(right == s.length()){  
                break;  
            }  
            if(isVowel(s.charAt(right))){  
                if(!isVowel(s.charAt(left))){  
                    res++;  
                }  
            }else{  
                if(isVowel(s.charAt(left))){  
                    res--;  
                }  
            }  
            // 移动窗口后比较 res 是否大于 ans            if(res > ans){  
                ans = res;  
            }  
            left++;  
        }  
        return ans;  
    }  
    public boolean isVowel(char c){  
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){  
            return true;  
        }else{  
            return false;  
        }  
    }  
}
```
### 1423. [可获得的最大点数](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/)
【中等题】
题目描述：
几张卡牌 **排成一行**，每张卡牌都有一个对应的点数。点数由整数数组 `cardPoints` 给出。
每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 `k` 张卡牌。
你的点数就是你拿到手中的所有卡牌的点数之和。
给你一个整数数组 `cardPoints` 和整数 `k`，请你返回可以获得的最大点数。

**示例 1：**
**输入：** `cardPoints = [1,2,3,4,5,6,1], k = 3`
**输出：** `12`
**解释：** 第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。

**提示：**
- `1 <= cardPoints.length <= 10^5`
- `1 <= cardPoints[i] <= 10^4`
- `1 <= k <= cardPoints.length`
#### 算法思路与总结
看了这道题的官方提示（Let the sum of all points be total_pts. You need to remove a sub-array from cardPoints with length n - k.）以后，其实就能把这个问题很快的转换成一个标准的定长滑动窗口的模板题。其实就是找到一个长度为 `n-k`的连续子数组，并且要求子数组的元素之和最小。
![[leetcode 1432 转换为固定长度滑动窗口图示]]
有了整个题目的思路以后，就可以很容易的实现整个算法。
#### 算法实现
```java
class Solution {

public int maxScore(int[] cardPoints, int k) {
	int total = 0;
	// 转换为子数组和最小的问题
	int ans = Integer.MAX_VALUE;
	int tmp = 0;
	int left = 0;

	for(int i = 0; i < cardPoints.length - k; i++){
		total += cardPoints[i];
		tmp += cardPoints[i];
	}
	if(tmp < ans){
	
		ans = tmp;
	}
	// 开始滑动窗口
	for(int right = cardPoints.length - k; right < cardPoints.length; right++){
		tmp += cardPoints[right];
		total += cardPoints[right];
		tmp -= cardPoints[left];
		if(tmp < ans){
			ans = tmp;
		}
		left++;
	}
	return total - ans;
	}
}
```
## 可变长度滑动窗口
可变长度滑动窗口与固定长度滑动窗口的最大区别就是题目中是否给定了窗口的长度，一般来说，固定长度的滑动窗口会接收两个输入，一个输入是给定的字符串/数组，另一个输入就是滑动窗口的窗口大小。
可变长度的滑动窗口题目特征是需要求窗口的最长、最短结果。比如下面这几道题：
### 3. [无重复子串的最大长度](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
【中等题】
给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长 子串** 的长度。

**示例 1:**
**输入:** `s = "abcabcbb"`
**输出:** `3 `
**解释:** 因为无重复字符的最长子串是 `"abc"`，所以其长度为 3。

**示例 2:**
**输入:** `s = "bbbbb"`
**输出:** `1`
**解释:** 因为无重复字符的最长子串是 `"b"`，所以其长度为 1。

**提示：**
- `0 <= s.length <= 5 * 104`
- `s` 由英文字母、数字、符号和空格组成

注意点：字符串子序列和字符串子串的区别：
1. **子串 (Substring)**  
   - 必须连续  
   - 示例：`"abcde"` 的子串 → `"bcd"`（连续字符）

2. **子序列 (Subsequence)**  
   - 可不连续（但顺序不变）  
   - 示例：`"abcde"` 的子序列 → `"ace"`（跳过 `b` 和 `d`）
**关键区别**：子串像截取片段，子序列像按顺序挑字符。
#### 算法思路
本来想使用哈希表 HashMap 来解决出现次数的问题，但是越写复杂度越高，最后发现可以使用一个长度为 128 的字符数组来统计所有字母、数字、符号和空格的出现次数，相比使用哈希表时间复杂度要高的多，可以这样使用的原因是 ASCII 码表可以将字母、数字、符号和空格转换成一个特定的数字，从而映射到字符数组的下标，字符数组中的元素代表出现次数（其实这种思路也是一种哈希算法）。然后在根据滑动窗口解题套路写算法。
#### 算法实现
```java
class Solution {  
    public int lengthOfLongestSubstring(String s) {  
        char[] array = s.toCharArray();  
        if(array.length == 0){  
            return 0;  
        }  
        int ans = Integer.MIN_VALUE;  
        int tmp = 0;  
        int[] count = new int[128];  
        int left = 0;  
        for(int right = 0; right < array.length; right++){  
            count[array[right]]++;  
            tmp++;  
            while(count[array[right]] > 1){  
                count[array[left]]--;  
                left++;  
                tmp--;  
            }  
  
            if(tmp > ans){  
                ans = tmp;  
            }  
        }  
        return ans;  
    }  
}
```
### 1493. [删掉一个元素以后全为 1 的最长子数组](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/description/)
给你一个二进制数组 `nums` ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。

**提示 1：**
**输入：** `nums = [1,1,0,1]`
**输出：** `3`
**解释：** 删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。

**示例 2：**
**输入：**` nums = [0,1,1,1,0,1,1,0,1]`
**输出：** `5`
**解释：** 删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。

**提示：**
- `1 <= nums.length <= 105`
- `nums[i]` 要么是 `0` 要么是 `1` 。

#### 算法思路
#### 算法实现

## summary Sliding Window
1. Sliding Window 套路模板时间复杂度一般为 O(n)
2. 一般 String 使用 map 作为 window，如果说明了只有小写字母也可以用 `int[26]`，如果说明了是 ASCII 字符，可以使用 `int[256]`。
3. 多重限制条件的压轴题需要考虑是否为单调队列。
4. 字母类还可以暴力尝试 26 个字母，比如 1 个 unique，2 个 unique，让后内部使用模板
5. Exact(k) 可以转换为 atMost(k) - atMost(k - 1)

# 线性数据结构
## 数组
### 704. [二分查找](https://leetcode.cn/problems/binary-search/description/)

**题目描述**：给定一个 `n` 个元素有序的（升序）整型数组 `nums` 和一个目标值 `target`  ，写一个函数搜索 `nums` 中的 `target`，如果目标值存在返回下标，否则返回 `-1`。

  
**示例 1:**

**输入:** `nums = [-1,0,3,5,9,12], target = 9
**输出:** `4`
**解释:** 9 出现在 `nums` 中并且下标为 4

**示例 2:**

**输入:** `nums = [-1,0,3,5,9,12], target = 2`
**输出:** `-1`
**解释:** 2 不存在 `nums` 中因此返回 -1

**提示：**

1. 你可以假设 `nums` 中的所有元素是不重复的。
2. `n` 将在 `[1, 10000]`之间。
3. `nums` 的每个元素都将在 `[-9999, 9999]`之间。
#### 算法思路
标准的二分搜索模板题目，没有什么可以讲的思路。下面几道题目也是二分查找有关的题目。
#### 算法实现
```java
class Solution {  
    public int search(int[] nums, int target) {  
        int left = 0;  
        int right = nums.length - 1;  
        while(left <= right){  
            if(target > nums[(left + right) / 2]){  
                left = ((left + right) / 2) + 1;  
            }else if(target < nums[(left + right) / 2]){  
                right = ((left + right) / 2) - 1;  
            }else{  
                return (left + right) / 2;  
            }  
        }  
        return -1;  
    }  
}
```
### 35. [搜索插入位置](https://leetcode.cn/problems/search-insert-position/description/)
**题目描述：**
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 `O(log n)` 的算法。

**示例 1:**
**输入:** `nums = [1,3,5,6], target = 5`
**输出:** `2`

**示例 2:**
**输入:**` nums = [1,3,5,6], target = 2`
**输出:** `1`
#### 算法思路与刷题总结
自己在做这道题目的时候想法比较简单，其实就是先找到数组中是否有一个元素的值可以和 target 相等。如果有的话直接返回这个元素的下标，但是如果没有的话就根据 `nums[middle]` 与 `target`的大小关系来决定在哪里插入 target 的值。
虽然成功解决了这道题目但是花费的思考时间有点太长了，感觉对于一道简单题来说还是有一些复杂，并且空间复杂度也不是最优。
总结一下官方提供的题解：==其实对于所有没有找到 target 的情况，left 指针指向的 Index 就是待插入的位置，通过手动模拟这个过程就可以知道！说一自己代码里面的条件判断其实没有用。==

#### 算法实现
```java
class Solution {  
    public int searchInsert(int[] nums, int target) {  
        int left = 0;  
        int right = nums.length - 1;  
        int middle = 0;  
        while(left <= right){  
            middle = (left + right) / 2;  
            if(target > nums[(left + right) / 2]){  
                left = middle + 1;  
            }else if(target < nums[middle]){  
                right = middle - 1;  
            }else{  
                return middle;  
            }  
        }  
        // 改进前的算法
        if(nums[middle] > target){  
            return middle;  
        }else{  
            return middle + 1;  
        }
	    // 改进后的算法
	    return left;
    }  
}
```
### 1007. [行相等的最少多米诺旋转](https://leetcode.cn/problems/minimum-domino-rotations-for-equal-row/description/)
【题目描述】在一排多米诺骨牌中，`tops[i]` 和 `bottoms[i]` 分别代表第 `i` 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 —— 该平铺的每一半上都有一个数字。）

我们可以旋转第 `i` 张多米诺，使得 `tops[i]` 和 `bottoms[i]` 的值交换。

返回能使 `tops` 中所有值或者 `bottoms` 中所有值都相同的最小旋转次数。

如果无法做到，返回 `-1`.
**示例 1：**

![](https://assets.leetcode.com/uploads/2021/05/14/domino.png)

**输入：** `tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]`
**输出：** `2`
**解释：** 
图一表示：在我们旋转之前， tops 和 bottoms 给出的多米诺牌。 如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。
#### 算法思路与总结

#### 算法实现
```java
class Solution {  
    public int minDominoRotations(int[] tops, int[] bottoms) {  
  
        int topCount;  
        int bottomCount;  
        boolean flag;  
        int target;  
        for(int i = 1; i <= 6; i++){  
            topCount = 0;  
            bottomCount = 0;  
            flag = true;  
            target = tops.length;  
            for(int index = 0; index < tops.length; index++){  
  
                if(tops[index] != i && bottoms[index] != i){  
                    flag = false;  
                    break;  
                }  
                if(tops[index] == i && bottoms[index] != i){  
                    topCount++;  
                }  
                if(bottoms[index] == i && tops[index] != i){  
                    bottomCount++;  
                }  
                if(bottoms[index] == i && tops[index] == i){  
                    target--;  
                }  
            }  
            if(topCount + bottomCount >= target && flag){  
                if(topCount > bottomCount){  
                    return bottomCount;  
                }else{  
                    return topCount;  
                }  
            }  
        }  
        return -1;  
    }  
}
```
## 栈
### 94. [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)
【简单题】
给定一个二叉树的根节点 `root` ，返回 _它的 **中序** 遍历_ 。

**示例 1：**
![[二叉树的中序遍历.png]]
```
输入：root = [1,null,2,3]
输出：[1,3,2]
```
示例 2：
```
输入：root = []
输出：[]
```
**提示：**
- 树中节点数目在范围 `[0, 100]` 内
- `-100 <= Node.val <= 100`
**进阶:** ==递归算法很简单，你可以通过迭代算法完成吗？==
#### 递归算法实现
相关知识点：[[数据结构与 Java#线性表：栈]]
```java
/**  
 * Definition for a binary tree node. 
 * public class TreeNode {
 *     int val; 
 *     TreeNode left; 
 *     TreeNode right;
 *     TreeNode() {} 
 *     TreeNode(int val) { this.val = val; } 
 *     TreeNode(int val, TreeNode left, TreeNode right) { 
 *         this.val = val; 
 *         this.left = left; 
 *         this.right = right; 
 *     } 
 * } 
 */
 
class Solution {  
    public List<Integer> inorderTraversal(TreeNode root) {  
        List<Integer> list = new ArrayList<>();  
        inOrder(root,list);  
        return list;  
    }  
    public void inOrder(TreeNode root, List<Integer> list){  
        if(root == null){  
            return ;  
        }  
        inOrder(root.left, list);  
        list.add(root.val);  
        inOrder(root.right, list);  
    }  
}
```
#### 迭代算法实现
到这里有点不清楚，因为不知道如何设置迭代条件，但是想到了可以再创建一个 List 来存放每个二叉树结点，方便进行回溯之类的操作。

### 232 [用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/)
【简单题】
队列相关内容：[[数据结构与 Java#线性表：队列]]
#### 题目描述
请你==仅使用两个栈实现先入先出队列==。队列应当支持一般队列支持的所有操作（`push`、`pop`、`peek`、`empty`）实现 `MyQueue` 类：

- `void push(int x)` 将元素 x 推到队列的末尾
- `int pop()` 从队列的开头移除并返回元素
- `int peek()` 返回队列开头的元素
- `boolean empty()` 如果队列为空，返回 `true` ；否则，返回 `false`

**说明：**

- 你 **只能** 使用标准的栈操作 —— **也就是只有 `push to top`, `peek/pop from top`, `size`, 和 `is empty` 操作是合法的。**
- 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

**提示：**
- `1 <= x <= 9`
- 最多调用 `100` 次 `push`、`pop`、`peek` 和 `empty`
- 假设所有操作都是有效的 （例如，一个空的队列不会调用 `pop` 或者 `peek` 操作）

**进阶：**

- 你能否实现每个操作均摊时间复杂度为 `O(1)` 的队列？换句话说，执行 `n` 个操作的总时间复杂度为 `O(n)` ，即使其中一个操作可能花费较长时间。

经过几次思考以后终于成功实现了，太不容易了😭。在学习过程中看到了一种很有意思的思考方法，那就是把两个栈底部平行相接，**一边是负责入队的 StackIn 栈，另一个是负责出队的 StackOut 栈**。这里以 数字 1 为例，在进入 StackIn 的时候，1 压在了栈底（但是由于栈先进先出的特点，所以会最后一个出栈 StackIn）然后进入 StackOut 以后，就是在栈顶的元素了。从而使用两个栈实现了队列的操作。
![[双栈实现队列]]

#### 算法实现：
```java
package DatastructureWithJava.test;  
import java.util.Stack;  
  
/**  
 * 使用两个栈实现先进先出的队列  
 */  
class MyQueue {  
  
    Stack<Integer> StackIn = new Stack<>();  
    Stack<Integer> StackOut = new Stack<>();  
    
    public MyQueue() {}  
  
    // 队列的入队操作，这一部是最简单的。只需要将目标元素压入 StackIn    public void push(int x) {  
        StackIn.push(x);  
    }  
  
    // 出队操作  
    public int pop() {  
        // 判断 StackOut 是否为空，不为空的情况下才能出栈。  
        // StackOut 的栈顶元素就是队列的队尾元素  
        if(!StackOut.empty()){  
            return StackOut.pop();  
        }  
        // 如果 StackOut 为空，说明元素在 StackIn 中，需要将其转换到 StackOut 中  
        else{  
            while(!StackIn.empty()){  
                StackOut.push(StackIn.pop());  
            }  
            return StackOut.pop();  
        }  
    }  
  
    // 获取队尾元素的方法和出队操作类似  
    public int peek() {  
        if(!StackOut.empty()){  
            return StackOut.peek();  
        }  
        else{  
            while(!StackIn.empty()){  
                StackOut.push(StackIn.pop());  
            }  
            return StackOut.peek();  
        }  
    }  
    public boolean empty() {  
        return (StackIn.empty() && StackOut.empty());  
    }  
}  
  
/**  
 * Your MyQueue object will be instantiated and called as such: 
 * MyQueue obj = new MyQueue(); 
 * obj.push(x); 
 * int param_2 = obj.pop(); 
 * int param_3 = obj.peek(); 
 * boolean param_4 = obj.empty(); 
 */
```

### 150. [逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/)
==【中等题】栈最经典的题目。==
**题目描述：**
给你一个字符串数组 `tokens` ，表示一个根据 逆波兰表示法表示的算术表达式。
请你计算该表达式。返回一个表示表达式值的整数。

**注意：**
- 有效的算符为 `'+'`、`'-'`、`'*'` 和 `'/'` 。
- 每个操作数（运算对象）都可以是一个整数或者另一个表达式。
- 两个整数之间的除法总是 **向零截断** 。
- 表达式中不含除零运算。
- 输入是一个根据逆波兰表示法表示的算术表达式。
- 答案及所有中间计算结果可以用 **32 位** 整数表示。

**示例 1：**

**输入：** `tokens = ["2","1","+","3","*"]`
**输出：** `9`
**解释：**  `该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9`

**逆波兰表达式：**

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

- 平常使用的算式则是一种中缀表达式，如 `( 1 + 2 ) * ( 3 + 4 )` 。
- 该算式的逆波兰表达式写法为 `( ( 1 2 + ) ( 3 4 + ) * )` 。

逆波兰表达式主要有以下两个优点：
- 去掉括号后表达式无歧义，上式即便写成 `1 2 + 3 4 + *` 也可以依据次序计算出正确结果。
- 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
#### 算法思路与总结

看完波兰表达式的定义其实差不多思路就有了，就是根据当前遍历到的元素判断是运算符还是数字，如果是运算符就取出栈顶的两个元素，计算运算结果，然后再压到栈中；如果是数字就直接把这个数字压入栈中。

用时: 32 m 10 s  花费时间这么长主要是因为在字符串转换为数字过程中一直在想怎么做，本来打算通过字符数组来转换发现根本通过不了，然后才知道 Integer 类里面封装好了通过 String 对象转换数字的静态方法；另外一个问题就是由于栈的特性，如果遇到 “-” “/” 这两种操作数有序的运算符，需要好好考虑一下出栈数字的顺序，否则也会错误。
- [x] 总结如何将字符串 或者 字符 转换为 int 类型的数字(@2025-05-04 23:30)

#### 算法实现
```java
class Solution {  
    public int evalRPN(String[] tokens) {  
        Stack<Integer> stack = new Stack<>();  
  
        for(String str : tokens){  
  
            if(str.equals("*")){  
                int num1 = stack.pop();  
                int num2 = stack.pop();  
                stack.push(num1 * num2);  
  
            }else if(str.equals("-")){  
                int num1 = stack.pop();  
                int num2 = stack.pop();  
                stack.push(num2 - num1);  
            }else if(str.equals("/")){  
                int num1 = stack.pop();  
                int num2 = stack.pop();  
                stack.push((int)(num2 / num1));  
  
            }else if(str.equals("+")){  
                int num1 = stack.pop();  
                int num2 = stack.pop();  
                stack.push(num1 + num2);  
            }else{  
                // 把字符串转换为 int 类型  
                int num = Integer.parseInt(str);  
                stack.push(num);  
            }  
        }  
        return stack.pop();  
    }  
}
```

### 225. [用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/description/?envType=problem-list-v2&envId=stack)

**题目描述**：
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（`push`、`top`、`pop` 和 `empty`）。

实现 `MyStack` 类：

- `void push(int x)` 将元素 x 压入栈顶。
- `int pop()` 移除并返回栈顶元素。
- `int top()` 返回栈顶元素。
- `boolean empty()` 如果栈是空的，返回 `true` ；否则，返回 `false` 。

**注意：**

- 你只能使用队列的标准操作 —— 也就是 `push to back`、`peek/pop from front`、`size` 和 `is empty` 这些操作。
- 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

**示例：**

**输入：**
`["MyStack", "push", "push", "top", "pop", "empty"]
`[[], [1], [2], [], [], []]`
**输出：**
`[null, null, null, 2, 2, false]`

**解释：**
```
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False
```
#### 算法思路与总结
【简单题】仍然做的比较困难，想不到如何用两个队列实现栈。然后看了一个题解的动画演示，顿时明白了，其实难点就是在向队列中添加元素的时候，怎么模拟出栈的效果。动画演示就是：先把所有主队列中的元素添加到副队列中，然后把元素添加到主队列中，然后再将副队列中的元素添加到主队列中，模拟过一次就能够发现，可以实现先进后出的效果，其实就是使用一个队列暂存了先进的元素，让先进的元素实际上后进，从而实现通过先进先出的数据结构实现先进后出的数据结构。
#### 算法实现
```java
class MyStack {  
    private Queue<Integer> queue1;  
    private Queue<Integer> queue2;  
  
    public MyStack() {  
        queue1 = new LinkedList<Integer>();  
        queue2 = new LinkedList<Integer>();  
    }  
  
    public void push(int x) {  
        if(queue1.isEmpty()){  
            queue1.add(x);  
        }else{  
            while(!queue1.isEmpty()){  
                queue2.add(queue1.remove());  
            }  
            queue1.add(x);  
            while(!queue2.isEmpty()){  
                queue1.add(queue2.remove());  
            }  
        }  
    }  
  
    public int pop() {  
        return queue1.remove();  
    }  
  
    public int top() {  
        return queue1.peek();  
    }  
  
    public boolean empty() {  
        return queue1.isEmpty();  
    }  
}  
  
/**  
 * Your MyStack object will be instantiated and called as such: * MyStack obj = new MyStack(); * obj.push(x); * int param_2 = obj.pop(); * int param_3 = obj.top(); * boolean param_4 = obj.empty(); */
```

## 链表
### 203 [移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/submissions/624693677/)
**题目描述**：
给你一个链表的头节点 `head` 和一个整数 `val` ，请你删除链表中所有满足 `Node.val == val` 的节点，并返回 **新的头节点** 。
示例 1：

![](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

**输入：** `head = [1,2,6,3,4,5,6], val = 6`
**输出：** `[1,2,3,4,5]`

示例 2：
**输入：** `head = [], val = 1`
**输出：** `[]`

示例 3：
**输入：** `head = [7,7,7,7], val = 7`
**输出：**`[]`
#### 算法思路
在初步思考解法的时候，就发现了在移除元素的时候处理头结点和处理一般的结点不一样，所以如果使用一般方法对链表中的每个元素值进行判断的话需要对头结点加上特殊的处理。在看了代码随想录中这一道题的解法以后，意识到对于这种需要判断头结点的题目，可以在链表前面加上一个虚拟的头结点，这样对于链表中的每一个结点都可以使用一般方法来进行判断。
#### 算法实现 - 带有虚拟头结点
```java
/**  
 * Definition for singly-linked list.
 * public class ListNode { 
 *     int val; 
 *     ListNode next; 
 *     ListNode() {} 
 *     ListNode(int val) { this.val = val; } 
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; } 
 * } */
 class Solution {
    public ListNode removeElements(ListNode head, int val) {  
        if(head == null){  
            return null;  
        }  
        ListNode preHead = new ListNode();  
        preHead.next = head;  
        ListNode node = preHead;  
        while(node.next != null){  
            if(node.next.val == val){  
                node.next = node.next.next;  
            }  
            else{  
                node = node.next;  
            }  
        }  
        head = preHead.next;  
        return head;  
    }  
}
```
#### 算法实现 - 不带虚拟头结点

#### 存在的问题
1. *首先就是使用 while 循环的时候忘记设置迭代条件*。导致每次 leetcode 提交的时候遇到「执行超时」的报错，其实就是 while 循环没有办法跳出。在看了题解以后才意识到没有设置变量迭代。
2. 思路不清晰，代码效率不高。典型的地方就是在删除元素的时候考虑尾结点，但是稍微画图思考一下就可以知道没有必要在删除尾结点的时候加上判断。*优化以后执行时间快了很多*。![[为何链表在删除尾结点的时候不需判断是否为空]]
### 206. 反转链表
【简单题】
**题目描述：**
给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

**输入：** `head = [1,2,3,4,5]`
**输出：**`[5,4,3,2,1]`
#### 算法思路与总结
感觉有点难的简单题，双指针的思路非常简单，但是实现过程中有很多细节容易写错。比如在反转一次以后，应该以怎样的顺序更新双指针，决定了算法能否 ac。
其实最重要的就是对于链表这种数据结构，==更新指针指向之前都要考虑一下这样的操作会不会导致丢失指针/元素==。

![[双指针实现反转链表]]
#### 算法实现
**双指针：**
```java
class Solution {  
    public ListNode reverseList(ListNode head) {  
        ListNode pre = new ListNode();  
        ListNode cur = new ListNode();  
        pre = null;  
        cur = head;  
        while(cur != null){  
            ListNode tmp = new ListNode();  
            tmp = cur.next;  
            cur.next = pre;  
            pre = cur;  
            cur = tmp;  
        }  
        return pre;  
    }  
}
```

### 92. [反转链表 ||](https://leetcode.cn/problems/reverse-linked-list-ii/submissions/627027356/)
**题目描述：**

#### 算法思路与总结

#### 算法实现
```java
class Solution {  
    public ListNode reverseBetween(ListNode head, int left, int right) {  
        ListNode dummy = new ListNode();  
        dummy.next = head;  
  
        ListNode p0 = new ListNode();  
        p0 = dummy;  
        for(int i = 1; i < left; i++){  
            p0 = p0.next;  
        }  
  
        ListNode pre = new ListNode();  
        ListNode cur = new ListNode();  
        cur = p0.next;  
        for(int i = 1; i <= right - left + 1; i++){  
            ListNode tmp = new ListNode();  
            tmp = cur.next;  
            cur.next = pre;  
            pre = cur;  
            cur = tmp;  
        }  
        p0.next.next = cur;  
        p0.next = pre;  
        return dummy.next;  
    }  
}
```
## 字符串
### 242. [有效的字母异位词](https://leetcode.cn/problems/valid-anagram/)
**题目描述**:
给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的字母异位词。

> **字母异位词**是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次。

**示例 1:**
**输入:**` s = "anagram", t = "nagaram"`
**输出:** `true`

**示例 2:**
**输入:** `s = "rat", t = "car"`
**输出:** `false`

**提示:**

- `1 <= s.length, t.length <= 5 * 104`
- `s` 和 `t` 仅包含小写字母

#### 算法思路与总结
解题思路其实非常简单，就是把两个字符串排序以后按照顺序比较一下每个字符，如果有不同的字符直接返回假即可。做完这部分内容才知道对于数组 Arrays 类、字符串 String 类的方法又忘记地差不多了。
- [x] 复习 Java 字符串 (@2025-05-09)

#### 算法实现
自己实现的版本：
```java
class Solution {  
    public boolean isAnagram(String s, String t) {  
        if(s.length() != t.length()){  
            return false;  
        }  
        char[] s1 = s.toCharArray();  
        char[] t1 = t.toCharArray();  
        Arrays.sort(s1);  
        Arrays.sort(t1);  
        for(int i = 0; i < s1.length; i++){  
            if(s1[i] != t1[i]){  
                return false;  
            }  
        }  
        return true;  
    }  
}
```
跟官方题解对比一下多使用了一层循环，导致时空复杂度都有一点不好。
更优雅的做法是：
```java
class Solution {  
    public boolean isAnagram(String s, String t) {  
        if(s.length() != t.length()){  
            return false;  
        }  
        char[] s1 = s.toCharArray();  
        char[] t1 = t.toCharArray();  
        Arrays.sort(s1);  
        Arrays.sort(t1);  
        return Arrays.equals(s1,t1);  
    }  
}
```
### 344. [反转字符串](https://leetcode.cn/problems/reverse-string/submissions/627858700/)
#### 算法思路与总结
比较简单，就是把输入的字符数组翻转过来
#### 算法实现
```java
class Solution {  
    public void reverseString(char[] s) {  
        for(int i = 0; i < s.length / 2; i++){  
            char tmp = s[i];  
            s[i] = s[s.length - i - 1];  
            s[s.length - i - 1] = tmp;  
        }  
    }  
}
```
# 数据结构 - 哈希表
## 884.[两句话中的不常见单词](https://leetcode.cn/problems/uncommon-words-from-two-sentences/)
【简单题】1200 档
**题目描述：** **句子** 是一串由空格分隔的单词。每个 **单词** 仅由小写字母组成。
如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 **没有出现** ，那么这个单词就是 **不常见的** 。
给你两个 **句子** `s1` 和 `s2` ，返回所有 **不常用单词** 的列表。返回列表中单词可以按 **任意顺序** 组织。

**示例 1：**

**输入：** `s1 = "this apple is sweet", s2 = "this apple is sour"`
**输出：**`["sweet","sour"]`
### 算法思路与总结
看到这道题目的时候其实就想到了要用哈希表，键设计为存储单词，值设计为这个单词出现的次数。因为哈希表查找 Key 的时间复杂度为 O(1)，所以整个算法的时间复杂度就是O(n)，n 为两个字符串数组的最大长度。
### 算法实现
```java
class Solution {  
    public String[] uncommonFromSentences(String s1, String s2) {  
        HashMap<String,Integer> hashMap1 = new HashMap<>();  
        String[] arr1 = s1.split(" ");  
        for(int i = 0; i < arr1.length; i++){  
            if(!hashMap1.containsKey(arr1[i])){  
                hashMap1.put(arr1[i],1);  
            }else{  
                int count = hashMap1.get(arr1[i]);  
                count++;  
                hashMap1.put(arr1[i],count);  
            }  
        }  
  
        HashMap<String,Integer> hashMap2 = new HashMap<>();  
        String[] arr2 = s2.split(" ");  
        for(int i = 0; i < arr2.length; i++){  
            if(!hashMap2.containsKey(arr2[i])){  
                hashMap2.put(arr2[i],1);  
            }else{  
                int count = hashMap2.get(arr2[i]);  
                count++;  
                hashMap2.put(arr2[i],count);  
            }  
        }  
        ArrayList<String> ls = new ArrayList<>();  
        for(Map.Entry<String, Integer> entry : hashMap1.entrySet()){  
            if(entry.getValue() == 1){  
                String key = entry.getKey();  
                if(!hashMap2.containsKey(key)){  
                    ls.add(key);  
                }  
            }  
        }  
        for(Map.Entry<String, Integer> entry : hashMap2.entrySet()){  
            if(entry.getValue() == 1){  
                String key = entry.getKey();  
                if(!hashMap1.containsKey(key)){  
                    ls.add(key);  
                }  
            }  
        }  
        return ls.toArray(new String[0]);  
    }  
}
```
## 2260. 必须拿起的最小连续卡牌数
【中等题】
**题目描述：**
给你一个整数数组 `cards` ，其中 `cards[i]` 表示第 `i` 张卡牌的 **值** 。如果两张卡牌的值相同，则认为这一对卡牌 **匹配** 。

返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 `-1` 。

**示例 1：**

**输入：** `cards = [3,4,2,3,4,7]`
**输出：** `4`
**解释：** `拿起卡牌 [3,4,2,3] 将会包含一对值为 3 的匹配卡牌。注意，拿起 [4,2,3,4] 也是最优方案。`

### 算法思路与刷题总结
本题其实就是找到数组中出现相同元素的最短连续子数组。理解题目以后不难知道本题是关于哈希表与滑动窗口的问题。
那么关键问题就转换为了，哈希表中应该存储什么内容？
最开始思考的是使用哈希表存储每个元素出现的次数，然后利用滑动窗口的思想，遍历滑动窗口右窗口，维护滑动窗口的左窗口，如果遇到出现次数超过两次的元素，那么就移动左窗口，直到出现次数刚好为两次，记录此时的窗口长度，如果小于最小值，就记录下来。
### 算法实现
```java
class Solution {  
    public int minimumCardPickup(int[] cards) {  
        HashMap<Integer,Integer> hashMap = new HashMap<>();  
        int ans = Integer.MAX_VALUE;  
        for(int i = 0; i < cards.length; i++){  
            if(!hashMap.containsKey(cards[i])){  
                hashMap.put(cards[i], i);  
            }else{  
                int dist = i - hashMap.get(cards[i]) + 1;  
                if(dist < ans){  
                    ans = dist;  
                }  
                hashMap.put(cards[i],i);  
            }  
        }  
        if(ans == Integer.MAX_VALUE){  
            return -1;  
        }else{  
            return ans;  
        }  
    }  
}
```
## 36. [有效的数独](https://leetcode.cn/problems/valid-sudoku/description/)
【中等题】请你判断一个 `9 x 9` 的数独是否有效。只需要 **根据以下规则** ，验证已经填入的数字是否有效即可。

1. 数字 `1-9` 在每一行只能出现一次。
2. 数字 `1-9` 在每一列只能出现一次。
3. 数字 `1-9` 在每一个以粗实线分隔的 `3x3` 宫内只能出现一次。（请参考示例图）

**注意：**

- 一个有效的数独（部分已被填充）不一定是可解的。
- 只需要根据以上规则，验证已经填入的数字是否有效即可。
- 空白格用 `'.'` 表示。
**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png)

**输入：

```
board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
**输出：** true
### 算法思路与总结
本质上不算太难的一道题，但是关键就是如何用数组来实现一个哈希表统计每个数字出现的次数。尤其是对于每个 $3*3$ 的子二维数组中如何统计出现次数。
比如，对于任意一个在九宫格里面的格子 $borad[i][j]$ 如何找到这个格子属于九宫格的哪一个区域。规律就是：
$$
box_n = (j/3) * 3 + i/3
$$
统计 $borad[i][j]$ 属于九宫格的哪一个格子是因为题目中要求了对于每个格子里面，0-9 的每个数字只能最多出现一次。从而使用一个二维数组` box[boxn][curnum]`，统计每个数字在九宫格里面出现的次数。

![[有效的数独图解.png]]
### 代码实现
```java
class Solution {  
    public boolean isValidSudoku(char[][] board) { 
	    // 分别代表行哈希表 
        boolean row[][] = new boolean[9][9];  
        // 列哈希表
        boolean col[][] = new boolean[9][9];  
        // 九宫格哈希表
        boolean box[][] = new boolean[9][9];  
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
	            // 如果格子是 “。” 说明是空白格，直接跳过剩下的循环
                if(board[i][j] == '.')  
                    continue;
                // 计算哈希值
                int curNum = board[i][j] - '1';  
                // 查找哈希表是否存在元素，存在说明不满足有效的数独
                if(row[i][curNum])  
                    return false;  
                if(col[j][curNum])  
                    return false;
                // 计算当前小格子在哪个九宫格里面  
                int boxNum = j / 3 + (i / 3) * 3;  
                if(box[boxNum][curNum])  
                    return false;  
                row[i][curNum] = true;  
                col[j][curNum] = true;  
                box[boxNum][curNum] = true;  
            }  
        }  
        return true;  
    }  
}
```


# 二叉树
## 遍历二叉树


### LCP 44. [开幕式烟火](https://leetcode.cn/problems/sZ59z6/)
【简单题】
「力扣挑战赛」开幕式开始了，空中绽放了一颗二叉树形的巨型焰火。 给定一棵二叉树 `root` 代表焰火，节点值表示巨型焰火这一位置的颜色种类。请帮小扣计算巨型焰火有多少种不同的颜色。

**示例 1：**
> 输入：`root = [1,3,2,1,null,2]
> 输出：`3`
> 解释：焰火中有 3 个不同的颜色，值分别为 1、2、3

**示例 2：**
> 输入：`root = [3,3,3]`
> 输出：`1`
> 解释：焰火中仅出现 1 个颜色，值为 3

**提示：**
- `1 <= 节点个数 <= 1000`
- `1 <= Node.val <= 1000`
#### 算法思路
这道题其实就是比较简单的二叉树遍历问题，只需要遍历节点值的出现次数即可，记录在这里的原因是通过本题，学习了如何使用 HashSet，在这题之前，针对元素出现次数的问题都是使用 HashMap 解决的，相比 HashSet 复杂了不少。
#### 算法实现
1 使用 HashMap 解决本题：
```java
class Solution {
    HashMap<Integer, Integer> hashMap = new HashMap<>();
    public int numColor(TreeNode root) {
        
        int ans = 0;
        dfs(root);
        return hashMap.size();
    }
    public void dfs(TreeNode node){
        if(node == null)
            return;
        if(!hashMap.containsKey(node.val)){
            hashMap.put(node.val, 1);
        }else{
            int cnt = hashMap.get(node.val);
            hashMap.put(node.val, cnt+1);
        }
        dfs(node.left);
        dfs(node.right);
    }
}
```

2 使用 HashSet 优化逻辑：
```java
class Solution {
    HashSet<Integer> hashSet = new HashSet<>();
    public int numColor(TreeNode root) {
        
        int ans = 0;
        dfs(root);
        return hashSet.size();
    }
    public void dfs(TreeNode node){
        if(node == null)
            return;
        hashSet.add(node.val);
        dfs(node.left);
        dfs(node.right);
    }
}
```
### 104. [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)
**题目描述：** 给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

**输入：** `root = [3,9,20,null,null,15,7]`
**输出：** `3`

**示例 2：**

**输入：** `root = [1,null,2]`
**输出：** `2`
#### 算法思路与总结
本题的解法其实不难想到，就是使用深度优先搜索+递归的思路确定二叉树的最大深度，但是虽然思路简单，代码实现却怎么都想不到。看了官方题解其实也不难，问题点应该在于 DFS 递归应该如何设计、如何设计递归的结束条件。有关的使用深度优先搜索的题目非常多，并且大部分都是有关二叉树的，可以说二叉树这种数据结构天然就适合使用深度优先搜索。

#### 算法实现
```java
class Solution {  
    public int maxDepth(TreeNode root){  
        if(root == null){  
            return 0;  
        }else{  
            int maxLeft = maxDepth(root.left) + 1;  
            int maxRight = maxDepth(root.right) + 1;  
            return Math.max(maxLeft,maxRight);  
        }  
    }  
}
```

### 637. [二叉树的层平均值](https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/)
【简单题】最不像简单题的简单题，感觉不管使用深度优先还是广度优先难度都比较大。
**题目描述：** 
给定一个非空二叉树的根节点 `root` , 以数组的形式返回每一层节点的平均值。与实际答案相差 `10-5` 以内的答案可以被接受。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

**输入：** `root = [3,9,20,null,null,15,7]`
**输出：**`[3.00000,14.50000,11.00000]`
**解释：** 第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 `[3, 14.5, 11]` 。
#### 算法思路
**广度优先搜索：** 使用广度优先搜索解决
#### 算法实现
**广度优先搜索：**
```java
class Solution {  
    public List<Double> averageOfLevels(TreeNode root) {  
        List<Double> ls = new ArrayList<>();  
  
        Queue<TreeNode> queue = new LinkedList<>();  
        queue.add(root);  
        long sum = 0;  
        while(!queue.isEmpty()){  
            int size = queue.size();  
            sum = 0;  
            for(int i = 0; i < size; i++){  
                TreeNode node = queue.poll();  
                sum += node.val;  
                if(node.left != null){  
                    queue.add(node.left);  
                }  
                if(node.right != null){  
                    queue.add(node.right);  
                }  
            }  
            double tmp = (double) sum / size;  
            ls.add(tmp);  
        }  
        return ls;  
    }  
}
```

### 102. [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)
**题目描述：**
给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**输入：**` root = [3,9,20,null,null,15,7]`
**输出：** `[[3],[9,20],[15,7]]`
#### 算法思路与总结
手撕的另一道中等题，有了上面一题作为基础思路，其实后面相关类型的题目都非常好做了，手撕起来也很快，差不多能够达到十分钟一题的速度。
- [x] 这道题目里面稍微难一点的可能就是有关嵌套 List 如何进行初始化的问题。(@2025-04-30 20:00)
#### 算法实现
**广度优先搜索：** 
```java
class Solution {  
    public List<List<Integer>> levelOrder(TreeNode root) {  
  
        Queue<TreeNode> queue = new LinkedList<>();  
        List<List<Integer>> res = new LinkedList<>();  
  
        if(root == null){  
            return res;  
        }  
  
        queue.add(root);  
        while(!queue.isEmpty()){  
            List<Integer> tmp = new LinkedList<>();  
            int size = 0;  
            size = queue.size();  
            for(int i = 0; i < size; i++){  
                TreeNode node = queue.poll();  
  
                tmp.add(node.val);  
                if(node.left != null){  
                    queue.add(node.left);  
                }  
                if(node.right != null){  
                    queue.add(node.right);  
                }  
            }  
            res.add(tmp);  
        }  
        return res;  
    }  
}
```

### 515. [在每个树行中找最大值](https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/)
**题目描述：**
#### 算法思路
#### 算法实现
**广度优先搜索：**
```java
class Solution {  
    public List<Integer> largestValues(TreeNode root) {  
        List<Integer> ls = new LinkedList<>();  
        Queue<TreeNode> queue = new LinkedList<>();  
  
        if(root == null){  
            return ls;  
        }  
  
        queue.add(root);  
        while(!queue.isEmpty()){  
            int size = queue.size();  
            int max = Integer.MIN_VALUE;  
            for(int i = 0; i < size; i++){  
                TreeNode node = new TreeNode();  
                node = queue.poll();  
                if(node.val > max){  
                    max = node.val;  
                }  
                if(node.right != null){  
                    queue.add(node.right);  
                }  
                if(node.left != null){  
                    queue.add(node.left);  
                }  
            }  
            ls.add(max);  
        }  
        return ls;  
    }  
}
```
### 515. [在每个树中找最大值](https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/)
**题目描述：** 给定一棵二叉树的根节点 `root` ，请找出该二叉树中每一层的最大值。

**示例1：**

![](https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg)

**输入:**` root = [1,3,2,5,3,null,9]`
**输出:** `[1,3,9]`
#### 算法思路与总结
经过前面一题的训练，这一题使用广度优先搜索可以直接手撕了，虽然是一道中等题，但是做题过程中的算法思路特别清晰。对于这种**满足某种条件**的广度优先搜索也总结了一下自己的套路：
1. 初始化相关数据以及要返回的值。（比如要找到的最大值，要求的平均值，使用广度优先搜索需要借助的数据结构队列）
2. 如果解题思路中需要使用到每个结点的层次（高度），就需要在广度优先搜索的循环中继续嵌套一层循环（用于一次性将所有同一层次的结点出队列，从而对同一层次的结点实现相同的操作）。循环的跳出条件一般是超出队列中元素的个数。

总的来说，==核心思想还是：结点入队，结点出队、判断左右子树是否为空，将左右子树结点入队。==通过在这个基础上添加各种判断完成不同的操作。
#### 算法实现
```java
class Solution {  
    public List<Integer> largestValues(TreeNode root) {  
        List<Integer> ls = new LinkedList<>();  
        Queue<TreeNode> queue = new LinkedList<>();  
  
        if(root == null){  
            return ls;  
        }  
  
        queue.add(root);  
        while(!queue.isEmpty()){  
            int size = queue.size();  
            int max = Integer.MIN_VALUE;  
            for(int i = 0; i < size; i++){  
                TreeNode node = new TreeNode();  
                node = queue.poll();  
                if(node.val > max){  
                    max = node.val;  
                }  
                if(node.right != null){  
                    queue.add(node.right);  
                }  
                if(node.left != null){  
                    queue.add(node.left);  
                }  
            }  
            ls.add(max);  
        }  
        return ls;  
    }  
}
```
### 513. [找树左下角的值](https://leetcode.cn/problems/find-bottom-left-tree-value/description/)
【题目难度】中等
**题目描述：**
给定一个二叉树的 **根节点** `root`，请找出该二叉树的 **最底层 最左边** 节点的值。

假设二叉树中至少有一个节点。

**示例 1:**

![](https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg)

**输入:** `root = [2,1,3]`
**输出:** `1`
#### 算法思路与总结
看了灵神的题解，才知道本题最简单解法的思路。要找到最底层最左边结点，可以利用广度优先搜索的特性：按照层次遍历二叉树，所以我们不难发现这样的规律，既广度优先搜索中最后队列中存储的结点，一定是二叉树的叶子结点。这个特性就解决了本题中需要找到最底层结点的问题。至于对于最左边的结点，可以这样思考，每次总是先加入结点的右子树，然后再加入结点的左子树，然后出队操作正常执行，当最后队列为空的时候，最后一个移除的结点就是最坐下角的结点。
#### 算法实现
使用 Queue 实现
```java
class Solution {  
    public int findBottomLeftValue(TreeNode root) {  
        ArrayList<TreeNode> queue = new ArrayList<>();  
        queue.add(root);  
        TreeNode tmp = null;  
        while(queue.size() != 0){  
            tmp = queue.remove(0);  
            if(tmp.right != null){  
                queue.add(tmp.right);  
            }  
            if(tmp.left != null){  
                queue.add(tmp.left);  
            }  
        }  
        return tmp.val;  
    }  
}
```
### 二叉树的右视图
【中等题】
给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**示例 1：**

**输入：** `root = [1,2,3,null,5,null,4]`

**输出：** `[1,3,4]`

**解释：**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

**示例 2：**

**输入：** `root = [1,2,3,4,null,null,null,5]`

**输出：** `[1,3,4,5]`

**解释：**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)
#### 算法思路
本题思考的时候想到了先遍历右子树，然后再遍历左子树，根据每个结点的深度判断当前结点是否能够从右边看到，但是在具体实现的时候完全没有实现的思路，看了灵神的题解才有了题目的思路，后续需要好好复习，对于这种需要在 DFS 中更新数据、维护数据的题目还是比较弱。
#### 算法实现
```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        dfs(root, 0, ans);
        return ans;
    }
    public void dfs(TreeNode node, int depth, List<Integer> ans){
        if(node == null){
            return;
        }
        // 代表某个深度的元素第一次遇到
        if(depth == ans.size()){
            ans.add(node.val);
        }
        dfs(node.right, depth + 1, ans);
        dfs(node.left, depth + 1, ans);
    }
}
```

## 完全二叉树
### 222. [完全二叉树的结点个数](https://leetcode.cn/problems/count-complete-tree-nodes/description/)
**题目描述：** 给你一棵 **完全二叉树** 的根节点 `root` ，求出该树的节点个数。
**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)

**输入：** `root = [1,2,3,4,5,6]`
**输出：** `6`
#### 算法思路与总结

简单的做法就是使用递归实现深度优先搜索，或者借助队列实现广度优先搜索。递归实现的时候思路有些不清晰，统计结点个数要么就是忘记加上左右子树的和，要么就是统计的时候多统计了。相比而言广度优先搜索实现起来思路超级清晰。

#### 算法实现
**一般递归做法：**
```java
class Solution {  
    public int countNodes(TreeNode root) {  
        int left = 0;  
        int right = 0;  
        if(root == null){  
            return 0;  
        }  
        if(root.left != null){  
            left = countNodes(root.left);  
        }  
        if(root.right != null){  
            right = countNodes(root.right);  
        }  
        return (left + right + 1);  
    }  
}
```
## 二叉搜索树
### 700. [二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/description/)
**题目描述：** 给定二叉搜索树（BST）的根节点 `root` 和一个整数值 `val`。

你需要在 BST 中找到节点值等于 `val` 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 `null` 。
**示例 1:**

![](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)

**输入：** `root = [4,2,7,1,3], val = 2`
**输出：**`[2,1,3]`
####  算法思路
[[数据结构与 Java#二叉搜索树的操作]]
#### 算法实现
```java
/**  
 * Definition for a binary tree node. * public class TreeNode { *     int val; 
 *     TreeNode left; 
 *     TreeNode right; 
 *     TreeNode() {} 
 *     TreeNode(int val) { this.val = val; } 
 *     TreeNode(int val, TreeNode left, TreeNode right) { 
 *         this.val = val; 
 *         this.left = left; 
 *         this.right = right; 
 *     } 
 * } 
 * */
 class Solution {  
    public TreeNode searchBST(TreeNode root, int val) {  
        while(root != null){  
            if(root.val < val){  
                root = root.right;  
            }else if(root.val > val){  
                root = root.left;  
            }else{  
                return root;  
            }  
        }  
        return null;  
    }  
}
```
### 701.  [二叉搜索树中的插入操作](https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/)
【中等题】
**题目描述：** 
给定二叉搜索树（BST）的根节点 `root` 和要插入树中的值 `value` ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 **保证** ，新值和原始二叉搜索树中的任意节点值都不同。

**注意**，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 **任意有效的结果** 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg)

**输入：** `root = [4,2,7,1,3], val = 5`
**输出：**`[4,2,7,1,3,5]`
**解释：** 另一个满足题目要求可以通过的树是：
![](https://assets.leetcode.com/uploads/2020/10/05/bst.jpg)

#### 算法思路与总结
自己手撕这道中等题的时候，思路参考了《Hello 算法》里面有关二叉搜索树中插入元素的算法步骤，确实是最符合直觉的一种 “搜索-插入” 思路。具体详见：[[数据结构与 Java#二叉搜索树的操作#插入结点]]。这种做法感觉本质上还是一种双指针的做法，pre 指针指向 node 上一个位置，node 遍历到 null 的时候退出循环，然后再比较一次 pre.val 和 val 的大小就知道应该插入到哪个位置。最后还多花费了一次比较的时间。

在看官方题解的时候也学习了递归做法，虽然有一点不符合直觉，但是优点是算法的空间复杂度比较低。



#### 算法实现
```java
/**  
 * Definition for a binary tree node. 
 * public class TreeNode { 
 *     int val; 
 *     TreeNode left; 
 *     TreeNode right; 
 *     TreeNode() {} 
 *     TreeNode(int val) { this.val = val; } 
 *     TreeNode(int val, TreeNode left, TreeNode right) { 
 *         this.val = val; 
 *         this.left = left; 
 *         this.right = right; 
 * } 
 * } 
 **/
 class Solution {  
    public TreeNode insertIntoBST(TreeNode root, int val) {  
        if(root == null){  
            return new TreeNode(val);  
        }  
  
        TreeNode pre = new TreeNode();  
        TreeNode node = new TreeNode();  
        node = root;  
        while(node != null){  
            if(node.val < val){  
                pre = node;  
                node = node.right;  
            }else{  
                pre = node;  
                node = node.left;  
            }  
        }  
        if(pre.val < val){  
            pre.right = new TreeNode(val);  
        }  
        else{  
            pre.left = new TreeNode(val);  
        }  
        return root;  
    }  
}
```

# 算法 - 前缀和
前缀和，就是从 nums 数组中的第 0 个位置开始累加，到第 i 个位置的累加结果，我们常把这个结果保存到数组 preSum 中，记为 `preSum[i]`。
计算前缀和的公式 `preSum[i] = presum[i-1] + nums[i]`，为了防止当 `i = 0`的时候数组越界，可以加上 if 判断。

在其他写法中，为了省略这个 if 条件判断，常常把前缀和数组的长度定义为原数组长度 + 1。preSum 的第 0 个位置，相当于一个占位符，置为 0。这样就可以把前缀和的公式统一为：`preSum[i] = presum[i-1] + nums[i-1]`，此时的 `preSum[i]` 表示 nums 中 i 元素左边所有元素之和（不包括元素 i ）。

![动图理解前缀和](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f565174445c94fa09f038d261602ffd4~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp)
前缀和的作用：
- 用数组求前 i 个数之和
- 求数组的区间和
前缀和部分基础题如下。
## 经典题型

### 303. [区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/description/)
给定一个整数数组  `nums`，处理以下类型的多个查询:

1. 计算索引 `left` 和 `right` （包含 `left` 和 `right`）之间的 `nums` 元素的 **和** ，其中 `left <= right`

实现 `NumArray` 类：

- `NumArray(int[] nums)` 使用数组 `nums` 初始化对象
- `int sumRange(int i, int j)` 返回数组 `nums` 中索引 `left` 和 `right` 之间的元素的 **总和** ，包含 `left` 和 `right` 两点（也就是 `nums[left] + nums[left + 1] + ... + nums[right]` )

**示例 1：**
**输入：**
```
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
```
**输出：**
`[null, 1, -1, -3]`
**解释：**
```
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
```

**暴力解法：直接遍历左右之间元素的和：**
```java
class NumArray {  
    private int[] nums;  
  
    public NumArray(int[] nums) {  
        this.nums = nums;  
    }  
    public int sumRange(int left, int right) {  
        int res = 0;  
        for(int i = left; i <= right; i++){  
            res += nums[i];  
        }  
        return res;  
    }  
}  
  
/**  
 * Your NumArray object will be instantiated and called as such: 
 * NumArray obj = new NumArray(nums); 
 * int param_1 = obj.sumRange(left,right); 
 */
```
#### 算法实现
使用前缀和实现本题，时间复杂度为 O(n)：

```java
lass NumArray {
    int[] nums;
    int[] preSum;
    public NumArray(int[] nums) {
        this.nums = nums;
        preSum = new int[nums.length + 1];
        for(int i = 1; i < preSum.length; i++){
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
    }
    
    public int sumRange(int left, int right) {
        return preSum[right + 1] - preSum[left];
    }
}
```


### 560. [和为 k 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/)
给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 _该数组中和为 `k` 的子数组的个数_ 。
子数组是数组中元素的连续非空序列。

**示例 1：**
**输入：** `nums = [1,1,1], k = 2`
**输出：** 2

**示例 2：**
**输入：** `nums = [1,2,3], k = 3`
**输出：** 2

**提示：**
- `1 <= nums.length <= 2 * 104`
- `-1000 <= nums[i] <= 1000`
- `-107 <= k <= 107`

#### 算法思路与总结
特别好的一道题目，既涉及经典的 2 Sum 问题，又需要用到非常 popular 的 preSum 思想。并且不同解法的难度逐渐加大，时间复杂度大幅度降低。
解法一：纯粹暴力解法，我们可以首先 generate 所有可能的 subArr，然后对 subArr 求 Sum，判断这个值是否等于我们的目标 k。时间复杂度为 $O(n^3)$，解法如下：
```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        for(int i = 0; i < nums.length; i++){
            for(int j = i; j < nums.length; j++){
                int ans = 0;
                for(int t = i; t <= j; t++){
                    ans += nums[t];
                }
                if(ans == k){
                    res++;
                }
            }
        }
        return res;
    }
}
```
直接超出时间限制。。。
解法二：还是暴力的产生所有可能的 subArr，但是我们不需要在内部再次使用一个 for loop，而是使用前缀和数组判断子数组是否满足条件，这种解法的时间复杂度为 $O(n^2)$ ，提交用时打败 10%。
 ```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int[] preSum = new int[nums.length + 1];
        for(int i = 1; i < preSum.length; i++){
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }

        int res = 0;
        for(int i = 0; i < nums.length; i++){
            for(int j = i; j < nums.length; j++){
                if(preSum[j + 1] - preSum[i] == k){
                    res++;
                }
            }
        }
        return res;
    }
}
```
解法三，当我们求得前缀和数组的时候，原问题就可以转换为在前缀和数组中找到两个 `i, j` 使得 `preSum[j] - preSum[i] == k` 其实就是一个 2 Sum 问题的变种，经过一定的变形以后，得到`preSum[i] = preSum[j] - k`。所以我们可以使用一个哈希表来存储所有遍历到的数组元素，key 存储元素值，value 存储这个元素出现的次数，在遍历过程中，如果查找到 `preSum[j] - k` 说明找到了一个这样的子数组，我们把这个出现次数加到答案上去，代码如下：
```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int[] preSum = new int[nums.length + 1];
        Map<Integer, Integer> map = new HashMap<>();
        int res = 0;
        for(int i = 1; i < preSum.length; i++){
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
        for(int i = 0; i < preSum.length; i++){
            int diff = preSum[i] - k;
            if(map.containsKey(diff)){
                res += map.get(diff);
            }
            map.put(preSum[i], map.getOrDefault(preSum[i], 0) + 1);
        }
        return res;
    }
}
```
#### 算法实现
在解法三的基础上还可以进行优化，其实没有必要使用数组存储前缀和，我们在计算前缀和的过程中，就可以把哈希表的判断加上，这样具体的时间复杂度就从 
$$
O(2n) -> O(n)
$$
最终代码实现：




## 前缀和基础

### 1480. [一维数组的动态和](https://leetcode.cn/problems/running-sum-of-1d-array/description/)
【简单题】给你一个数组 `nums` 。数组「动态和」的计算公式为：`runningSum[i] = sum(nums[0]…nums[i])` 。

请返回 `nums` 的动态和。

**示例 1：**
**输入：** `nums = [1,2,3,4]`
**输出：** `[1,3,6,10]`
**解释：** `动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。`


**简单解法：其实就是一道返回前缀和数组的题目：**
```java
// 时间复杂度 O(N)
class Solution{
	public int[] runningSum(int[] nums){
		int[] s = new int[nums.length];
		s[0] = nums[0];
		for(int i = 1; i < nums.length; i++){
			s[i] = nums[i] + s[i-1];
		}
		return s;
	}
}
```

**暴力解法：通过两重循环解决：**


### 3427. [变长子数组求和](https://leetcode.cn/problems/sum-of-variable-length-subarrays/description/)
【简单题】给你一个长度为 `n` 的整数数组 `nums` 。对于 **每个** 下标 `i`（`0 <= i < n`），定义对应的子数组 `nums[start ... i]`（`start = max(0, i - nums[i])`）。

返回为数组中==每个下标定义的子数组中所有元素的总和==。

**子数组** 是数组中的一个连续、**非空** 的元素序列。

**示例 1：**
**输入：**` nums = [2,3,1]`
**输出：** `11`

| 下标 i   | 子数组                      | 和   |
| ------ | ------------------------ | --- |
| 0      | `nums[0] = [2]`          | 2   |
| 1      | `nums[0 ... 1] = [2, 3]` | 5   |
| 2      | `nums[1 ... 2] = [3, 1]` | 4   |
| **总和** |                          | 11  |
总和为 11 。因此，输出 11 。


**前缀和解法：**
```java
class Solution {  
    public int subarraySum(int[] nums) {  
        int[] s = new int[nums.length];  
        s[0] = nums[0]; 
        
        // 首先计算数组的前缀和  
        for(int i = 1; i < nums.length; i++){  
            s[i] = nums[i] + s[i-1];  
        }  
  
        int sum = 0;  
        // 然后计算子数组所有元素的和  
        // 计算 start，同时根据前缀和数组计算所有的
        int start;  
        for(int i = 0; i < nums.length; i++){  
            start = Math.max(0, i - nums[i]);  
            if(start == 0){  
                sum += s[i];  
            }  
            else{  
                sum = sum + (s[i] - s[start - 1]);  
            }  
        }  
        return sum;  
    }  
}
```

# 算法-差分数组
## 差分数组基础
差分数组最适合的学习顺序应该是在刚学完前缀和以后，求差分数组的过程刚好和求前缀和数组的过程是相反的。
**示例引入**：
现在有一个数组 `a = [1,3,5,5,8]` 如果我们对于相邻的元素做差，作为一个新的数组中的元素，然后把`a[0]` 作为这个新数组的第一个元素，可以得到下面这样一个差分数组：
$$d=[1,2,2,0,3]$$
对于这个差分数组，不难发现，==只需要对其进行求前缀和操作，就可以得到原始数组。这是差分数组第一个重要的性质。==
即：差分数组的前缀和数组就是原始数组。
现在，对元素数组的子数组`a[1],a[2],a[3]`中的元素 +10。得到一个新的数组$a^,=[1,13,15,15,8]$ ，对于这个新的操作以后的数组求差分数组，得到新的差分数组
$$
d^, = [1,12,2,0,-7]
$$
对比新的差分数组和原始的差分数组，可以发现只有改变过元素的边界位置的值变了`d[1] d[3+1]`，其他所有位置的值都没有改变，这说明了差分数组的另一个性质：==对于原始数组子数组的操作，可以通过在差分数组中改变两个元素实现相同的操作。==
**定义和性质**：

$$
d[i]= $ \begin{cases}a[0], i =0\\a[i]-a[i-1],i \geqslant 1 \end{cases} 
$$
性质 1：从左到右内家 d 中的元素，可以得到数组 a。
性质 2：如下两个操作是等价的。
- 把 a 的子数组 `a[i], a[i+1], ... ,a[j]` 都加上 x。
- 把 `d[i]` 增加 x，把 `d[j+1]` 减少 x。

利用性质 2，我们只需要 `O(1)` 的时间就可以完成对 a 的子数组的操作。最后利用性质 1 从差分数组复原出数组 a。
### 1094. [拼车 ](https://leetcode.cn/problems/car-pooling/)
【差分数组模板题】
车上最初有 `capacity` 个空座位。车 **只能** 向一个方向行驶（也就是说，**不允许掉头或改变方向**）

给定整数 `capacity` 和一个数组 `trips` ,  `trip[i] = [numPassengersi, fromi, toi]` 表示第 `i` 次旅行有 `numPassengersi` 乘客，接他们和放他们的位置分别是 `fromi` 和 `toi` 。这些位置是从汽车的初始位置向东的公里数。

当且仅当你可以在所有给定的行程中接送所有乘客时，返回 `true`，否则请返回 `false`。

**示例 1：**

**输入：** `trips = [[2,1,5],[3,3,7]], capacity = 4`
**输出：** `false`

**示例 2：**

**输入：**` trips = [[2,1,5],[3,3,7]], capacity = 5`
**输出：** `true`
#### 算法思路与总结
对于本题，原始数组 `a[i]` 就表示车行驶到位置 i 的时候车上的人数。我们需要判断的就是每个位置上 `a[i]` 都不超过`capacity`。
`trips[i]` 相当于把`a`中下标从$from_i$ 到 $to_i - 1$的数都增加`numPassengers。相当于对于原始数组的子数组进行操作，所以可以利用上面讲到的差分数组来进行解决。
注意这里我们需要先得到差分数组，然后根据差分数组，求得每个位置车上会有多少人。
比如，对于示例 1 ，将会有两个人在 2 上车，5 下车，3 个人在 3 上车，7 下车，所以差分数组就会是：
```
d = [0,0,2,3,0,-2,0,-3]
```
从左到右边累加，得到：
```
a = [0,2,2,5,5,3,3,0]
```
由于存在一个 `a[i] > capacity` 所以返回 false。
**实现方法：**
1. 第一种写法，创建一个长为 1001 的差分数组，这样可以保证 d 数组不会下标越界。

#### 算法实现
```java
```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        // 创建一个差分数组
        int[] d = new int[1001];
        // 遍历 trip 数组
        for(int[] t : trips){
            d[t[1]] = d[t[1]] + t[0];
            d[t[2]] = d[t[2]] - t[0];
        }
        // 还原到原始数组
        int s = 0;
        for(int v : d){
            s += v;
            if(s > capacity){
                return false;
            }
        }
        return true;
    }
}
```
```
# 算法-相向双指针
## 两数之和
### 167. [两数之和 || - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/)
**题目描述**：
给你一个下标从 **1** 开始的整数数组 `numbers` ，该数组已按 **非递减顺序排列**  ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。如果设这两个数分别是 `numbers[index1]` 和 `numbers[index2]` ，则 `1 <= index1 < index2 <= numbers.length` 。

以长度为 2 的整数数组 `[index1, index2]` 的形式返回这两个整数的下标 `index1` 和 `index2`。

你可以假设每个输入 **只对应唯一的答案** ，而且你 **不可以** 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。

**示例 1：**
**输入：** `numbers = [2,7,11,15], target = 9`
**输出：** `[1,2]`
**解释：** `2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。`

#### 算法思路与总结

这道题目是跟着灵神的相向双指针算法学习的，看完豁然开朗！思路非常清晰，手撕直接可以一遍过，假如自己做这道题的话，估计会使用 $O(N^2)$ 的时间复杂度暴力求出来。其实这道题最重要的性质就是==传入的数组已经按照非递减顺序排列==。假如使用暴力解法，本质上就是没有使用到有序数组的性质。
双指针思路：首先初始化左指针、右指针，分别指向数组的最左边和最右边元素，判断 `numbers[left] + numbers[right] == target` 如果等于的话，直接返回结果。否则，如果结果＞ target，说明最小的数和最大的数相加比 target 大，又因为数组有序，所以最大的数前面一个元素和最小的数相加可能等于 target；反之，如果结果＜target，说明最小的数和最大的数相加比 target 还要小，所以最小的数的后面一个数和最大的数相加可能等于 target。通过重复这个过程，就能在 O(N) 的时间复杂度内解决这个问题。

#### 算法实现
**使用双指针在 O(N) 的时间复杂度内实现：**
```java
class Solution {  
    public int[] twoSum(int[] numbers, int target) {  
        int[] res = new int[2];  
        int left = 0;  
        int right = numbers.length - 1;  
  
        while(numbers[left] + numbers[right] != target){  
            if(numbers[left] + numbers[right] > target){  
                right = right - 1;  
            }else{  
                left = left + 1;  
            }
        }
        res[0] = left + 1;  
        res[1] = right + 1;  
        return res;  
    }  
}
```
**尝试使用暴力求解算法解题：**
```java
class Solution {  
    public int[] twoSum(int[] numbers, int target) {  
        int num1 = 0;  
        int num2 = 0;  
        for(;num1 < numbers.length; num1++){  
            for(num2 = num1 + 1; num2 < numbers.length; num2++){  
                if(numbers[num1] + numbers[num2] == target){  
                    return new int[]{num1 + 1, num2 + 1};  
                }  
            }  
        }  
        return new int[2];  
    }  
}
```
### 15. 三数之和

# 彩票问题
## 基础彩票问题
### 121. [买卖彩票的最佳时间](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/)【只能买卖一次】
**题目描述：**
给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**
**输入：** `[7,1,5,3,6,4]`
**输出：** 5
**解释：** 
在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

**算法思路：**


# 排序
## 252. [会议室](https://leetcode.cn/problems/meeting-rooms/description/)

【简单题】
给定一个会议时间安排的数组 `intervals` ，每个会议时间都会包括开始和结束的时间 `intervals[i] = [starti, endi]` ，请你判断一个人是否能够参加这里面的全部会议。

**示例 1：**
**输入：**` intervals = [[0,30],[5,10],[15,20]]`
**输出**：`false`

**示例 2：**
**输入：** `intervals = [[7,10],[2,4]]`
**输出**：`true`

**提示：**
- `0 <= intervals.length <= 104`
- `intervals[i].length == 2`
- `0 <= starti < endi <= 106`

### 算法思路与总结
本题是在学习 [[Java 比较器 Comparator 与 Comparable|Java 比较器专题]] 中积累的。主要是为了熟悉如何正确使用比较器。
题目思路其实比较简单，对于一系列的活动来说，如果上一个活动的结束时间大于下一个活动的开始时间，那么活动之间肯定就存在冲突，这时就需要返回 false。所以只需要将所有活动按照活动开始时间进行排序，然后判断先开始的活动是否能够先结束，返回答案即可。
另外一个问题就是， `Arrays.sort(intervals, (a, b) -> a[0] - b[0]);` 为什么这行代码就可以实现把二维数组按照活动的开始时间进行排序。最开始并不理解 `a, b` 两个参数分别代表什么，为什么 Java 解释器能够理解 a、b 两个参数代表的是几维的数组。经过 AI 的解释，由于使用的是 Arrays.sort() 方法：
```java
public static <T> void sort(T[] a, Comparator<? super T> c)
```
例子中的调用是：

```java
int[][] intervals = { ... };
Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
```
在这里：
- `intervals` 的类型是 `int[][]`，也就是 `T[]` 中的 `T = int[]`
- 所以 `T[]` 就是 `int[][]`
- Java 编译器 **推断出 T 是 `int[]`**
- 因此，`a` 和 `b` 的类型自动变成 `int[]`（一维数组）
### 代码实现
```java
class Solution {  
    public boolean canAttendMeetings(int[][] intervals) {  
        // 实现 Comparator
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);  
        for(int i = 0; i < intervals.length - 1; i++){  
            if(intervals[i][1] > intervals[i + 1][0]){  
                return false;  
            }  
        }  
        return true;  
    }  
}
```
其他使用比较器实现的方法：
```java
import java.util.Arrays;  
import java.util.Comparator;  
  
public class Solution {  
    public boolean canAttendMeetings(int[][] intervals) {  
        if(intervals.length == 0) return true;  
          
        // 1. 外部 comparator 普通写法  
        Arrays.sort(intervals,new MyComparator());  
          
        // 2. 内部 comparator 普通写法，使用匿名内部类的方式  
        Arrays.sort(intervals,new Comparator<int[]>() {  
            @Override  
            public int compare(int[] o1, int[] o2) {  
                return o1[0] - o2[0];  
            }  
        });  
          
        for(int i = 0; i < intervals.length; i++){  
            if(intervals[i][0] > intervals[i+1][0]){  
                return false;  
            }  
        }  
        return true;  
    }  
    class MyComparator implements Comparator<int[]> {  
        @Override  
        public int compare(int[] o1, int[] o2) {  
            return Integer.compare(o1[0],o2[0]);  
        }  
    }  
}
```
# 贪心算法
贪心算法是指在对问题进行求解时，在每一步选择中采取最好或者最优的选择，从而希望能够导致结果是最好或者最优的算法。贪心算法得到的结果玩玩不是最优解（有时候会是最优解），但是都是相对近似（接近）最优解的结果。
贪心算法没有固定的算法解决框架，算法的关键是贪心策略的选择，根据不同的问题选择不同的策略。
需要注意的是贪心策略的选择必须具备无后效性，即某个状态的选择不会影响到之前的状态，只与当前状态有关，所以对采用的贪心的策略一定要仔细分析是否满足这个性质。

**基本思路：**
1. 建立数学模型描述问题。
2. 把求解的问题分成若干个子问题。
3. 对每一个子问题求解，得到子问题的局部最优解。
4. 把子问题对应的局部最优解合成原来整个问题的一个近似最优解。

## 1710. [卡车上的最大单元数](https://leetcode.cn/problems/maximum-units-on-a-truck/description/)
【简单题】
请你将一些箱子装在 **一辆卡车** 上。给你一个二维数组 `boxTypes` ，其中 `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]` ：
- `numberOfBoxesi` 是类型 `i` 的箱子的数量。
- `numberOfUnitsPerBoxi` 是类型 `i` 每个箱子可以装载的单元数量。
整数 `truckSize` 表示卡车上可以装载 **箱子** 的 **最大数量** 。只要箱子数量不超过 `truckSize` ，你就可以选择任意箱子装到卡车上。

返回卡车可以装载**单元**的**最大**总数。

**示例 1：**
**输入：** `boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4`
**输出：** `8`
**解释：** 箱子的情况如下：
- 1 个第一类的箱子，里面含 3 个单元。
- 2 个第二类的箱子，每个里面含 2 个单元。
- 3 个第三类的箱子，每个里面含 1 个单元。
可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。
单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8
### 算法思路
卡车能够装载的最多单元的数量，然后每个箱子能够装的单元又是不一样的，我们需要在不超过卡车箱子容量的前提下返回卡车可以装载的单元最大总数。本题本质上其实是一道特殊的背包问题，但是因为问题足够特殊，所以我们可以使用贪心思路解决问题。每一步都做出最优的选择：选择能够装单元数量最多的箱子，最后得到的一定是最大的单元数量。

### 代码实现
```java
class Solution {  
    public int maximumUnits(int[][] boxTypes, int truckSize) {  
	    // 按照箱子的装载能力从大到小排序
        Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);  
        int ans = 0;  
        for(int i = 0; i < boxTypes.length; i++){
	        // 不能继续装箱子了
            if(truckSize <= 0){  
                break;  
            }  
            // 
            if(truckSize > boxTypes[i][0])  
                ans += boxTypes[i][0] * boxTypes[i][1];  
            else  
                ans += truckSize * boxTypes[i][1];  
            truckSize -= boxTypes[i][0];  
        }  
        return ans;  
    }  
}
```
## 11. 包含最多的水
【中等题】
### 算法思路

### 代码实现

## 55. 跳跃游戏




## 134
## Summary
1. 贪心算法可以寻找局部最优解，并尝试用这种方式获得全局最优解。
2. 得到的可能是近似最优解，但也可能是就是最优解（区间调度问题、最短路径问题）。
3. 贪心算法在大部分情况在易于实现，并且效率不错。
4. 贪心算法并不能总求得问题的整体最优解。但是对于某些问题，却总能求得整体最优解，这要看问题是什么。只要满足贪心算法的两个性质：贪心选择性质和最优子结构性质，贪心算法就能够出色的求出问题的整体最优解。**最优子结构性质**是比较容易看出来的，但是**贪心选择性质**就需要使用数学归纳法或者反证法证明。

优点：简单、高效，省去了为了找最优解需要的穷举操作，通常作为其他算法的辅助算法来使用。
缺点：不从总体上考虑其他可能情况，每次选取局部最优解，不再进行回溯操作，所以很少情况下得到最优解。

# 最大公约数与最小公倍数
首先介绍一个求最大公约数的算法：辗转相除法。
辗转相除法的代码模板：
```java
int gcd(int a, int b){
	if(b == 0)
		return a;
	rturn gcd(b, a % b);
}
```
## 最小公倍数

# 递归 Recursion
## 使用场景
1. Tree Travel (binary search)
2. backtracking (subset, permutation, etc)
3. divide and conquer (quick sort, merge sort)
4. depth first search
5. dynamic programing => top down approach
6. math problem

**递归需要遵守的重要规则：**
- 执行一个方法时，就创建一个新的受保护的独立空间（栈空间）
- 方法的局部变量是独立的，不会相互影响。
- 如果方法中使用的是应用类型变量（比如数组），就会共享该引用类型的数据。
- 递归必须向退出递归的条件逼近，否则就是无限递归，出现 StackOverFlow。
- 当一个方法执行王比，或者遇到 return，就会返回，遵守谁调用，就将结果返回给谁，同时当方法执行完毕或者返回时，该方法也就执行完成。
## 968. [监控二叉树](https://leetcode.cn/problems/binary-tree-cameras/description/)
【困难题】
给定一个二叉树，我们在树的节点上安装摄像头。
节点上的每个摄影头都可以监视**其父对象、自身及其直接子对象。**
计算监控树的所有节点所需的最小摄像头数量。

**示例 1：**
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_01.png)

**输入：**`[0,0,null,0,0]`
**输出：** 1
**解释：** 如图所示，一台摄像头足以监控所有节点。

**示例 2：**
![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_02.png)
**输入：**`[0,0,null,0,null,0,null,null,0]`
**输出：** 2
**解释：** 需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
**提示：**

1. 给定树的节点数的范围是 `[1, 1000]`。
2. 每个节点的值都是 0。

### 算法思路与总结

### 代码实现
```java
class Solution {  
    int res = 0;  
    public int minCameraCover(TreeNode root) {  
        return (dfs(root) < 1? 1: 0) + res;  
    }  
    public int dfs(TreeNode root){  
        if(root == null)  
            return 2;  
        int left = dfs(root.left), right = dfs(root.right);  
        // 左孩子或者右孩子没有看到，当前结点都必须装监控  
        if(left == 0 || right == 0){  
            res++;  
            return 1;  
        }  
        // 如果左孩子或者右孩子有监控，当前结点能够被看到  
        if(left == 1 || right == 1)  
            return 2;  
        // 如果左孩子右孩子 covered 了，那么我们把当前结点也可以看作一个叶子结点，prefer 在父亲结点上装监控  
        if(left == 2 && right == 2)  
            return 0;  
        return Integer.MIN_VALUE;  
    }  
}
```
# BFS
广度优先搜索，一般用来：
- 遍历树的结构（Level Order）
- 遍历图的结构（BFS，Topological）
- 遍历二维数组

## 490 [迷宫](https://leetcode.cn/problems/the-maze/description/)
【中等题】由空地（用 `0` 表示）和墙（用 `1` 表示）组成的迷宫 `maze` 中有一个球。球可以途经空地向 **上、下、左、右** 四个方向滚动，且在遇到墙壁前不会停止滚动。当球停下时，可以选择向下一个方向滚动。

给你一个大小为 `m x n` 的迷宫 `maze` ，以及球的初始位置 `start` 和目的地 `destination` ，其中 `start = [startrow, startcol]` 且 `destination = [destinationrow, destinationcol]` 。请你判断球能否在目的地停下：如果可以，返回 `true` ；否则，返回 `false` 。
你可以 **假定迷宫的边缘都是墙壁**（参考示例）。
**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/31/maze1-1-grid.jpg)

**输入：** `maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]`
**输出：** `true`
**解释：** `一种可能的路径是 : 左 -> 下 -> 左 -> 下 -> 右 -> 下 -> 右。`
### 算法思路与总结
使用 BFS 解决迷宫问题，关键问题就在于理解题目中所述的球在遇到墙壁之前不会停下来。按照 BFS 题目的模板，我们在每次从队列中取一个点，首先判断是否到达了迷宫的出口，到达就返回 true；否则我们尝试所有可行的反向，并且一直走到墙，然后判断每个方向是否被访问过，如果走到头以后并且这个格子没有被访问过，那么就把这个格子加入到队列中。当整个循环结束还没有走到出口的时候，就说明我们无法按照题目要求走到对应地点，返回 false。
### 算法实现
```java
class Solution {  
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {  
        boolean[][] visited = new boolean[maze.length][maze[0].length];  
        Queue<int[]> q = new LinkedList<>();  
        q.offer(start);  
        int[][] dirs = new int[][]{  
                {0, 1},  
                {0, -1},  
                {1, 0},  
                {-1, 0}  
        };  
        while(!q.isEmpty()){  
            int[] cur = q.poll();  
            if(cur[0] == destination[0] && cur[1] == destination[1]) return true;  
            for(int[] dir : dirs){  
                int x = cur[0] + dir[0];  
                int y = cur[1] + dir[1];  
                // 没有碰到墙的清况下就一直滚动  
                while(x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0){  
                    x += dir[0];  
                    y += dir[1];  
                }  
                x -= dir[0];  
                y -= dir[1];  
                if(visited[x][y] == false){  
                    q.offer(new int[]{x, y});  
                    visited[x][y] = true;  
                }  
            }  
        }  
        return false;  
    }  
}
```

