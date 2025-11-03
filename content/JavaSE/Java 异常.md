异常中一个比较重要的规则就是：

**“如果出现 RuntimeException 异常，那么一定是你的问题”**


# 异常机制
在正常情况下，程序会按照预定思维去运行，按理来说是不会出现问题的，但是，代码实际编写过程不是完美的，可能会有没有考虑到的情况。比如下面这段程序：
```java
public class test {  
    public static void main(String[] args) {  
        T(1,0);  
    }  
    public static int T(int a, int b) {  
        return a / b;  
    }  
}
```
这段程序在编译过程中不会出现问题，但是在运行过程中就会抛出异常：
```
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at Exception.test.T(test.java:8)
	at Exception.test.main(test.java:5)
```

> 对于异常情况，例如，可能造成程序崩溃的输入数据，Java 使用了一种称为异常处理（exception handing）的错误捕获机智。Java 中的异常处理与 C++中的异常处理十分类似。
## 异常的类型
在 Java 程序设计语言中，==异常对象都是派生于 Throwable 类的一个类的实例==。稍后还会介绍到，如果 Java 中内置的异常类型不能满足要求，用户还可以创建自己的异常类。
![[Java 中的异常层次类型.png]]
需要注意的是，**Throwable 类下面分为了两个分支，一个是 Error，另一个是 Exception。**
- Error 类层次描述了 Java 运行时系统的内部错误和资源耗尽问题。不应该抛出这种类型的对象，如果出现了这种错误，除了通知用户，并且尽力终止程序以外，几乎无能为力，但是这种情况很少见。
-  编写 Java 程序的时候，重点关注 Exception 层次结构。这个层次下面又分出两个分支
	- **RuntimeException：由编译错误导致的异常属于 RuntimeException。**
	- 另一个分支包括其他异常，不继承运行时异常。

> **继承自 RuntimeException 的异常包括以下问题：**
> - 错误的强制类型转换
> - 越界的数组访问
> - 访问 null 指针
> 
> **不继承自 RuntimeException 的异常包括：**
> - 试图越过文件末尾继续读取数据
> - 试图打开一个不存在的文件
> - 试图根据给定的字符串查找 class 对象，而这个字符串表示的类并不存在。

**“如果出现 RuntimeException 异常，那么一定是你的问题”**。应该通过检测数组索引是否越界来避免 ArrayIndexOutOfBoundsException 异常；如果在使用变量之前先检查这个变量是否为 null，NullPointerException 异常就不会发生。


之前已经接触过一些异常了，比如空指针异常、数组越界异常、算数异常等等，这些都是异常类型，每一个异常都是一个类，它们都继承自 Exception 类！异常类型的本质依然是类的对象，但是异常类型支持程序运行出现问题的时候抛出。
## 声明异常

> ==为什么可能抛出异常的函数需要加上一个 throws ... exception== 的语法，下面这段内容解答了我在学习过程中对于语法的疑惑。

如果遇到了无法处理的情况，Java 方法可以抛出一个异常。这个道理很简单：**方法不仅需要告诉编译器将要返回什么值，还要告诉编译器有可能发生什么错误。**

要在方法的首部指出这个方法可能抛出一个异常，所以就要修改方法的首部，用来反映这个方法可能抛出的异常类型。例如，下面是标准类库中的 FileInputStream 类的一个构造器的声明：
```java
public FileInputStream(String name) throws FileNotFoundException
```

> 这个声明表示这个构造器将根据给定的 String 参数生成一个 FileInputStream 对象，但是也有可能出错而抛出一个 FileNotFoundException 异常。如果真的出现了这种情况，构造器不会初始化一个新的 FileInputStream 对象，而是抛出一个 FileNotFoundException 类的对象。运行时系统就会开始搜索知道如何处理 FileNotFoundException 对象的异常处理器。

### 什么时候应该抛出异常
我们在编写方法的时候，不必声明方法可能抛出的所有 throwable 对象，至于什么时候需要在写的方法中使用 throws 子句声明异常，以及要用 throws 子句声明哪些异常，需要记住在遇到下面 4 种情况时会抛出异常：
- 调用了一个抛出异常的方法，例如，调用了上面提到的 FileInputStream 构造方法
- 检测到一个语句，并且利用 throw 语句抛出一个异常
- 程序出现错误，例如，`a[-1]=0`会抛出一个非检查型异常
- Java 虚拟机或运行时库出现内部错误

