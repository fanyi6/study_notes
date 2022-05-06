# 移动端特点



## 移动端和PC网页端不同点

PC屏幕大，网页一般是有固定的版心的
手机屏幕小，网页宽度多数为100%

**电脑通过谷歌模拟器调试移动端网页效果**



## 分辨率

**物理分辨率**
生产屏幕时候加固定的，他是不可被改变的



**逻辑分辨率**

由软件/驱动决定

**制作网页时候使用的是逻辑分辨率**



**移动端主流设备分辨率**

一般是参考iPhone6/7/8
[移动端主流设备分辨率](images/移动端主流设备分辨率.jpg)



## 视口

使用meta标签设置视口宽度，制作适配不同设备宽度的网页，使得网页宽度和设备宽度(分辨率)相同



**添加视口**
一般在vscode生成html时候会自动添加

```html
<!-- 手动添加方法 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

- viewport:视口
- width=device-width:视口宽度=设备宽度
- initial-scale=1.0:缩放1倍（不缩放）



## 二倍图

现阶段设计稿参考iPhone6/7/8，设备宽度375px产出设计稿。二倍图设计稿尺寸:750px

那么在像素大厨软件测量时候需要将设计图修改成x



## 百分比布局
百分比布局， 也叫流式布局
效果: 宽度自适应，高度固定

[百分比布局案例_京东移动端菜单栏](./%E7%BB%83%E4%B9%A0/01-%E7%99%BE%E5%88%86%E6%AF%94%E5%B8%83%E5%B1%80_%E4%BA%AC%E4%B8%9C%E7%A7%BB%E5%8A%A8%E7%AB%AF%E8%8F%9C%E5%8D%95%E6%A0%8F/index.html)



# Flex布局

多个盒子横向排列设置间距，如果使用浮动和margin那么盒子会脱标，如果使用flex布局就没有这个问题，而且布局更灵活快速



**flex布局/弹性布局：**

- 是一<font color="red">种浏览器提倡的布局模型</font>
- 布局网页<font color="red">更简单、灵活</font>
- 避免<font color="red">浮动脱标</font>的问题



## 主轴对齐方式

给需要对齐的的子元素父元素添加 **display: flex**
同时添加**justify-content**调节元素在主轴的对齐方式

|属性值|作用|
|-----|---|
|flex-start|默认值，起点开始一次排序|
|flex-end|终点开始一次排序|
|center|沿主轴居中排列|
|space-around|弹性盒子沿主轴均匀排列，空白间距均分在弹性盒子两侧|
|space-between|弹性盒子沿主轴均匀排列，空白间距均分在相邻盒子之间|
|space-evenly|弹性盒子沿主轴均匀排列，空白间距均分在弹性盒子与容器之间间距相等|

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>体验flex布局</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .box {
            /* 父级元素添加display:flex */
            display: flex;

            /* 沿主轴对齐方式 */
            justify-content: space-evenly;
            border: 1px solid #000;
        }

        .box div {
            width: 100px;
            height: 100px;
            background-color: pink;
        }
    </style>
</head>
<body>
    <!-- 父级盒子 容器-->
    <div class="box">
        <!-- 子盒子 -->
        <div>1</div>
        <div>2</div>
        <div>3</div>
    </div>
</body>
</html>
```



## 测轴对齐方式

**align-items：控制所有弹性盒子（添加到弹性容器）**
**align-self：控制某个弹性盒子在侧轴的对齐方式(添加到弹性盒子)**

|属性值|作用|
|---|---|
|flex-start|默认值，起点开始依次排序|
|flex-end|终点开始一次排序|
|center|沿测轴居中排列|
|stretch|默认值，弹性盒子沿着株洲线被拉伸至铺满容器|

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>侧轴对齐方式</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .box {
            /* 设置display:flex:; */
            display: flex;

            /* 所有弹性盒子居中对齐 */
            align-items: center;

            height: 300px;
            margin: auto;
            border: 1px solid #000;
        }
        
        .box div {
            width: 100px; 
            height: 100px;
            background-color: pink;
        }

        /* 单独设置某个弹性盒子的侧轴对齐方式 */
        .box div:nth-child(3){
            align-self: flex-end;
        }

        
    </style>
</head>

<body>
    <div class="box">
        <div>1</div>
        <div>2</div>
        <div>3</div>
    </div>
</body>

