# JavaScript基本介绍

**Html/Css/Js的关系**

![图片9](/Users/Zander/GitHub/study_notes/JavaScript/images/图片9-2014905.png)

## 引入js

**内嵌式**

```html
<script>
    alert('Hello  World~!');
</script>
```

在html中可以将js代码写到<script>中，可以写多行，一般把script放到<body>后面

**外部JS文件**

```html
<script src="路径"></script>
```

- 利于HTML页面代码结构化，把大段 JS代码独立到 HTML 页面之外，既美观，也方便文件级别的复用
- 引用外部 JS文件的 script 标签中间不可以写代码
- 适合于JS 代码量比较大的情况



# 基本语法

## 注释

```
// 用来注释单行文字（  快捷键   ctrl  +  /   ）

/* */  用来注释多行文字（ 默认快捷键  alt +  shift  + a ） 
```



##  JavaScript输入输出语句

为了方便信息的输入输出，JS中提供了一些输入输出语句，其常用的语句如下：

| 方法             | 说明                           | 归属   |
| ---------------- | ------------------------------ | ------ |
| alert(msg)       | 浏览器弹出警示框               | 浏览器 |
| console.log(msg) | 浏览器控制台打印输出信息       | 浏览器 |
| prompt(info)     | 浏览器弹出输入框，用户可以输入 | 浏览器 |

- 注意：alert() 主要用来显示消息给用户，console.log() 用来给程序员自己看运行时的消息。



# 变量

## 使用变量

```js
var age; // 只声明变量

var age = 18;
// 变量初始化，age是变量 ，18是赋给变量的值
```

**同时声明多个变量**

```js
var usrName = 'fanyi_c',
    age = 24,
	sex = '男';
```



## 变量命名规范

```
- 由字母(A-Za-z)、数字(0-9)、下划线(_)、美元符号( $ )组成，如：usrAge, num01, _name
- 严格区分大小写。var app; 和 var App; 是两个变量
- 不能 以数字开头。  18age   是错误的
- 不能 是关键字、保留字。例如：var、for、while
- 变量名必须有意义。 MMD   BBD        nl   →     age  
```



# 数据类型

## 简单数据类型
|简单的数据类型|说明|默认值|
| ------ | ------------------------ | ---- |
| Number | 数字型，包含整型和浮点型 | 0    |
| Boolean | 布尔型 | false |
| Sreing | 字符串 | "" |
| Undefined | var a;声明了变量a但是没有给值 | undefined |
| null | Var a = null;声明了变量a为空值 | null |



### 数字型 Number