出现前面两种情况，则必须告诉使用这个方法的程序员有可能抛出异常。为什么？因为任何一个抛出异常的方法都有可能是一个死亡陷阱。如果没有处理器捕获这个异常，当前的执行线程就会终止。

但是不需要声明 Java 的内部错误，也就是从 Error 继承的异常。任何代码都有可能抛出这些异常，但是我们没有办法控制。

类似的，也==不应该声明从 RuntimeException 继承的那些非检查型异常。==
```java
class Test{

void drawImage(int i) throws ArrayIndexOutOfBoundsException //错误的示例
{
...
}

}
```

这些运行时错误完全在我们的控制之中。如果特别担心数组索引错误. 就应该多花时间修正这些错误，而不只是声明这些错误有可能发生。
### 抛出多个异常
一个方法有可能抛出多个异常类型，那么就必须在方法的首部列出所有的异常类型。每个异常之间用逗号隔开。

```java
class Test{

	public Image loadImage(String s) throws FileNotFoundException,IOException{
	...
	}

}
```

总之，**一个方法必须声明所有可能抛出的检查型异常，而非检查型异常要么在你的控制之外(Error) ，要么是由从一开始就应该避免的情况导致的(RuntimeException)**。
## 如何抛出异常
假设在程序中发生了糟糕的事情。一个名为 readData 的方法正在读取一个文件，文件首部承诺文件长度为 1024 个字符：
```
Content-length: 1024
```
不过读到某个字符以后文件就结束了，这可能是一种不正常那个的情况，希望抛出一个异常。

首先要决定抛出什么类型的异常，可能某种 IOException 是个不错的选择。仔细阅读文档以后发现，EOFException 异常的描述是：“指示输入过程中意外遇到了EOF”，这就是我们需要抛出的异常：
```java
throw new EOFException();
```
下面是完整代码：
```java
String readData(Scanner in) throws EOFException{
	while(...){
		if(!in.hasNext()) // EOF 
		{
			if (n < len)
				throw new EOFException();
		}
	}
	return s;
}
```
EOFException 类还有一个带一个字符串参数的构造器。你可以很好地利用这个构造器，可以用来更加细致地描述异常情况：
```java
String gripe = "Content-length:" + len + ",Received:" + n;
throw new EOFException(gripe);
```
前面已经看到，如果一个已有的异常类能够满足你的要求，抛出这个异常非常容易。在这种情况下：
1. 找到一个合适的异常类
2. 创建这个类的一个对象
3. 将对象抛出

### 创建异常类
当然，代码有时候也会遇到任何标准异常类都无法描述清楚的问题，这种情况下，创建自己的异常类就是顺利成章的事情了。

习惯做法是，自定义的这个类==应该包含两个构造器==，==一个是默认的构造器，另一个是包含详细描述信息的构造器(超类 Throwable 的 toString 方法会返回一个字符串，其中就包含了这个详细信息)。==
```java
class FileFormatException extends IOException{
	// 默认构造器
	public FileFormatException(){}
	// 包含详细信息的构造器
	public FileFormatException(String grip){
	 super(grip);
	}
}
```
现在，就可以抛出自定义的异常类型了。
```java
// 在声明一个方法的时候抛出文件格式异常
String readData(Scanner in) throws FileFormatException{
	while(...){
		if(ch == -1) //EOF
		{
			if(n < len){
				throw new FIleFormatException();
			}
		}
	}
}
```

----

**java.lang.Throwable 1.0 源码解读：**

> Throwable() 创建一个新的 Throwable 对象，但是没有详细的描述信息
> 
> Throwable(String message) 创建一个新的 Throwable 对象，带有指定的详细描述信息。==所有派生的异常类都支持一个默认构造器和一个带有详细信息的构造器。==
> 
> String getMessage() 获得 Throwable 对象的详细描述信息
## 捕获异常

