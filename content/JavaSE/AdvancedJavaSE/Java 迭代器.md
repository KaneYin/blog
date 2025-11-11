# 声明迭代器
```java
public interface Iterator<E>
```

这里 E 代表要迭代的元素类型。

# 什么是迭代器

Java 迭代器是 Java 集合框架中的一种机制，是一种用于遍历集合的接口。提供了一种统一的方式来访问集合中的元素，而不需要了解底层集合的具体实现细节。

Iterator 是 Java 迭代器最简单的实现。


迭代器接口定义了几个方法，最常用的是以下三个：
- next(): 返回迭代器的下一个元素，并将迭代器的指针移到下一个位置。
- hasNext(): 用于判断集合中是否还有下一个元素可以访问。
- remove(): 从集合中删除迭代器最后访问的元素。

Iterator 类位于 java.util 包中，使用前需要引入，语法格式如下：

```Java
import java.util.Iterator;
```

通过使用迭代器，我们可以逐个访问集合中的元素，而不需要使用传统的 for 循环或索引。这种方式更加简洁灵活，并且适合各种类型的集合。
```java
import java.util.Iterator;  
import java.util.ArrayList;  
  
  
public class IteratorDemo {  
    public static void main(String[] args) {  
  
        /* Creating a list */  
        ArrayList<String> sites = new ArrayList<>();  
        sites.add("google");  
        sites.add("Runoob");  
        sites.add("Taobao");  
        sites.add("Bing");  
  
        /* Obtaining an iterator */  
        Iterator<String> it = sites.iterator();  
  
        /* print the first element in the list */  
        System.out.println(it.next());  
    }  
}
```

使用迭代器遍历集合的时候，如果在遍历过程中对集合进行了修改，可能会导致异常，为了避免这个问题，可以使用迭代器自身的 remove() 方法进行删除操作。
## 创建迭代器
```java
Collection<String> names = new ArrayList<>();  
Iterator<String> itr = names.iterator();
```


## 迭代器继承体系

Iterator 位于 java.util 包下，被所有的 Collection 类的子接口实现。
![[Java 迭代器继承体系]]
# 循环集合元素
让迭代器 iterator 逐个返回集合中所有元素最简单的方法是使用 while 循环：
```java
while(it.hasNext()){
	System.out.println(it.next());
}
```

注意：Java 迭代器是一种单向遍历机制，即只能从前往后遍历集合中的元素，不能往回遍历。同时，在使用迭代器遍历集合的时候，不能直接修改集合中的元素，而是需要使用迭代器的 `remove()` 方法来删除当前元素。

# 使用 var 关键字接收迭代器变量
You can also use the `var` keyword with iterators. This avoids repeating the long type name `Iterator<String>`, since the compiler already knows the type from the collection.

This makes code shorter, **but many developers still use the full type for clarity**. Since `var` is valid from Java version 10, you may see it in other code, so it's good to know that it exists:

```java
// without var
Iterator<String> it = sites.iterator();

// with var
var it = sites.iterator();
```
