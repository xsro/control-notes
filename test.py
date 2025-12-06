def generate_permutations(arr):
    """
    递归回溯生成数组的所有排列（纯原生Python实现）
    :param arr: 输入数组（如[1,2,...,9]）
    :return: 所有排列组成的列表，每个元素是一个排列列表
    """
    # 存储最终所有排列的结果列表
    result = []
    
    def backtrack(current, remaining):
        """
        回溯核心函数
        :param current: 当前已选的元素（构建中的排列）
        :param remaining: 剩余可选的元素
        """
        # 终止条件：剩余元素为空，当前排列完成
        if not remaining:
            result.append(current.copy())
            return
        
        # 遍历剩余元素，逐个选择并回溯
        for i in range(len(remaining)):
            # 选择第i个剩余元素
            chosen = remaining[i]
            current.append(chosen)
            # 剩余元素排除已选的第i个
            new_remaining = remaining[:i] + remaining[i+1:]
            # 递归处理下一层
            backtrack(current, new_remaining)
            # 回溯：撤销选择
            current.pop()
    
    # 初始调用：当前排列为空，剩余元素为输入数组
    backtrack([], arr)
    return result

# ===================== 主程序 =====================
if __name__ == "__main__":
    # 生成1到9的列表
    nums = list(range(1, 10))
    
    # 生成所有排列
    print("开始生成1到9的所有排列...（9! = 362880 个，耗时约10-20秒）")
    all_permutations = generate_permutations(nums)
    
    # 结果验证
    print(f"\n排列总数：{len(all_permutations)}（理论值9! = {362880}）")
    print("\n前5个排列示例：")
    for i in range(5):
        print(f"第{i+1}个排列：{all_permutations[i]}")
    
    print("\n最后5个排列示例：")
    for i in range(-5, 0):
        print(f"第{len(all_permutations)+i+1}个排列：{all_permutations[i]}")


    for p in all_permutations:
        a1=p[0]*p[1]
        a2=p[2]*10+p[3]
        b1=(p[4]*10+p[5])/p[6]
        b2=p[7]*10+p[8]
        if abs(a1-a2)<0.1 and abs(b1-b2)<0.1:
            print(f"{p[0]}x{p[1]}={p[2]}{p[3]}",f"{p[4]}{p[5]}/{p[6]}={p[7]}{p[8]}")