​	JavaScript 数字类型既可以保存整数，也可以保存小数(浮点数）。  

```js
var age = 21;       // 整数
var Age = 21.3747;  // 小数     
```

1. 数字型进制

   最常见的进制有二进制、八进制、十进制、十六进制。

   ```js
     // 1.八进制数字序列范围：0~7
    var num1 = 07;   // 对应十进制的7
    var num2 = 019;  // 对应十进制的19
    var num3 = 08;   // 对应十进制的8
     // 2.十六进制数字序列范围：0~9以及A~F
    var num = 0xA;   
   ```

   现阶段我们只需要记住，在JS中八进制前面加0，十六进制前面加 0x  

2. 数字型范围

   JavaScript中数值的最大和最小值

   - 最大值：Number.MAX_VALUE，这个值为： 1.7976931348623157e+308

   - 最小值：Number.MIN_VALUE，这个值为：5e-32

3. 数字型三个特殊值

   - Infinity ，代表无穷大，大于任何数值

   - -Infinity ，代表无穷小，小于任何数值

   - NaN ，Not a number，代表一个非数值

  4. isNaN

     用来判断一个变量是否为非数字的类型，返回 true 或者 false

![图片17](/Users/Zander/GitHub/study_notes/JavaScript/images/图片17.png)

   ```js
  var usrAge = 21;
var isOk = isNaN(userAge);
  console.log(isNum);          // false ，21 不是一个非数字
var usrName = "andy";
  console.log(isNaN(userName));// true ，"andy"是一个非数字
   ```



### 字符串型 String

​	字符串型可以是引号中的任意文本，其语法为 双引号 "" 和 单引号''

```js
var strMsg = "我爱北京天安门~";  // 使用双引号表示字符串
var strMsg2 = '我爱吃猪蹄~';    // 使用单引号表示字符串
// 常见错误
var strMsg3 = 我爱大肘子;       // 报错，没使用引号，会被认为是js代码，但js没有这些语法
```

​	因为 HTML 标签里面的属性使用的是双引号，JS 这里我们更推荐使用单引号。

1. 字符串引号嵌套

   ​		JS 可以用单引号嵌套双引号 ，或者用双引号嵌套单引号 (外双内单，外单内双)

   ```js
   var strMsg = '我是"高帅富"程序猿';   // 可以用''包含""
   var strMsg2 = "我是'高帅富'程序猿";  // 也可以用"" 包含''
   //  常见错误
   var badQuotes = 'What on earth?"; // 报错，不能 单双引号搭配
   ```

2. 字符串转义符

   ​		类似HTML里面的特殊字符，字符串中也有特殊字符，我们称之为转义符。

   ​		转义符都是 \ 开头的，常用的转义符及其说明如下：

   | 转义符 | 解释说明                          |
   | ------ | --------------------------------- |
   | \n     | 换行符，n   是   newline   的意思 |
   | \ \    | 斜杠   \                          |
   | \'     | '   单引号                        |
   | \"     | ”双引号                           |
   | \t     | tab  缩进                         |
   | \b     | 空格 ，b   是   blank  的意思     |

3. 字符串长度

   			字符串是由若干字符组成的，这些字符的数量就是字符串的长度。通过字符串的 length 属性可以获取整个字符串的长度。

   ```js
   var strMsg = "我是帅气多金的程序猿！";
   alert(strMsg.length); // 显示 11
   ```

4. 字符串拼接

   - 多个字符串之间可以使用 + 进行拼接，其拼接方式为 字符串 + 任何类型 = 拼接之后的新字符串

   - 拼接前会把与字符串相加的任何类型转成字符串，再拼接成一个新的字符串

     ```js
     //1.1 字符串 "相加"
     alert('hello' + ' ' + 'world'); // hello world
     //1.2 数值字符串 "相加"
     alert('100' + '100'); // 100100
     //1.3 数值字符串 + 数值
     alert('11' + 12);     // 1112 
     ```

     - ***+ 号总结口诀：数值相加 ，字符相连***

5. 字符串拼接加强

   ```js
   console.log('pink老师' + 18);        // 只要有字符就会相连 
   var age = 18;
   console.log('pink老师age岁啦');      // 这样不行哦
   console.log('pink老师' + age);         // pink老师18
   console.log('pink老师' + age + '岁啦'); // pink老师18岁啦
   ```

   - 经常会将字符串和变量来拼接，变量可以很方便地修改里面的值
   - 变量是不能添加引号的，因为加引号的变量会变成字符串
   - 如果变量两侧都有字符串拼接，口诀“引引加加 ”，删掉数字，变量写加中间

### 布尔型Boolean

​		布尔类型有两个值：true 和 false ，其中 true 表示真（对），而 false 表示假（错）。

​		布尔型和数字型相加的时候， true 的值为 1 ，false 的值为 0。

```js
console.log(true + 1);  // 2
console.log(false + 1); // 1
```

- Undefined和 Null

  ​		一个声明后没有被赋值的变量会有一个默认值undefined ( 如果进行相连或者相加时，注意结果）

  ```js
  var variable;
  console.log(variable);           // undefined
  console.log('你好' + variable);  // 你好undefined
  console.log(11 + variable);     // NaN
  console.log(true + variable);   //  NaN
  ```

  ​		一个声明变量给 null 值，里面存的值为空（学习对象时，我们继续研究null)

  ```js
  var vari = null;
  console.log('你好' + vari);  // 你好null
  console.log(11 + vari);     // 11
  console.log(true + vari);   //  1
  ```

  

## 获取变量数据类型



**获取检测变量的数据类型**

typeof 可用来获取检测变量的数据类型

```js
var num = 18;
console.log(typeof num) // 结果 number      
```

​		不同类型的返回值

![图片18](/Users/Zander/GitHub/study_notes/JavaScript/images/图片18.png)



- 字面量

  ​		字面量是在源代码中一个固定值的表示法，通俗来说，就是字面量表示如何表达这个值。

  - 数字字面量：8, 9, 10
  - 字符串字面量：'黑马程序员', "大前端"
  - 布尔字面量：true，false
  - 

## 数据类型转换

​		什么是数据类型转换？

​		使用表单、prompt 获取过来的数据默认是字符串类型的，此时就不能直接简单的进行加法运算，而需要转换变量的数据类型。通俗来说，就是把一种数据类型的变量转换成另一种数据类型，通常会实现3种方式的转换：

```
转换为字符串类型
转换为数字型
转换为布尔型
```

- 转换为字符串

  ![图片19](/Users/Zander/GitHub/study_notes/JavaScript/images/图片19.png)

  - toString() 和 String()  使用方式不一样。
  - 三种转换方式，更多第三种加号拼接字符串转换方式， 这一种方式也称之为隐式转换。

- 转换为数字型（重点）

  ![图片20](/Users/Zander/GitHub/study_notes/JavaScript/images/图片20.png)

  - 注意 parseInt 和 parseFloat 单词的大小写，这2个是重点
  - 隐式转换是我们在进行算数运算的时候，JS 自动转换了数据类型

- 转换为布尔型

  ![图片21](/Users/Zander/GitHub/study_notes/JavaScript/images/图片21.png)

  - 代表空、否定的值会被转换为 false  ，如 ''、0、NaN、null、undefined  

  - 其余值都会被转换为 true

    ```js
    console.log(Boolean('')); // false
    console.log(Boolean(0)); // false
    console.log(Boolean(NaN)); // false
    console.log(Boolean(null)); // false
    console.log(Boolean(undefined)); // false
    console.log(Boolean('小白')); // true
    console.log(Boolean(12)); // true
    ```


## 