</html>
```



## 伸缩比

可以设置弹性盒子所占父盒子剩余尺寸的比

属性：flex:值;
取值分类:数值(整数)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        /* 给容器设置flex布局 */
        .box {
            display: flex;

            height: 300px;
            border: 1px solid #000;
        }

        .box div {
            height: 200px;
        }

        /* 第一个盒子固定宽度50px */
        .box div:first-child{
            background-color: red;
            width: 50px;
        }

        /* 第二个盒子所在剩余部分的3份(剩余部分3+1) */
        .box div:nth-child(2){
            background-color: yellow;
            flex: 3;
        }

        /* 最后一个盒子所占容器剩余部分的1份(剩余部分3+1) */
        .box div:last-child{
            background-color: green;
            flex: 1;
        }
        
    </style>
</head>
<body>
    <div class="box">
        <div>1</div>
        <div>2</div>
        <div>3</div>
    </div>
</body>
</html>
```



## 修改主轴方向

主轴默认是水平方向，侧轴默认是垂直方向
修改主轴方向属性：flex-direction
|属性值|作用|
|-----|----|
|row|行，水平（默认）|
|<font color="red">column</font>|<font color="red">列，垂直</font>|
|row-reverse|行，从右向左|
|column-reverse|列，从下向上|



## 弹性盒子换行

如果弹性盒子不换行，那么如果一行显示不下盒子不会自动换行而是会挤压变形

弹性盒子换行属性：<font color="red">flex-wrap:wrap</font>;



## flex布局案例

[小兔鲜儿_确认订单移动端](./%E7%BB%83%E4%B9%A0/02-flex_%E5%B0%8F%E5%85%94%E9%B2%9C%E5%84%BF_%E7%A1%AE%E8%AE%A4%E8%AE%A2%E5%8D%95%E7%A7%BB%E5%8A%A8%E7%AB%AF/xiaotuxian/orders.html)

[小兔鲜儿_个人中心web端](./%E7%BB%83%E4%B9%A0/03-flex_%E5%B0%8F%E5%85%94%E9%B2%9C%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83web%E7%89%88/xiaotuxian_web/center.html)



# 移动适配

## rem

rem是一个单位，1rem=1HTML字号大小

**媒体查询**

能够使用媒体查询设置差异化CSS样式，修改不同视口宽度下html字号大小
```css
@media (媒体特性){
    选择器{
        CSS属性
    }
}

@media (width:372px){
    html{
        font-size:37.5rem
    }
}
```
<font color="red">目前热门布局方案中，将网页等份10份，HTML标签的字号是视口宽度的1/10

**确定rem数值**

rem单位的尺寸=px单位数值/基准根字号

**flexible**

使用flexible js配合rem实现在不同宽度的设备中，网页元素尺寸等比缩放效果

在<body>中引入flexible js
```html
<script sec="相对路径"></script> 
```



# Less

Less是一个CSS预处理器，Less文件后缀是.less
但是浏览器不识别less代码，目前阶段，网页要引入对应的CSS文件

**提前在vscode中加入插件：easy less**



## 基本语法
|语法|功能|说明|
|---|----|---|
|//|单行注释|快捷键ctrl+/|
|/* */|块注释|快捷键shift+alt+A|
|+-*(/)|算数运算|除法的写法(1/b)|



## 嵌套

在less中的写法
```less
.father{
    width:200px;

    .son{
        color:red;

        &:hover{
            color:green;
        }
    }
}
```
到css中之后语法
```css
.father{
    width:200px;
}
.father .son{
    color:red;
}
.father .son:hover{
    color:green;
}
```
**<font color="red">注意</font>:&不生成后代选择器，表示当前选择器，通常配合伪类或伪元素使用**



## less变量数值

作用：可以直接批量修改网站中的某一变量

**定义变量**
@变量名:值;

**使用变量**
CSS属性:@变量名;

```less
// 定义变量
@color:red;

// 使用变量
.father{
    color:@color;
}
.son{
    color:@color;
}

/*此时生成的css文件color属性值就是red
如果变量修改成@color:green;
那么css中color的属性值就都会变成green
*/
```



## 导入less

```less
@import '路径';
```
导入less的内容会自动添加到新css里面



## 导出css

现在默认生成css路径是当前文件同级目录，如果要默认生成到一个单独的css文件夹下需要修改

vscode中配置插件: 设置 → 搜索EasyLess → 在setting.json中编辑 → "less.compile":{添加代码}
```
"out":"../css/"
```

**控制当前Less文件导出路径**
less文件第一行添加如下代码，注意文件夹名称后面添加/
```less
// out: ./css/
// out: ./css/common.less
```
这里的//不是注译

**禁止导出**
部分less不需要导出css，比如base、common
```less
//out: false
```
