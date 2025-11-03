> 在学习 Stream 流之前，需要大量使用到[[Lambda 表达式]]，所以这部分内容需要先行掌握比较好。

**Stream 流的思想：**
Java Stream 是一连串的元素序列，可以进行各种操作实现数据的转换和处理。流式编程的概念基于函数编程的思想，旨在简化代码，提高可读性和维护性。并且一般会结合 Lambda 表达式、简化集合、数组的操作。
**使用步骤：**
1. 先得到一条 Stream 流，并把数据放上去。
2. 利用 Stream 流中的 API 进行各种操作。其中 API 又有各种不同类型的：
	1. 中间方法。方法调用完毕后，还可以调用其他方法。
		1. 过滤。
		2. 转换
	2. 终结方法。最后一步，调用完毕以后，不能调用其他方法。
		1. 统计。
		2. 输出打印。
# 如何使用 Stream 流
## 如何得到一条 Steam 流，把数据放上去

| 获取方式   | 方法名                                             | 说明                                     |
| ------ | ----------------------------------------------- | -------------------------------------- |
| 单列集合   | `default Stream<E> stream()`                    | Collection 中的默认方法                      |
| 双列集合   | 无                                               | 无法直接使用 stream 流，需要先转为单列集合再获取 stream 流。 |
| 数组     | `public static <T> Stream<T> stream(<T> array)` | Arrays 工具类中的静态方法                       |
| 一堆零散数据 | `public static <T> Stream <T> of(T ... values)` | Stream 接口中的静态方法                        |

## Stream 流的中间方法

| 名称                                                 | 说明                           |
| -------------------------------------------------- | ---------------------------- |
| `Stream<T> filter(Predicate<? super T> predicate)` | 过滤                           |
| `Stream<T> limit(long maxSize)`                    | 获取前几个元素                      |
| `Stream<T> skip(long n)`                           | 跳过前几个元素                      |
| `Stream<T> distinct()`                             | 元素去重，依赖 hashCode 和 equals 方法 |
| `static <T> Stream<T> concat(Stream a, Stream b)`  | 合并 a 和 b 两个流为一个流             |
| `Stream<R> map(Function<T, R> mapper)`             | 转换流中的数据类型                    |
注意：
- 中间方法，返回新的 Stream 流，原来的 Stream 流只能使用一次，建议使用链式编程。
- 修改 Stream 流中的数据，不会影响原来集合或者数组中的数据。

```java  
import java.util.*;  
import java.util.function.Predicate;  
import java.util.stream.Stream;  
  
/**  
 * 本类用于展示如何正确使用 Stream API  
 */public class StreamAPI {  
    public static void main(String[] args) {  
        List<String> list = new ArrayList<>();  
        Collections.addAll(list, "李浩然", "王思远", "陈雅婷", "赵子轩", "刘语彤", "孙志豪", "张婉琳", "周俊杰", "周俊杰", "周俊杰", "黄心怡", "徐景天");  
  
        // filter 过滤, 把 张 开头的名字留下，剩下的不要  
        list.stream().filter(new Predicate<String>() {  
            @Override  
            public boolean test(String s) {  
                // true 表示要留下的  
                if(s.startsWith("张"))  
                    return true;  
                // false 表示要过滤掉的  
                return false;  
            }  
        }).forEach(System.out::println);  
  
        // 当然我们也可使用 Lambda 表达式简化  
        list.stream().filter(s -> s.startsWith("张")).forEach(System.out::println);  
  
        // 遍历一下原始集合，观察数据是否有被更改，原始数据没有任何变化  
//        for(String s: list){  
//            System.out.println(s);  
//        }  
  
        // 演示 Stream 流中的数据只能使用一次  
        Stream<String> stream = list.stream().filter(s -> s.startsWith("张"));  
        stream.forEach(System.out::println);  
        // 当我们再次想要使用 stream 的时候，就会发现 JVM 抛出了如下错误，说明只要调用了 Stream 终结方法，stream 对象就会关闭  
        /*  
        Exception in thread "main" java.lang.IllegalStateException: stream has already been operated upon or closed            at java.base/java.util.stream.AbstractPipeline.<init>(AbstractPipeline.java:203)            at java.base/java.util.stream.ReferencePipeline.<init>(ReferencePipeline.java:96)            at java.base/java.util.stream.ReferencePipeline$StatelessOp.<init>(ReferencePipeline.java:800)            at java.base/java.util.stream.ReferencePipeline$2.<init>(ReferencePipeline.java:167)            at java.base/java.util.stream.ReferencePipeline.filter(ReferencePipeline.java:166)            at Stream.StreamAPI.main(StreamAPI.java:39)         */        // stream.filter(s -> s.length() == 2).forEach(System.out::println);  
        System.out.println("==================");  
  
        // limit 方法，获取前几个元素  
        list.stream()  
                .limit(5)  
                .forEach(System.out::println);  
  
        System.out.println("==================");  
  
        // skip 方法，用于跳过前几个元素  
        list.stream().skip(5).forEach(System.out::println);  
        System.out.println("==================");  
  
        // distinct 方法用于去重, 底层依赖 hashCode 和 equals 方法，也就是说对于自定义类实现了 hashCode 才能正确去重  
        list.stream().distinct().forEach(System.out::println);  
  
        System.out.println("==================");  
  
        // concat 合并两个流为一个流，需要尽可能保证两个数据类型一致，否则类型会是两个流类型的父类。  
        // 额外创建一个流  
        List<String> s = new ArrayList<>();  
        Collections.addAll(s, "aaa", "bbb");  
        Stream.concat(list.stream(), s.stream()).forEach(System.out::println);  
  
        System.out.println("==================");  
  
        // map 转换流里面的数据类型  
        s.stream()  
                .map(str -> str.toUpperCase())  
                .forEach(a -> System.out.println(a));  
    }  
}
```
## Stream 流的终结方法

> 所谓终结方法，其实就是这个 Stream API 的返回类型不再是 Stream 对象，也就是说一旦调用终结方法，这个 Stream 对象就会在方法执行结束以后关闭。

| 名称                            | 说明            |
| ----------------------------- | ------------- |
| void forEach(Consumer action) | 遍历            |
| long count()                  | 统计            |
| toArray()                     | 收集流中的数据，放到数组中 |
| collect(Collector collector)  | 收集流中的数据，放到集合中 |