当然，从前面的示例知道：不只是声明异常，还可以捕获异常。这样就不会从这个方法抛出这个异常，所以没有必要使用 throws。后面会讨论如何决定究竟是捕获一个异常，还是将其抛出由其他人捕获。

### 捕获异常概述
如果发生了某个异常，但没有在任何地方捕获这个异常。程序就会终止，并在控制台上打印一个消息。其中包括这个异常的类型和一个栈轨迹。

要捕获一个异常，需要建立 try/catch 语句块。简单的示例如下：
```
try
{
	 code
}
catch(ExceptionType e)
{
	handler for this type
}
```
如果 try 语句块中的任何代码**抛出了 catch 子句中指定的一个异常类**，那么：
1. 程序将跳过 try语句块的其余代码。
2. 程序将执行 catch 子句中的处理器代码。
3. 继续执行 catch 语句块以后的所有代码。
如果 try 语句块中的代码没有抛出任何异常，那么程序将跳过 catch 子句。

但是如果方法中的任何代码抛出了一个异常，但不是 catch 子句中指定的异常类型，那么这个方法就会立即退出。

一个很典型的读取数据的代码：
```java
public void read(String filename){
	try{
		var in = new FileInputStream(filename);
		int b;
		while((b = in.read()) != -1){
			process input
		}
	}
	catch (IOException e){
		e.printStackTrace();
	}
}
```
需要注意的是，try 子句中的大部分代码很容易理解：读取并处理字节，知道遇到文件结束符为止。但是 read 方法有可能抛出一个 IOException 异常。在这种情况下，将跳出整个 while 循环，进入 catch 子句，并生成一个栈轨迹。对于一个简单程序来说，这样处理看上去很有道理，但是还有其他选择吗？
通常，最好的选择是什么也不做，而只是将异常继续传递给调用者“ 如果 read 方法出现了错误，就让 read 方法的调用者去操心这个问题！如果采用这种处理方式，就必须声明这个方法可能会抛出一个 lOException。
```java
public void read(String filename) throws IOException{
	var in = new FileInputStream(filename);
	int b;
	while((b = in.read()) != -1){
		process input
	}
}
```
编译器严格执行 throws 说明符，如果调用了一个抛出检查异常的方法，就必须要处理这个异常，或者继续传递这个异常。
哪种方法更好呢？一般经验来说，要捕获那些你知道如何处理的异常，而继续传递那些你不知道如何处理的异常。

如果要传播一个异常，就必须在方法的首部添加一个 throws 说明符，提醒调用者这个方法可能会抛出一个异常。

### 捕获多个异常
在一个 try 语句块中可以捕获多个异常类型，并对不同类型的异常做出不同的处理。要为每个异常类型使用一个单独的 catch 子句，如下例所示：
```
try
{
	code might throw exceptions
}
catch(FileNotFoundException e)
{
	emergency action for missing files
}
catch(UnknownHostException e)
{
	emergency action for unkown hosts
}
catch(IOException e)
{
	emergencey action for all other IO problems
}

```

异常对象可能包含有关异常性质的信息。可以使用 `e.getMessage()` 得到详细的错误信息，或者使用`e.getClass().getName()`得到异常对象的实际类型。

> 但是这些信息在 e.printStackTrace 中都会展示。
### 再次抛出异常与异常链

### finally 子句
代码抛出一个异常时，就会停止处理这个方法中剩余的代码，并退出这个方法。如果这个方法已经获得了只有它自己知道的一些本地资源，而且这些资源必须清理，这就会有问
题，一种解决方案是捕获所有异常，完成资源的清理，再重新抛出异常。但是，这种解决方案比较烦琐，因为需要在两个地方清理资源分配，一个是在正常的代码中，另一个是在异常代码中。**finally 子句可以解决这个问题**。

不管是否捕获到异常，finally 子句中的代码都会执行，在下面的示例中，所有情况在程序都将关闭输入流：
```java
var in = new FileInputStream();
try{
	 // 1
	 code might throw exceptions
	 // 2
}
catch (IOException e)
{
	// 3
	show error message
	// 4
}
finally
{
	// 5
	in.close();
}

// 6
```

