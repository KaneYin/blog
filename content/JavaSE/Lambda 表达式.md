# What is Lambda Expression
Lambda Expressions were added in Java 8.

A lambda expression is a short block of code which takes in parameters and returns a value. Lambda expressions are similar to methods, but they do not need a name and they can be implemented right in the body of a method.

## Syntax
the simplest lambda expression contains a single parameter and an expression:
```java
parameter -> expression
```
to use more than one parameter, wrap them in parentheses:
```java
(parameter1, parameter2) -> expression
```
Expressions are limited. They have to immediately return a value, and they can not contain variables, assignments or statements such as **if** or **for**. In order to do more complex operations, a code block can be used with curly braces. If the lambda expression needs to return a value, then the code block should have a return statement.
```java
(parameter1, parameter2) -> {code block}
```
## 特点

### 函数式编程支持
Lambda 表达式是函数式编程的一种体现，它允许将函数当作参数传递给方法，或者将函数作为返回值，这种支持使得 Java 在函数式编程方面更为灵活，能够更好地处理集合操作、并行计算等任务。

### 变量捕获
Lambda 表达式可以访问外部外部作用域的变量，这种特征称为变量捕获， Lambda 表达式可以隐式地捕获 final 或事实上是 final 的局部变量。

```java
// 变量捕获
int x = 10;
MyFunction myFunction = y -> System.out.println(x + y);
myFunction.doSomething(5); // 输出 15
```

# Using Lambda Expressions
```java
import java.util.ArrayList;

public class Main {
  public static void main(String[] args) {
    ArrayList<Integer> numbers = new ArrayList<Integer>();
    numbers.add(5);
    numbers.add(9);
    numbers.add(8);
    numbers.add(1);
    numbers.forEach( (n) -> { System.out.println(n); } );
  }
}
```

> Lambda expressions can be stored in variables if the variable's type is an interface which has only one method. The lambda expression should have the same number of parameters and the same return type as that method. Java has many of these kinds of interfaces build-in such as the `Consumer` interface (found in the java.util package) used by lists.


# Reference

1. [W3School Lambda](https://www.w3schools.com/java/java_lambda.asp)
2. [Runoob Lambda](https://www.runoob.com/java/java8-lambda-expressions.html)
3. 