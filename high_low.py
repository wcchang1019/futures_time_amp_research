import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
sns.set()
sns.set(font=['sans-serif'])
sns.set_style("whitegrid", {"font.sans-serif": ['Microsoft JhengHei']})


def big_small_compare(big_type, small_type):
    df = pd.read_csv('data\high_low_3.csv')
    df2 = pd.read_csv('data\high_low_10.csv')
    df = df.astype(float)
    df2 = df2.astype(float)
    df.columns = ['pre_date', 'now_date', 'type', 'time', 'amp']
    df2.columns = ['pre_date', 'now_date', 'type', 'time', 'amp']
    df = df[df['type'] == small_type]
    df2 = df2[df2['type'] == big_type]
    ans = pd.DataFrame()
    for index, row in df2.iterrows():
        tmp = df.loc[(df.pre_date >= row['pre_date']) & (df.now_date <= row['now_date'])]
        tmp = tmp.assign(id=pd.Series(list(range(0, len(tmp)))).values)
        print(tmp)
        ans = ans.append(tmp)
    name = '大週期: ' + str(big_type) + ' 小週期: ' + str(small_type)
    plt.title(name)
    ans['id'] = ans['id'].astype(int)
    sns.scatterplot(x='time', y='amp', hue='id', data=ans, palette=sns.color_palette("muted", len(np.unique(ans['id']))))
    plt.savefig('大週期10天小週期3天/' + name.replace(':', '-')+'.jpg')
    plt.show()


def total_big_small_compare():
    for x in range(-1, 2):
        for y in range(-1, 2):
            big_small_compare(x, y)


def time_amp_scatter(f):
    df = pd.read_csv('data\high_low_' + str(f) + '.csv')
    df = df.astype(float)
    df.columns = ['pre_date', 'now_date', 'type', 'time', 'amp']
    df['type'] = df['type'].astype(int)
    print(df)
    sns.scatterplot(x='time', y='amp', hue='type', data=df, palette=sns.color_palette("muted", len(np.unique(df['type']))))
    plt.title('週期:' + str(f) + '天')
    plt.savefig('震幅與時間分布圖/' + '週期-' + str(f) + '天')
    plt.show()


def total_time_amp_compare():
    time_amp_scatter(3)
    time_amp_scatter(5)
    time_amp_scatter(10)


def big_small_times_amp_count(big_type, small_type):
    df = pd.read_csv('data\high_low_3.csv')
    df2 = pd.read_csv('data\high_low_10.csv')
    df = df.astype(float)
    df2 = df2.astype(float)
    df.columns = ['pre_date', 'now_date', 'type', 'time', 'amp']
    df2.columns = ['pre_date', 'now_date', 'type', 'time', 'amp']
    df = df[df['type'] == small_type]
    df2 = df2[df2['type'] == big_type]
    ans = pd.DataFrame()
    for index, row in df2.iterrows():
        tmp = df.loc[(df.pre_date >= row['pre_date']) & (df.now_date <= row['now_date'])]
        ans = ans.append(tmp)
    # print(ans[name].value_counts())
    ans['time'].value_counts().plot(kind='bar')
    plt.xlabel('時間')
    plt.ylabel('出現次數')
    plt.title('大週期:' + str(big_type) + ' 小週期:' + str(small_type))
    plt.savefig('震幅與時間次數圖/' + '大週期-' + str(big_type) + ' 小週期-' + str(small_type) + '時間.jpg')
    plt.show()
    sns.distplot(ans['amp'], kde=False, bins=50)
    plt.xlabel('震幅')
    plt.ylabel('出現次數')
    plt.title('大週期:' + str(big_type) + ' 小週期:' + str(small_type))
    plt.savefig('震幅與時間次數圖/' + '大週期-' + str(big_type) + ' 小週期-' + str(small_type) + '震幅.jpg')
    plt.show()


def total_big_small_time_amp_count():
    for x in range(-1, 2):
        for y in range(-1, 2):
            big_small_times_amp_count(x, y)


if __name__ == '__main__':
    total_big_small_time_amp_count()
