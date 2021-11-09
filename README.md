# running
### 基于手机模拟器虚拟定位实现自动跑圈
### 手机模拟器需求
- nox模拟器 [https://www.bignox.com/en/download/fullPackage?beta"点此下载"]
### 需求python依赖模块（已打包为exe，无需手动编译）
- pyautogoi
- keyboard
### 食用方法
1. 修改配置文件，字段如下说明
|  字段   | 说明  |
|  ----  | ----  |
| region  | 左上角和右下角的经纬度 |
| speed.init  | 初始速度 |
| speed.ave  | 平均速度 |
| speed.step  | 速度变化步长 |
| divide_num  | 分隔点的个数 |
| target  | 目标距离(m) |
| keymap.start  | 开始热键 |
| keymap.test  | 测试热键 |
| keymap.stop  | 结束热键 |

2. 修改finish.png为你模拟器的结束按钮截图（否则如果分辨率与我的不同，将不能自动结束）
3. 添加系统环境变量runhome为你的工作目录
4. 双击打开Main.exe
5. 打开模拟器，打开跑步app，打开虚拟定位，先虚拟定位至区域左上角之外的一点（否则里程记录会不准）
6. 鼠标点击一下虚拟定位的输入框第一栏，如下图
![image](1.png)
7. 按下f1开始运行，会再20分钟左右自动结束（以3.1km的里程为例）
### 已知bug
- 分隔点过多会造成两点距离过近，被视为同一点，为此可以先按f2 test一下，成功后再start，不成功九江divide_num字段改小
### 支持学校
浙江理工大学
