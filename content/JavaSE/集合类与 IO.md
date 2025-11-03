# 集合类
前面已经把所有的基础内容介绍了，这篇笔记正式进入集合类中：

集合类是 Java 中非常重要的存在，使用频率非常高。集合其实与我们数学中的集合是差不多的概念，集合表示一组对象，每一个对象我们都可以称其为元素。不同的集合有着不同的性质，比如一些集合运行重复的元素，而另一些则不允许，一些集合是有序的，而其他则是无序的。

集合类其实就是为了更好地组织、管理和操作我们的数据而存在的，包括**列表、集合、队列、映射**等数据结构。从这一块开始，我们从源码角度来讲解（先从接口定义对于集合需要实现哪些功能，包括这些集合类的底层机制如何运作）不仅仅教会大家如何使用。

集合和数组一样，可以表示同样的一组元素，但是他们的相同和不同之处在于：
- 它们都是容器，能够容纳一组元素。

不同之处：
- 数组的大小是固定的，集合的大小是可变的。
- 数组可以存放基本数据类型，但集合只能存放对象。

## 集合根接口 Collection
Java 中已经帮我们把常用的集合类型都实现好了，我们只需要拿来使用即可，比如我们之前学习的顺序表：

```java
import java.util.ArrayList

public class Main{
	public static void main(String[] args){
		ArrayList<String> list = new ArrayList<>();
		list.add("1");
	}
}
```

 我们会在这一部分认识大部分 Java 为我们提供的集合类。所有的集合类最终都是实现自集合根接口的，比如我们下面就会讲到 ArrayList 类，它的祖先就是 Collection 接口：
![](ArrayList)

 这个接口定义了集合类的一些基本操作，方法如下：
```java
public interface Collection<E> extends Iterable<E>{

	// 这些是查询相关的操作

	// 获取当前集合中的元素数量
	int size();
	
	// 查看当前集合是否为空
	boolean isEmpty();
	
	// 查询当前集合中是否包含某个元素
	boolean contains(Object o);
	
	// 生成当前集合的一个迭代器
	Iterator<E> iterator();
	
	// 把当前集合转换为对应的数组
	Object[] toArray();
	
	// 有参数的 toArray 方法，转换为对应类型的数组
	<T> T[] toArray(T[] a);
	
	// 向集合中添加元素，不同的集合类可能会对插入的元素有要求
	// 这个操作不一定会添加成功，添加成功返回 true，添加失败返回 false
	boolean add(E e);
	
	// 移除集合中的某个元素
	boolean remove(Object o);
	// 批量执行的操作
	
	// 查询当前集合是否包含给定集合中的所有元素
	// 从数学角度来看，就是看给定集合是不是当前元素的子集
	boolean containsAll(Collection<?> c);
	
	// 添加给定集合中的所有元素
	// 数学上，就是求给定集合与当前集合的并集
	// 成功返回 true，失败返回 false
	boolean addAll(Collection<? extends E> c);
	
	// 移除给定集合中出现的所有元素，如果某个元素在当前集合中不存在，那么就忽略这个元素
	// 数学上，就是求当前集合与给定集合的差集
	// 移除成功返回 true，失败返回 false
	boolean removeAll(Collection<?> c);
	
	// Java8 新增方法，根据给定的 Predicate 条件进行元素移除操作
	default boolean removeIf(Predicate<? super E> filter);
	
	// 只保留当前集合中给定集合中出现的元素，其他元素一律移除
	// 数学上，就是当前集合与给定集合的交集
	// 移除成功返回 true，否则返回 false
	boolean retainAll(Collection<?> c);
	
	// 清空整个集合，删除所有元素
	void clear();
	
	// TODO 比较以及哈希计算相关的操作
	
}


```

 
 