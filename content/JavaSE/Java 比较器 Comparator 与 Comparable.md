Java 中，对集合对象或者数组对象，有两种实现方式：
1. 对象实现 Comparable 接口。
2. 定义比较器，实现 Comparator 接口。（内部可以用传统写法或者 lambda 写法）
两者的区别是一个在集合内部实现，一个是集合外部实现：
```java
class Person implements Comparable<Person>{
	@Override
	public int compareTo(Person person){
		return name.compareTo(person.name);
		// return this.name - person.name;
	}
}
```

```java
Coollections.sort(people, new Comparator<Person>(){
	@Override
	public int compare(Person a, Person b){
		// compare method
		return a.age < b.age ? -1 : a.age == b.age ? 0 : 1;
	}
})
```
Comparable 相当于内部比较器。Comparator 相当于外部比较器。
# Comparable
Java Comparable interface is used to order the objects of the user-defined class.
Comparable 是在集合 Collections 内部定义的方法实现的排序，位于 java.lang。
这个接口仅仅包含一个函数，定义如下：
```java
public interface Comparable<T> {
	public int compareTo(T o);
}
```
- Comparable 是一个对象，本身就已经支持自比较所需要实现的接口。
- 自定义类要在加入 list 容器中后能够排序，也可以实现 Comparable 接口。、
- 在用 Collections 类的 sort 方法排序的时候如不指定 Comparator，那么就以这个类实现 Comparable 接口的方式进行排序。
- 许多 Java 原生类实现了 Comparable 接口，比如：String 和 Integer。这就是为什么 String 和数字不需要比较器就能够使用 Arrays.sort 方法排序。

# Comparator
Comparator 是在集合外部实现的排序，位于 java.util 下。Comparator 接口包含了两个函数。
我们如果需要控制某个类的次序，而该类本身不支持排序（即没有实现 Comparator 接口），那么我们可以新建一个该类的比较器来进行排序。这个比较器只需要实现 comparator 即可。
如果引用的维第三方 jar 包，这个时候没办法改变类本身，可以使用这种方式。


语法：
```java
public int compare(Object obj1, Object obj2);
```
- 如果 $obj1 < obj2$ ，方法将返回负数。
- 如果两个对象相等将会返回 0。
- 如果 $obj1 > obj2$，方法返回正数。

一个实现了 Comparator 接口的类看起来是这样的：
```java
// Sort Car objects by year
class SortByYear implements Comparator {
  public int compare(Object obj1, Object obj2) {
    // Make sure that the objects are Car objects
    Car a = (Car) obj1;
    Car b = (Car) obj2;
    
    // Compare the objects
    if (a.year < b.year) return -1; // The first car has a smaller year
    if (a.year > b.year) return 1;  // The first car has a larger year
    return 0; // Both cars have the same year
  }
}
```
# 什么时候需要使用比较器
- 当排序逻辑不应该在类里面的时候。
- 当需要按照多个属性排序的时候，比如：名字、号码、年龄。


# 参考内容
1. [Java Advanced Sorting](https://www.w3schools.com/java/java_advanced_sorting.asp)
2. 