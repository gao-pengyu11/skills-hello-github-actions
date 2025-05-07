import pandas as pd
import scipy.stats as stats
# 读取CSV文件（使用GBK编码）
df = pd.read_csv('./数据内容.csv', encoding='gbk')

# 打印原始数据查看列名
print("原始数据：")
print(df.head())

# 编码映射字典（请根据您的数据内容自行修改）
grade_mapping = {"大一": 1, "大二": 2, "大三": 3, "大四": 4}
major_mapping = {"理工科": 1, "文科": 2, "商科": 3, "艺术类": 4}
grade_change_mapping = {"无明显变化": 0, "略有提高": 1, "明显提高": 2, "略有下降": 3, "明显下降": 4}
homework_efficiency_change_mapping = {"无变化": 0, "提高了一些": 1, "提高了很多": 2, "降低了一些": 3, "降低了很多": 4}
time_change_mapping = {"无变化": 0, "时间略有增加": 1, "时间略有减少": 2, "时间大幅增加": 3, "时间大幅减少": 4}
independent_learning_dependency_mapping = {"无依赖": 0, "稍微依赖": 1, "非常依赖": 2, "完全不依赖": 3}
independent_learning_ability_change_mapping = {"没有影响": 0, "略有提升": 1, "大幅提升": 2, "略有下降": 3, "大幅下降": 4}
willingness_to_use_mapping = {"一般": 0, "愿意": 1, "不太愿意": 2, "非常愿意": 3}

# 假设列名为“年级”, “专业”, “成绩变化”等进行编码（请替换为实际列名）
df["年级"] = df["年级"].map(grade_mapping)
df["专业"] = df["专业"].map(major_mapping)
df["成绩变化"] = df["成绩变化"].map(grade_change_mapping)
df["作业效率变化"] = df["作业效率变化"].map(homework_efficiency_change_mapping)
df["时间变化"] = df["时间变化"].map(time_change_mapping)
df["独立学习依赖"] = df["独立学习依赖"].map(independent_learning_dependency_mapping)
df["独立学习能力变化"] = df["独立学习能力变化"].map(independent_learning_ability_change_mapping)
df["使用意愿"] = df["使用意愿"].map(willingness_to_use_mapping)

# 输出编码后的数据
print("编码后的数据：")
print(df.head())



# 选择自变量和因变量
independent_var = df["使用意愿"]  # 使用意愿列作为自变量
dependent_vars = [
    "成绩变化", "作业效率变化", "时间变化", 
    "独立学习依赖", "独立学习能力变化"
]

# 计算相关性系数 r 和显著性检验 p 值
correlations = {}
for dep_var in dependent_vars:
    corr, p_value = stats.pearsonr(independent_var, df[dep_var])
    correlations[dep_var] = {"r": corr, "p-value": p_value}

# 输出相关性系数和显著性检验结果
for dep_var, result in correlations.items():
    print(f"{dep_var} 与 使用意愿 的相关性系数 r: {result['r']:.4f}, 显著性检验 p-value: {result['p-value']:.4f}")

