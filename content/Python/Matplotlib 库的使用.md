# 什么是 Matplotlib

- 这个包早期提供类似于 Matlab 的画图语法、画图效果
- 后期和 Pandas +  Numpy + Matpltolib 成为数据分析三兄弟
	- 不仅限于画图；动画、交互、程序 GUI 后端等

## 简单的 demo

```python
import matplotlib.pyplot as plt
  
# data

data_lst = [1, 2, 3, 4]

stock1 = [4, 8, 2, 6]

stock2 = [10, 12, 5, 3]  

# draw the image

plt.plot(data_lst, stock1)

plt.plot(data_lst, stock2)

plt.show()
```


![[使用 matplotlib 绘图的例子.png]]

```python
import matplotlib.pyplot as plt
# data

data_lst = [1, 2, 3, 4]

stock1 = [4, 8, 2, 6]

stock2 = [10, 12, 5, 3]

# draw the image

plt.plot(data_lst, stock1, "ro--", label="Stock num: abc")

plt.plot(data_lst, stock2, "b^--", label="Stock num: def")

plt.title("Linear Diagram")

plt.xlabel("Time") # 标注 x 轴

plt.ylabel("Stock Price") # 标注 y 轴

plt.legend() # 添加图例

plt.show()
```

![[稍加改动后的图表.png]]

# 

Most of the Matplotlib utilities lies under the `pyplot` submodule, and are usually imported under the `plt` alias:

```python
import matplotlib.pyplot as plt
```

Now the Pyplot package can be referred to as `plt`.

## Plotting
The plot() function is used to draw points in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
### Explaining the parameters
- Parameter1 is an array containing the points on the x-axis.
- Parameter2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays `[1, 8]` and `[3, 10] `to the plot function.

A example:
```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
```
Result:

![](https://www.w3schools.com/python/img_matplotlib_plotting1.png)

### Plot without line
To plot only the markers, you can use _shortcut string notation_ parameter 'o', which means 'rings'.
```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
```

### Multiple Points
You can plot as many points as you like, just make suer you have the same number of points in both axis.

Example:
```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
```

Result:
![](https://www.w3schools.com/python/img_matplotlib_plotting2.png)

### Default X-Points
If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc, depending on the length of the y-points.
So, If we take the same example as above, and leave out the x-points, the diagram will look like this:

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
```

Result:
![](https://www.w3schools.com/python/img_matplotlib_plotting4.png)

## Matplotlib Markers
### Markers
You can use the keyword argument `marker` to emphasize each point with a specified marker:

```python
import matplotlib.pyplot as plt  
import numpy as np  
  
ypoints = np.array([3, 8, 1, 10])  
  
plt.plot(ypoints, marker = 'o')  
plt.show()
```

Result:
![](https://www.w3schools.com/python/img_matplotlib_marker_o.png)

### Marker Reference
#### 1. 常见点状 Marker

|取值|含义|示例外观|
|---|---|---|
|`"."`|点（point marker）|`·`|
|`","`|像素点（pixel marker，更小）|`•`|

#### 2. 圆形与三角形

|取值|含义|示例外观|
|---|---|---|
|`"o"`|圆形|`○`|
|`"v"`|下三角|`▽`|
|`"^"`|上三角|`△`|
|`"<"`|左三角|◁|
|`">"`|右三角|▷|

#### 3. 方形与菱形

| 取值    | 含义                    | 示例外观 |
| ----- | --------------------- | ---- |
| `"s"` | 方形（square）            | ■    |
| `"p"` | 五边形（pentagon）         | ⬟    |
| `"P"` | 加号填充的五边形（plus filled） | ⊕    |
| `"D"` | 菱形（diamond）           | ◆    |
| `"d"` | 瘦菱形（thin diamond）     | ◇    |

#### 4. 星形与加减号

|取值|含义|示例外观|
|---|---|---|
|`"*"`|星号|✱|
|`"+"`|加号|+|
|`"x"`|叉号|x|
|`"X"`|加粗的叉号|✖|

#### 5. 填充点（TeX 风格）

|取值|含义|示例外观|
|---|---|---|
|`"|"`|垂直线|
|`"_"`|水平线|`_`|

#### 6. 特殊 Marker

|取值|含义|示例外观|
|---|---|---|
|`"H"`|六边形 1|⬢|
|`"h"`|六边形 2|⬡|
|`"1"`|下三叉（tri-down）|ᐁ|
|`"2"`|上三叉（tri-up）|ᐃ|
|`"3"`|左三叉（tri-left）|ᐊ|
|`"4"`|右三叉（tri-right）|ᐅ|

#### 7. 无 Marker

|取值|含义|
|---|---|
|`"None"` 或 `None` 或 `" "`|不显示 marker|
### Format Strings `fmt`
You can also use the shortcut string notation parameter so specify the marker.
This parameter is also called `fmt`, and is written with this syntax:
`marker|line|color`



### Line Reference

| Line Syntax | Description        |
| ----------- | ------------------ |
| '-'         | Solid line         |
| ';'         | Dotted line        |
| '--'        | Dashed line        |
| '-.'        | Dashed/dotted line |

# Reference Material
