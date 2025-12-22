import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression  # 替换为线性回归模型
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)

# 读取数据集
sc_df = pd.read_csv('student_data_adjusted_rounded.csv', encoding='utf-8')

# 简单数据预处理
sc_df['性别_编码'] = sc_df['性别'].map({'男': 0, '女': 1})
major_dummies = pd.get_dummies(sc_df['专业'], prefix='专业')
sc_df = pd.concat([sc_df, major_dummies], axis=1)

# 定义特征和目标变量
feature_cols = ['每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率', '性别_编码'] + list(major_dummies.columns)
X = sc_df[feature_cols]
y = sc_df['期末考试分数']

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练轻量模型（线性回归）
model = LinearRegression()  # 线性回归模型文件极小
model.fit(X_train, y_train)

# 评估模型
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"模型训练完成！")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2_score(y_test, y_pred):.2f}")

# 保存模型和特征列
with open("score_model.pkl", 'wb') as f:
    pickle.dump(model, f)

with open("feature_cols.pkl", 'wb') as f:
    pickle.dump(feature_cols, f)

print("模型文件已保存为：score_model.pkl")
print("特征列文件已保存为：feature_cols.pkl")
