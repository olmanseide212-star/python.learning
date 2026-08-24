def remove_duplicates(nums: list[int]) -> int:
    # 步骤 1：处理特殊情况（如果列表是空的）
    if not nums:
        return 0

    # 步骤 2：慢指针（收纳员）先守在 0 号位
    slow = 0

    # 步骤 3：快指针（侦察兵）从 1 号位开始一路向后跑
    for fast in range(1, len(nums)):
        # 步骤 4：如果快指针发现了和慢指针不一样的全新数字
        if nums[fast] != nums[slow]:
            slow += 1                # 慢指针向右挪一格，空出一个新座位
            nums[slow] = nums[fast]  # 把快指针看到的新数字抄写过来

    # 步骤 5：返回不重复数字的总个数
    return slow + 1