==上面这段代码执行 finally 子句的 3 种可能的情况==：
1. **代码没有抛出异常**。在这种情况下，程序首先执行 try 语句块中的全部代码，然后执行 finally 子句中的代码。 随后，继续执行 finally 子句之后的第一条语句。也就是说，执行的顺序是 1、2、 5、6。
2. **代码抛出一个异常，并在一个 catch 子句中捕获**。程序首先执行 try 语句中的代码，抛出一个异常以后，转到 catch 语句中的代码（意味着 try 语句快中的剩余代码将会被忽略）。然后继续执行 finally 子句之后的代码。执行的顺序是 1、3、4、5、6
3. **代码抛出一个异常，但是没有 catch 子句捕获这个异常**。这种情况下，程序将执行 try 语句中的所有语句，直到抛出异常位置。此时，将跳过 try 语句块中的剩余代码，然后执行 finally 子句中的语句，并将异常抛回给方法的调用者。执行的顺序是：1、5。

try 语句可以只有 finally 语句，而没有 catch 语句。例如：
```java
input Stream in = ...
try{
	code might throw exceptions
}
finally{
	in.close
}
```
 无论在 try 语句块中是否遇到异常，finally 子句中的 in.close() 语句都会执行。当然，如果真的遇到一个异常，这个异常将会被重新抛出，并且必须由另一个 catch 子句捕获。
```
InputStream in = ... ;
try{
	try{
		code might throw exceptions
	}
	finally{
		in.close();
	}
}
catch(IOException e){
	 show error message
}
```
**内层的 try 语句只有一个职责，那就是确保关闭输入流。外层的 try 语句也只有一个职责，那就是确保报告出现的错误。** 这种解决方案不仅更清楚，而且功能性更强；将会报告 finally 子句中出现的错误。
### try-with-Resources 语句

### 分析栈轨迹 Stack Trace
Stack Trace 是程序执行过程中某个特定点上所有挂起的方法调用的一个列表。**当 Java 程序因为一个未捕获的异常而终止的时候，就会显示 Stack Trace**。

可以调用 Throwable 类的 printStackTrace 方法访问栈轨迹的文本描述信息：
```
var t = new Throwable();
var out = new StringWriter();
t.printStackTrace(new PrintWriter(out));
String desvription = out.toString();
```
## 使用异常的技巧
1. **异常处理不能代替简单的测试**
	假设一段代码将一个空栈弹出 10,000,000 次，
	1. 第一种做法是先查看栈是否为空：`if(!s.isEmpty()) s.pop()` 
	2. 第二种做法是要求不管怎么样都执行弹出操作，然后捕获 EmptyStackException 异常告诉我们不该这样做：`try{s.pop} catch(EmptyStackException e){}`
	调用 isEmpty 的版本相比每一次都执行，然后捕获栈为空的异常的版本运行速度快很多。可以看到，与完成简单的测试相比，捕获异常花费的时间大大超过了前者，因此使用异常的基本规则是：只在异常情况下使用异常。
2. **不要过分细化异常**
	很多程序员将每一条语句都分装在一个单独的 try 语句块中。
	![[过分细化异常.png]]
	这种编码方式将导致代码量的急剧膨胀。
3. **合理利用异常层次结构**
4. **不要压制异常**
5. **在检测错误时，“苛刻” 要比放任更好**
6. **不要羞于传递异常**
7. **使用标准方法报告 null 指针和越界异常**
8. **不要向最终用户显示栈轨迹**
### 运行时异常
异常的第一种类型是运行时异常，如上述的例子，在编译阶段无法感知程序是否会出现问题，只有在运行过程中才知道是否出错，这种异常称为运行时异常，运行时异常继承自 Runtimeexception。

### 编译时异常
异常的另一种类型是编译时异常，编译时异常明确指出可能出现的异常情况，在编译阶段就需要进行处理（也就是捕获异常）必须要考虑出现异常的情况，如果不进行处理，将无法通过编译。默认继承自 Exception 类的异常都是编译时异常。

## 异常与错误
还有一种类型是错误，错误比异常更加严重，异常只是程序出现了问题，而错误是致命问题，一般出现错误可能导致 JVM 虚拟机无法正常运行了，比如 StackOverflowError 就是栈溢出错误。