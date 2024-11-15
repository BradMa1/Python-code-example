import pandas as pd
import numpy as np

# 生成模拟交通数据
data = {
    'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='T'),
    'north_south': np.random.randint(0, 20, size=100),
    'east_west': np.random.randint(0, 20, size=100)
}
df = pd.DataFrame(data)
print(df.head())

def adjust_signal_duration(north_south_count, east_west_count):
    base_duration = 30  # 基础时长为30秒
    if north_south_count > east_west_count:
        north_south_duration = base_duration + 10
        east_west_duration = base_duration - 10
    else:
        north_south_duration = base_duration - 10
        east_west_duration = base_duration + 10
    return north_south_duration, east_west_duration

# 示例调整信号灯时长
north_south_count = df['north_south'].iloc[0]
east_west_count = df['east_west'].iloc[0]
north_south_duration, east_west_duration = adjust_signal_duration(north_south_count, east_west_count)
print(f"北南方向绿灯时长: {north_south_duration} 秒, 东西方向绿灯时长: {east_west_duration} 秒")

signal_durations = []

for index, row in df.iterrows():
    north_south_count = row['north_south']
    east_west_count = row['east_west']
    north_south_duration, east_west_duration = adjust_signal_duration(north_south_count, east_west_count)
    signal_durations.append({
        'timestamp': row['timestamp'],
        'north_south_duration': north_south_duration,
        'east_west_duration': east_west_duration
    })

duration_df = pd.DataFrame(signal_durations)
print(duration_df.head())


#  结果可视化
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(duration_df['timestamp'], duration_df['north_south_duration'], label='北南方向绿灯时长')
plt.plot(duration_df['timestamp'], duration_df['east_west_duration'], label='东西方向绿灯时长')
plt.xlabel('时间')
plt.ylabel('绿灯时长 (秒)')
plt.title('智能交通信号控制系统')
plt.legend()
plt.show()