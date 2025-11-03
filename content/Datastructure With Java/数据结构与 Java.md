在了解集合类之前，还有关键的内容需要学习。由于自底向上的学习方法才是最好的学习方向，所以这里先使用 Java 语言实现一下基本的数据结构，然后再来了解 Java 官方提供的数据结构工具类。当然，这里主要是关于 JavaSE 的知识点，数据结构知识作为铺垫作用，只包含数据结构的关键部分，其他部分详见数据结构与算法笔记。

所谓数据结构，通俗地说，就是学习如何在计算机当中更好地管理数据，能让我们对数据控制更加灵活。
# 线性表 Linear List

> 线性表是由同一类型的数据元素构成的有序序列的线性结构，线性表中元素的个数就是线性表的长度，表的起始位置称为表头，表的结束位置称为表尾，当一个线性表中没有元素的时候，称为空表。

线性表一般需要包含以下的功能：
- **获取指定位置上的元素**：直接获取线性表指定位置 i 上的元素。
- **插入元素**：在指定位置 i 上插入一个元素。
- **删除元素**：删除指定位置 i 上的一个元素。
- **获取长度**：返回线性表的长度。
也就是说，现在我们需要设计的是一种功能结构完善的表结构，不是像数组那样低级的，而是真正意义上的表。比如我们要设计菜单的时候，点菜过程中需要在菜单中添加或者删除菜品，这时列表就很有用了，因为数组长度固定、操作简单，数组无法满足长度动态变化的需求。
## 线性表：顺序表
既然数组无法实现这样的高级表的功能，那么我们就基于数组，对其进行强化，我们存放数据的还是使用数组，但是可以可以通过一些操作来强化为线性表，像这样底层依然采用顺序存储实现的线性表，称为顺序表。
这里我们定义一个新的类型：
```java
/**  
 * 采用数组实现的顺序表  
 * @param <E>  
 */  
public class ArrayList<E> {  
    /**  
     * capacity 代表顺序表的默认长度  
     */  
    private int capacity = 10;  
    /**  
     * size 记录当前表储存的元素个数  
     */  
    int size = 0;  
    private Object[] array = new Object[capacity];  
}
```
### 插入元素
当插入元素的时候，需要将插入位置空出来，也就是将后面的所有元素往后移动，同样的，如果要删除元素，就要将所有的元素往前移动。因为顺序表是紧凑的，不能出现空位。
```java
/**  
 * 插入元素的方法  
 * @param element 待插入的元素  
 * @param index 插入元素的位置  
 */  
public void add(E element,int index) {        
    // 首先将指定位置后面的元素全部往后移动  
    // 注意这里循环不能从前面往后面进行，否则后面位置的元素会被覆盖  
    for (int i = size; i > index; i--) {  
        array[i] = array[i - 1];  
    }  
    // 然后再将元素放到指定位置处  
    array[index] = element;  
    size++;  
}
```
只不过这样并不完美，因为插入操作并不是能够在任何位置都支持插入的，允许插入的位置只能是`[0,size]` 这个范围内：
![顺序表能够插入的位置](顺序表能够插入的位置.md)
所以在插入之前还要进行判断：
```java
public void add(E element,int index) {  
    // 判断传入的 index 是否合法  
    if(index < 0 ||index > size){  
        throw new IndexOutOfBoundsException("插入位置非法，合法的插入位置为：0～" + size);  
    }  
  
    // 首先将指定位置后面的元素全部往后移动  
    // 注意这里循环不能从前面往后面进行，否则后面位置的元素会被覆盖  
    for (int i = size; i > index; i--) {  
        array[i] = array[i - 1];  
    }  
    // 然后再将元素放到指定位置处  
    array[index] = element;  
    size++;  
}public void add(E element,int index) {  
    // 判断传入的 index 是否合法  
    if(index < 0 ||index > size){  
        throw new IndexOutOfBoundsException("插入位置非法，合法的插入位置为：0～" + size);  
    }  
  
    // 首先将指定位置后面的元素全部往后移动  
    // 注意这里循环不能从前面往后面进行，否则后面位置的元素会被覆盖  
    for (int i = size; i > index; i--) {  
        array[i] = array[i - 1];  
    }  
    // 然后再将元素放到指定位置处  
    array[index] = element;  
    size++;  
}
```
测试一下假如插入位置越界：
```java
public class test {  
    public static void main(String[] args) {  
        ArrayList<String> list = new ArrayList<>();  
        list.add("a",0);  
        list.add("b",1);  
        // 这里最后插入的 “c“ 就是非法位置
        list.add("c",3);  
    }  
}
```
运行以后，编译器报错，报错信息为：
```
Exception in thread "main" java.lang.IndexOutOfBoundsException: 插入位置非法，合法的插入位置为：0～2
	at DatastructureWithJava.LinearList.ArrayList.add(ArrayList.java:26)
	at DatastructureWithJava.LinearList.test.main(test.java:8)

Process finished with exit code 1
```
当然，还是有不完美的情况，假如顺序表装满以后应该怎么办呢，所以还要加上判断顺序表是否为 full 的判断条件，装满以后可以通过手动扩容的方式给顺序表中插入新的元素：
```java
/**  
 * 插入元素的方法  
 * @param element 待插入的元素  
 * @param index 插入元素的位置  
 */  
public void add(E element,int index) {  
  
    // 判断传入的 index 是否合法  
    if(index < 0 ||index > size){  
        throw new IndexOutOfBoundsException("插入位置非法，合法的插入位置为：0～" + size);  
    }  
  
    // 判断线性表是否为满  
    if(size >= capacity){  
        // 扩容为原来的两倍  
        int newCapacity = capacity * 2;  
        Object[] newArray = new Object[newCapacity];  
        System.arraycopy(array,0,newArray,0,size);  
        // 更新原来的 array 和 capacity        array = newArray;  
        capacity = newCapacity;  
    }  
  
    // 首先将指定位置后面的元素全部往后移动  
    // 注意这里循环不能从前面往后面进行，否则后面位置的元素会被覆盖  
    for (int i = size; i > index; i--) {  
        array[i] = array[i - 1];  
    }  
    // 然后再将元素放到指定位置处  
    array[index] = element;  
    size++;  
}  
  
// 重写类的 toString 方法，在打印 ArrayList 对象的时候，会自动调用这个方法  
public String toString(){  
    StringBuilder stringBuilder = new StringBuilder();  
    for (int i = 0; i < size; i++) {  
        stringBuilder.append(array[i]).append(" ");  
    }  
    return stringBuilder.toString();  
}
```
目前为止，这个添加元素的方法就比较完整了。
### 删除元素
删除元素和插入元素操作差不多，甚至更加简单，只需要将后面的覆盖到前面就可以：
```java
/**  
 * 删除指定位置处的元素  
 * @param index  
 * @return E e 返回值是删除的元素  
 */  
@SuppressWarnings("unchecked")  
public E remove(int index) {  
    // 合法的删除位置和插入位置有一点点不一样，这里是开区间  
    if(index < 0 ||index >= size){  
        throw new IndexOutOfBoundsException("删除位置不合法,合法的删除位置为：0～" + (size - 1));  
    }  
    E e =  (E) array[index];  
    // 删除元素的时候就需要从前往后面遍历  
    for (int i = index; i < size; i++) {  
        array[i] = array[i + 1];  
    }  
    // 最后不要忘记 size--
    size--;
    return e;  
}
```
现在进行一下测试：
```java
public class test {  
    public static void main(String[] args) {  
        ArrayList<String> list = new ArrayList<>();  
        list.add("a",0);  
        list.add("b",1);  
        list.add("c",2);  
        list.remove(1);  
        System.out.println(list); // a c  
    }  
}
```
输出结果没有问题。
### 获取元素

### 判空与判满


## 线性表：链表
前面介绍了如何使用数组实现线性表，接下来介绍第二种方式，可以使用链表来实现：
![](链表示意图.md)

链表不同于顺序表，顺序表底层使用数组作为存储容器，需要分配一块连续并且完整的内存空间进行使用，但是链表则不需要，它通过一个指针来连接各个分散的结点，形成了一个链状的结构，每个结点存放一个元素，以及一个指向下一个结点的指针，通过这样一个一个相连，最后形成了链表。链表不需要申请连续的空间，只需要按照顺序连接即可，物理上不相邻，但是在逻辑上依然是每个元素相邻存放的，这样的结构叫做链表。

链表分为带头结点的链表和不带头结点的链表，带头结点的链表就是会有一个头结点指向后续的整个链表，但是头结点不存放数据：

而不带头结点的链表就像上面的图示一样，第一个结点就是存放数据的结点，**一般设计链表都会采用带头结点的结构，因为操作更加方便**。

代码定义如下：
```java
public class LinkedList<E> {  
    // 头结点默认不存储任何元素，所以 element:null    
    private Node<E> head = new Node<>(null);  
  
    private int size = 0;  
  
    // 定义内部类，表示链表上面的结点  
    private static class Node<E> {  
         // 每个结点都存放元素  
         private E element;  
  
         // 以及指向下一个结点的引用  
         private Node<E> next;  
  
        // 内部类的构造方法  
         public Node(E element) {  
             this.element = element;  
         }  
    }  
      
}
```

接着我们设计一下链表的插入和删除操作，前面实现了顺序表的插入，那么链表的插入应该如何实现呢？
### 插入元素
我们可以先修改新插入的结点的后继结点（也就是下一个结点）指向，让新插入的结点指向原本在这个位置的结点，再让前面的结点指向新插入的结点：
![带头结点的链表插入示意图](带头结点的链表插入示意图.md)

按照这个思路，我们可以实现一下 add 方法：
```java
/**  
 * 链表的插入元素方法
 * @param element 插入的元素  
 * @param index 指定的插入位置  
 */  
public void add(E element, int index){  
    if(index < 0 || index > size){  
        throw new IndexOutOfBoundsException("插入位置异常，合法的插入位置是：0~" + size);  
    }  
    Node<E> node = new Node<>(element);  
    Node<E> prev = head;  
    for(int i = 0 ; i < index ; i++){  
        prev = prev.next;  
    }  
    // 这两个语句顺序不能反，否则会丢失插入元素以后的所有元素  
    node.next = prev.next;  
    prev.next = node;  
    size++;  
}
```
然后重写一下 toString 方法，以便测试：
```java
/**  
 * 重写的 toString 方法  
 * @return  
 */public String toString(){  
    StringBuilder stringBuilder = new StringBuilder();  
    Node<E> node = head.next;  
    for (int i = 0; i < size; i++) {  
        stringBuilder.append(node.element).append(" ");  
        node = node.next;  
    }  
    return stringBuilder.toString();  
}
```

测试插入方法：
```java
public class test {  
    public static void main(String[] args) {  
        LinkedList<Integer> list = new LinkedList<>();  
        list.add(1,0);  
        list.add(2,1);  
        list.add(3,1);  
        System.out.println(list);// 1 3 2
    }  
}
```
### 删除操作
插入操作完成以后，接着来看删除操作。删除操作逻辑上也很简单，就是让被删除元素的前驱结点的后向指针直接指向被删除元素后向指针指向的元素：
![链表删除结点示意](链表删除结点示意.md)
代码实现如下：
```java
public class test {  
    public static void main(String[] args) {  
        LinkedList<Integer> list = new LinkedList<>();  
        list.add(1,0);  
        list.add(2,1);  
        list.add(3,2);  
        System.out.println(list);  
        // 删除第一个元素  
        list.remove(0);  
        System.out.println(list);  
    }  
}
```
输出结果为：
```
1 2 3 
2 3 
```
这样我们就成功完成了链表的删除操作。

### 获取元素
接下来实现一下获取对应位置上面的位置：
```java
public E get(int index){  
    if(index < 0 || index >= size){  
        throw new IndexOutOfBoundsException("获取的元素位置非法，合法位置为0~" + (size - 1));  
    }  
    // 一定要从头结点开始  
    Node<E> prev = head;  
    for (int i = 0; i < index; i++) {  
        prev = prev.next;  
    }  
    return prev.next.element;  
}
```
测试一下代码是否正确：
```java
public class test {  
    public static void main(String[] args) {  
        LinkedList<Integer> list = new LinkedList<>();  
        list.add(1,0);  
        list.add(2,1);  
        list.add(3,2);  
        System.out.println(list);  
        Integer num = list.get(0);  
        System.out.println(num);  
    }  
}
```

这样，我们的链表就编写完成了，实际上只要理解了这种结构，还是非常简单的！
## 线性表 V.S. 链表
学习完线性表和链表以后，我们应该在什么时候使用线性表，什么时候使用链表呢？
 - 通过分析顺序表和链表的特性，不难发现，链表在随机访问元素的时候，需要通过遍历来完成，而顺序表利用数组的特性直接访问得到，所以当我们需要读取数据多于插入或者删除数据的情况下，使用顺序表会更好。
 - 顺序表在插入元素的时候显得有些不方便，因为要移动后续元素，整个移动操作会浪费时间，而链表则不需要，只需要修改结点指向就可以完成插入，所以在频繁出现插入或者删除的情况下，使用链表会更好。

虽然单链表使用起来比较方便，不过有一个问题就是，如果我们想要操作某一个结点，比如删除或是插入，那么由于单链表的性质，我们只能先去找到它的前驱结点，才能进行。为了解决这种查找前驱结点非常麻烦的问题，我们可以让结点不仅保存指向后续结点的指针，同时也保存指向前驱结点的指针：
![](双向链表示意图.md)
这样无论我们在哪个结点，都能快速找到对应的前驱结点，就很方便了，这样的链表我们称为双向链表。
## 栈

栈（Stack）是一种特殊的线性数据结构，只能在表尾进行插入和删除操作，就像下面这样：
比如，当我们依次插入 1、2、3、4 这四个元素以后，连续进行四次删除操作，删除的顺序正好相反：4、3、2、1 。
如下图所示，我们把堆叠元素的顶部称为 “栈顶”，底部称为 “栈底”。将把元素添加到栈顶的操作叫做 “入栈”，删除栈顶元素的操作叫做 “出栈”。
![栈的操作示意图](栈的操作示意图.md)
它是一种先进后出的数据结构（FILO，First In Last Out）。

实现栈的方式也非常简单，可以基于前面的顺序表或者是链表，但是需要实现两种新的操作：
- pop( ): 出栈操作，从栈顶取出一个元素。
- push( )：入栈操作，向栈中压入一个新的元素。
- peek( )：访问栈顶元素。

我们使用链表实现栈的结构，因为实际上使用链表会更加的方便，我们可以直接将头结点指向栈顶结点，而栈顶结点连接后续的栈内结点：
### 栈的实现
#### 基于链表的实现
使用链表实现栈的时候，==可以将链表的头节点视为栈顶，尾结点视为栈底==。
当有新的元素入栈以后，只需要在链表头部插入新的结点即可，这种节点插入方法被称为 “头插法”，代码如下：
```java

```

#### 基于数组的实现
使用数组实现栈时，可以将数组的尾部作为栈顶。入栈与出栈操作分别在数组尾部添加元素与删除元素：
由于入栈的元素可能会不断增加，所以可以使用动态数组（也就是 ArrayList 类）这样就不用自己处理数组扩容问题。
```java
package DatastructureWithJava.ArrayStack;  
  
import java.util.ArrayList;  
import java.util.EmptyStackException;  
  
/**  
 * 使用动态数组实现自己的栈  
 */  
public class MyArrayStack <E> {  
    private ArrayList<E> arrayList;  
  
    // 构造方法  
    public MyArrayStack() {}  
  
    /**  
     * 入栈操作  
     * @param element  
     */  
    public void push(E element) {  
        arrayList.add(element);  
    }  
  
    /**  
     * 出栈操作  
     * @return  
     */    public E pop(){  
        if(arrayList.isEmpty()){  
            throw new EmptyStackException();  
        }  
        E element = arrayList.remove(arrayList.size() - 1);  
        return element;  
    }  
  
    /**  
     * 取栈顶元素  
     * @return  
     */    public E peek(){  
        if(arrayList.isEmpty()){  
            throw new EmptyStackException();  
        }  
        return arrayList.get(arrayList.size() - 1);  
    }  
  
    /**  
     * 判断栈是否为空  
     */  
    boolean isEmpty(){  
        return arrayList.isEmpty();  
    }  
}
```
#### 两种实现的对比
**支持的操作**：两种实现都支持栈定义中的各项操作。数组实现额外支持随机访问，但这已超出了栈的定义范畴，因此一般不会用到。
**空间效率**：在初始化列表时，系统会为列表分配“初始容量”，该容量可能超出实际需求；并且，扩容机制通常是按照特定倍率（例如 2 倍）进行扩容的，扩容后的容量也可能超出实际需求。因此，==基于数组实现的栈可能造成一定的空间浪费==。
然而，由于==链表节点需要额外存储指针，因此链表节点占用的空间相对较大==。
综上，我们不能简单地确定哪种实现更加节省内存，需要针对具体情况进行分析。
### 栈的典型操作
- 浏览器中的后退与前进、软件中的撤销与反撤销。
- 程序内存管理。每次调用函数时，系统都会在栈顶添加一个栈帧，用于记录函数的上下文信息。在递归函数中，向下递推阶段会不断执行入栈操作，而向上回溯阶段则会不断执行出栈操作。
## 队列
前面我们学习了栈，栈中元素只能栈顶出入，它是一种特殊的线性数据结构，同样，队列（Queue）也是一种特殊的线性数据结构。
就像我们在超市结账过程中需要排队一样，总是排成一列，先到的人排在前面，后来的人排在后面，越前面的人越先完成任务，这就是队列，队列有队头和队尾：
![队列与入队出队操作示意](队列与入队出队操作示意.md)
秉承先来后到的原则，队列中的元素只能从队尾进入，只能从队首出去，也就是说，入队顺序是 1、2、3、4，那么出队的顺序也一定是 1、2、3、4，所以队列是一种先进先出（FIFO，First in First out）的数据结构。
#### 基于链表实现队列
可以将链表的 ”头节点“ 和 “尾节点” 分别视为 ”队首“ 和 ”队尾“，规定只有队尾可以添加节点，队首只可以删除节点。
队列也可以使用链表来实现，代码如下：
```java
public class LinkedQueue<E> {  
    private Node<E> head = new Node<E>(null);  
    private class Node<E>{  
        E element;  
        Node<E> next;  
        public Node(E element){  
            this.element = element;  
        }  
    }  
  
    /**  
     * enqueue 入队操作，在队尾操作  
     * @param element  
     */  
    public void enqueue(E element){  
        Node<E> tail = head;  
        while(tail.next != null){  
            tail = tail.next;  
        }  
        tail.next = new Node<>(element);  
    }  
  
    /**  
     * dequeue 出队操作，在队首操作  
     * @return  
     */    
     public E dequeue(){  
        if(isEmpty()){  
            throw new NoSuchElementException("队列为空");  
        }  
        E element = head.next.element;  
        head.next = head.next.next;  
        return element;  
    }  
  
    /**  
     * 获取队首元素  
     * @return  
     */    
     public E peak(){  
        if(isEmpty()){  
            throw new NoSuchElementException("队列为空");  
        }  
        return head.next.element;  
    }  
  
    /**  
     * 判断队列是否为空  
     * @return  
     */    
     public boolean isEmpty(){  
        return head.next == null;  
    }  
}
```

# 列表
**列表（list）是一个抽象的数据结构概念，表示元素的有序集合，支持元素访问、修改、添加、删除和遍历等操作，无须使用这考虑容量限制的问题。列表可以基于链表或数组实现。**
- 链表天然可以看作一个列表，支持元素的增删改查功能，并且可以灵活扩容。
- 数组也支持元素增删改查，但是由于其长度不可变，因此只能看作一个长度受限制的列表。
## 列表常用操作
### 初始化列表
我们通常使用“**无初始值**”和“**有初始值**”这两种初始化方法：
```java
// 无初始值初始化列表  
List<Integer> ls1 = new ArrayList<>();  
  
// 有初始值初始化列表  
Integer[] intArray = new Integer[] {1,2,3,4,5};  
List<Integer> ls2 = new ArrayList<>(Arrays.asList(intArray));
```

### 访问元素
列表本质上是数组，因此可以在 𝑂(1) 时间内访问和更新元素，效率很高。
```java
// 访问元素  
int num = ls2.get(1); // 访问索引 1 处的元素，列表也从下标 0 开始计数  
  
// 更新元素  
ls2.set(1, 9);
```

### 插入与删除元素
相较于数组，列表可以自由地添加与删除元素。在列表尾部添加元素的时间复杂度为 O(1)，但插入和删除元素的效率仍然和数组相同，时间复杂度为 O(n)。
```java
// 插入与删除元素  
// 清空列表  
ls2.clear();  
  
// 在尾部添加元素  
ls2.add(5);  
ls2.add(4);  
ls2.add(3);  
ls2.add(2);  
ls2.add(1);  
ls2.add(0,-1); // 在索引 0 的位置，插入数字 -1  
// 删除元素  
// 删除索引 5 的元素  
ls2.remove(5);
```
### 遍历列表
与数组一样，列表可以**根据索引遍历，也可以直接遍历各元素**。
```java
// 通过索引遍历列表  
int count = 0;  
for(int i = 0; i < ls2.size(); i++){  
    count += ls2.get(i);  
}  
// 直接遍历列表元素  
for(int number: ls2){  
    count += number;  
}
```

### 拼接列表
给定一个新列表 nums1，我们可以将其拼接到原列表的尾部。

### 排序列表

## 列表实现
```java
  
/**  
 * 实现一个简易版列表，包含下面三个重点设计  
 *  - 初始容量：选取一个合适的数组的初始容量。在本例中，选择 10  
 *  - 数量记录：声明一个变量 size，用于记录当前元素数量，并随着元素插入和删除实时更新。  
 *  - 扩容操作：若插入元素时列表容量已满，则需要进行扩容。  
 */  
public class MyList {  
  
    // 数组（存储列表元素）  
    private int[] arr;  
    // 列表容量  
    private int capacity =10;  
    // 列表长度（当前元素数量）  
    private int size = 0;  
    // 每次列表扩容的倍数  
    private int extendRatio = 2;  
  
    // 构造方法  
    public MyList() {  
        arr = new int[capacity];  
    }  
    // 获取列表元素个数  
    public int size(){  
        return size;  
    }  
    // 获取列表容量  
    public int capacity(){  
        return capacity;  
    }  
    // 访问 index 下标处的元素  
    public int get(int index){  
        // 索引越界，则抛出异常  
        if(index < 0 || index >= size){  
            throw new IndexOutOfBoundsException("索引越界");  
        }  
        return arr[index];  
    }  
    // 更新元素  
    public void set(int index, int num){  
        if(index < 0 || index >= size){  
            throw new IndexOutOfBoundsException("索引越界");  
        }  
        arr[index] = num;  
    }  
    // 在尾部添加元素  
    public void add(int num){  
        // 如果元素数量达到列表容量，扩容。  
        if(size == capacity){  
            extendCapacity();  
        }  
        arr[size] = num;  
        // 更新元素数量  
        size++;  
    }  
    public void insert(int index,int num){  
        if(index < 0 || index >= size){  
            throw new IndexOutOfBoundsException("索引越界");  
        }  
        // 元素数量超过容量时，触发扩容机制  
        if(index == size){  
            extendCapacity();  
        }  
        // 将索引 index 以及以后的元素都向后移动一位  
        for(int j = size; j >= index; j--){  
            arr[j+1] = arr[j];  
        }  
        arr[index] = num;  
        // 更新元素数量  
        size++;  
    }  
    public int remove(int index){  
        if(index < 0 || index >= size){  
            throw new IndexOutOfBoundsException("索引越界");  
        }  
        int num = arr[index];  
        // 将 index 索引之前的元素都向前移动一位  
        for(int i = index; i < size - 1; i++){  
            arr[i] = arr[i + 1];  
        }  
        // 更新元素数量  
        size--;  
        // 返回被删除的元素  
        return num;  
    }  
    // 列表扩容操作  
    public void extendCapacity(){  
        // 新建一个长度为原数组 extendRatio 倍的新数组，并将原数组复制到新数组  
        arr = Arrays.copyOf(arr, capacity() * extendRatio);  
        // 更新列表容量  
        capacity = arr.length;  
    }  
    public int[] toArray(){  
        int size = this.size();  
        // 仅转换有效长度范围内的列表元素  
        int[] arr = new int[size];  
        for (int i = 0; i < size; i++) {  
            arr[i] = this.get(i);  
        }  
        return arr;  
    }  
}
```
# 哈希表
通过建立 key 与值 Value 之间的映射
# 树
树是一种全新的数据结构，它就像一棵树的树枝一样，不断延伸：

在我们的程序中，想要表达出一棵树，可以像下面这样连接：
![树形数据结构示意](树形数据结构示意)

- 一般称位于最上方的结点为树的根结点（Root）因为整棵树是从这里开始延伸出去的。
- 每个结点连接的子结点数目（分支的数目）我们称为**结点的度**（Degree）而每个结点度的最大值称为树的度。
- 每个结点延伸下去的下一个结点都可以称为一颗子树（SubTree）
- 每个**结点的层次**按照从上往下的顺序，树的根结点为 1，每向下一层+1。整棵树的最大层次，就是这颗**树的深度**（Depth）。比如 G 的层次就是 3，整棵树中所有结点的最大层次

由于整颗树错综复杂，所以需要先规定一下结点之间的称呼：
- 与当前结点直接向下相连的结点，称为子结点（Child），比如 B、C、D 结点，都是 A 的子结点，就像族谱中的父子关系一样，相反的，A 就是 B、C、D 的父结点。
- 如果某个结点没有任何的子结点（也就是结点的度为 0 的时候）称这种结点为**叶子结点**，比如 K、L、F、G、M、I、J，都是叶子结点。
- 如果两个结点的父结点是同一个，那么称这两个结点为**兄弟结点**（Sibling）比如 B 和 C 就是兄弟结点，因为都是 A 结点的子结点。

本章需要着重讨论的是**二叉树**（Binary Tree），这是一种特殊的树，度最大只能为 2，也就是任意一个结点最多只能有 2 个子结点，所以我们称其为二叉树。

并且二叉树任何结点的子树是有左右之分的，不能颠倒顺序。

当然，对于某些特殊的二叉树有特别的称呼，比如，某一颗二叉树，所有分支结点都存在左子树和右子树，且子结点都在同一层：
![满二叉树](满二叉树.md)
这样的二叉树我们称为满二叉树，可以看到整颗树都是很饱满的，没有出现任何度为 1 的结点，当然，还有一种特殊情况：
![完全二叉树](完全二叉树.md)
可以看到只有最后一层有空缺，并且**所有的叶子结点都是按照从左往右的顺序排列的**，这样的二叉树称为**完全二叉树**，所以，一颗满二叉树，一定是一颗完全二叉树。
## 二叉树的程序表示
我们接着来看二叉树在程序中的表示形式，我们在前面使用链表的时候，每个结点不仅存放对应的数据，而且会存放一个指向下一个结点的引用：
![](链表示意图.md)
而二叉树也可以使用这样的链式存储形式，只不过现在一个结点需要存放一个指向左子树的引用和一个指向右子树的引用：
![二叉树的程序表示形式](二叉树的程序表示形式.md)

### 树的结点定义
```java
/**  
 * 存放二叉树里面的结点  
 * @param <E>  
 */  
public class TreeNode<E> {  
    private E element;  
  
    /**  
     * 指向左右指针的引用  
     */  
    public TreeNode<E> left;  
    public TreeNode<E> right;  
  
    public TreeNode(E element) {  
        this.element = element;  
    }  
    public String toString(){  
        return element.toString();  
    }  
}
```

### 构造二叉树
比如，我们现在想要构造一颗二叉树：
![完全二叉树](完全二叉树.md)

代码表示如下：
```java
public class Test {  
    public static void main(String[] args) {  
        TreeNode<Character> a = new TreeNode<>('A');  
        TreeNode<Character> b = new TreeNode<>('B');  
        TreeNode<Character> c = new TreeNode<>('C');  
        TreeNode<Character> d = new TreeNode<>('D');  
        TreeNode<Character> e = new TreeNode<>('E');  
        TreeNode<Character> f = new TreeNode<>('F');  
  
        // 构造二叉树的结构  
        a.left = b;  
        a.right = c;  
        b.left = d;  
        b.right = e;  
        c.left = f;  
  
        //如果想要访问 D,就是 a 的左子树的左子树  
        System.out.println(a.left.left);  
    }  
}
```
这样，我们通过链式结构，就构造出了二叉树的结构。
### 二叉树的退化
当二叉树的每层结点都被填满的时候，达到“完美二叉树”；而当所有结点都偏向一侧的时候，二叉树退化为“链表”。
- 完美二叉树是理想情况，可以充分发挥二叉树 “分治” 的优势。
- 链表则是另一个极端，各项操作都变为线性操作，时间复杂度变为 O(n)。
## 二叉树的遍历
接着我们来看如何遍历一颗二叉树，也就是访问二叉树的每一个结点，由于树形结构特殊，遍历顺序并不唯一，所以一共有四种访问方式：**前序遍历、中序遍历、后序遍历、层次遍历**。
### 前序遍历
![二叉树的前序遍历](二叉树的前序遍历.md)
前序遍历是一种勇往直前的态度，走到哪里就遍历到哪里，先走到左边再走右边，比如上图，就先从根结点开始，从 A 开始，先左后右，那么下一个就是 B，从 B 开始，先左后右下一个就是 D，由于 D 没有子结点，所以下一个就是 E...... 所以上面这个二叉树的前序遍历结果就是：ABDECF。

**遍历过程**
1. 打印根结点
2. 前序遍历左子树
3. 前序遍历右子树

代码实现：
```java
/**  
 * 二叉树的前序遍历静态泛型方法  
 * @param root 二叉树的根结点  
 * @param <T>  
 */  
public static <T> void preOrder(TreeNode<T> root){  
    if(root == null){ return;}  
    System.out.print(root.toString() + " ");  
    preOrder(root.left);  
    preOrder(root.right);  
}
```

测试：
```java
... // 构造二叉树结构

// 测试前序遍历  
preOrder(a); // A B D E C F
```
### 中序遍历
前序遍历了解完以后，接着就是中序遍历了，中序遍历在顺序上与前序遍历不同，前序遍历是遍历到哪里就打印到哪里，而中序遍历需要先完成整个左子树的遍历然后再打印，再遍历右子树。

这里还是以上面的二叉树为例：
![二叉树的中序遍历](二叉树的中序遍历.md)

**遍历过程：**
1. 遍历左子树
2. 打印根结点
3. 遍历右子树

代码实现：
```java
/**  
 * 中序遍历方法  
 * @param root  
 * @param <T>  
 */  
public static <T> void inOrder(TreeNode<T> root){  
    if(root == null){ return;}  
    inOrder(root.left);  
    System.out.print(root.toString() + " ");  
    inOrder(root.right);  
}
```

测试：
```java
// 测试中序遍历  
inOrder(a); // D B E A C F
```

### 后序遍历

接着是后序遍历，后序遍历继续将打印时机延后，需要等待左右子树全部遍历完成以后，才会进行打印：
![二叉树的后序遍历](二叉树的后序遍历.md)

**遍历过程：**
1. 遍历左子树
2. 遍历右子树
3. 打印根结点

代码实现：
```java
/**  
 * 后序遍历方法  
 * @param root  
 * @param <T>  
 */  
public static <T> void postOrder(TreeNode<T> root){  
    if(root == null){ return;}  
    postOrder(root.left);  
    postOrder(root.right);  
    System.out.print(root.toString() + " ");  
}
```
测试：
```java
// 测试后序遍历  
postOrder(a); // D E B F C A
```
### 层次遍历
最后再来看层次遍历，实际上这种遍历方式才是我们人脑最容易理解的，它是按照每一层来遍历的：
![二叉树的层次遍历](二叉树的层次遍历.md)
层次遍历实际上就是按照从上往下每一层，从左到右的顺序打印每个结点，比如上面这颗二叉树，层次遍历的结果就是：A B C D E F。像这样一层一层挨个输出。程序遍历本质上属于广度优先遍历（BFT）

但是这样的遍历方式编程实现起来却比较复杂。可以利用**队列**来实现层次遍历，首先将根结点存入队列中，接着循环执行以下步骤：
- **执行出队操作，得到一个结点，打印结点的值**。
- **将此节点的左右孩子结点依次入队**。

代码实现：
```java
public static <T> void levelOrder(TreeNode<T> root){  
    if(root == null){ return;}  
    Queue<TreeNode<T>> queue = new LinkedList<>();  
    queue.add(root);  
    while(!queue.isEmpty()){  
        TreeNode<T> node = queue.poll();  
        System.out.print(node.toString() + " ");  
        if(node.left != null){  
            queue.add(node.left);  
        }  
        if(node.right != null){  
            queue.add(node.right);  
        }  
    }
```

复杂度分析： 
- 时间复杂度：所有结点都被访问一次，时间复杂度为 O(n)，其中 n 是二叉树中结点的个数。
- 空间复杂度：最差的情况下，遍历到最后一个叶子结点之前，队列中最多同时存在 $(n+1)/2$ 个结点，占用 O(n) 的空间。


## 树的深搜与广搜
### 深度优先搜索
深度优先搜索算法（DFS），是一种用于遍历搜索树或者图的算法，其过程要求对于每一个可能的分支路径深入到不能再深入为止。

### 广度优先搜索
## 二叉搜索树 BST
对于一颗树，如果满足下面两个条件，就称这棵树为二叉搜索树：
1. 对于根结点，左子树中所有结点的值 < 根结点值 < 右子树中所有结点的值。
2. 任意结点的左、右子树也是二叉搜索树，即同样满足条件 1。
### 二叉搜索树的操作
将二叉搜索树封装为一个类 `BinarySearchTree` ，并声明一个成员变量 `root`，指向树的根结点。
#### 查找结点
给定目标节点值 num ，可以根据二叉搜索树的性质来查找。如图 所示，我们声明一个节点 cur ，从二叉树的根节点 root 出发，循环比较节点值 cur.val 和 num 之间的大小关系。

- 若 `cur.val < num` ，说明目标节点在 cur 的右子树中，因此执行 cur = cur.right 。
- 若 `cur.val > num` ，说明目标节点在 cur 的左子树中，因此执行 cur = cur.left 。
- 若 `cur.val = num` ，说明找到目标节点，跳出循环并返回该节点。

具体算法实现可见算法刷题记录篇：[[Leetcode 刷题#700. [二叉搜索树中的搜索](https //leetcode.cn/problems/search-in-a-binary-search-tree/description/)|二叉搜索树中的搜索]]

二叉搜索树的搜索操作其实和二叉查找算法的工作原理一致，每次都是排除一半的情况。搜索过程中循环次数最多就是二叉树的高度，当二叉树平衡的时候，时间复杂度为 `O(log n)`。
#### 插入结点
给定一个待插入元素，为了保持二叉搜索树 “左子树<根结点<右子树”的性质，插入操作流程如下所示：
1. **查找插入位置**：与查找操作类似，从根结点出发，根据当前结点值和 num 的大小关系循环向下搜索，直到越过叶子结点（遍历至null）以后跳出循环。
2. **在该位置插入结点**：初始化结点，让后将该结点置于前面一步查找到的位置。

具体算法实现可见算法刷题记录篇：[[Leetcode 刷题#701. [二叉搜索树中的插入操作](https //leetcode.cn/problems/insert-into-a-binary-search-tree/description/)|二叉搜索树中的插入操作]]

在代码实现过程中，需要注意以下两点：
- **二叉搜索树不允许出现重复结点**，否则将会违反其定义。所以如果在查找插入位置的时候遇到和待插入元素值相同的结点，不执行插入操作，直接返回。
- **为了实现插入结点，需要借助结点 pre 保存上一轮循环的结点**。这样在遍历到 None 的时候，可以获取到其父节点，从而完成结点插入操作。
#### 删除结点【难点！】
首先在二叉搜索树中找到目标结点，再将其删除。与插入操作类似，需要在删除操作完成后，二叉搜索树的性质仍然满足。因此，根据目标结点的子结点数量，分为0、1、2三种情况，执行对应的删除结点操作。
- 当待删除结点的度为 0 的时候，表示该结点是叶结点，可以直接删除。
- 当待删除结点的度为 1 的时候，将待删除的结点替换为其子结点即可。
- 当待删除结点的度为 2 的时候，我们无法直接删除它，而需要使用一个结点替换这个结点。由于要保持二叉搜索树的性质，因此这个结点可以是右子树的最小结点或者左子树的最大值。
### 二叉搜索树的应用
- 用作系统中的多级索引，实现高效的查找、插入、删除操作。
- 作为某些搜索算法的底层数据结构。
- 用于存储数据流，以保持其有序状态。

## 平衡二叉树 - AVL 树
改进了二叉搜索树添加结点的过程中可能出现左右子树长度不一致导致的二叉搜索树查询结点效率过低的问题。
特点：任意节点左右子树的高度差不超过 1。
### 平衡二叉树的旋转
如何旋转平衡二叉树，保持平衡二叉树的平衡。步骤如下：
1. 确定支点：从添加的节点开始，不断的往父节点找不平衡的节点。

#### 左旋
1. 以不平衡的点作为支点。
2. 把支点向左旋转降级，变成左子节点。
3. 晋升原来的右子节点。

另一种情况：
1. 以不平衡的点作为支点
2. 将根节点的右侧往左拉
3. 原先的右子节点变成新的父节点，并把多余的左子节点出让，给已经降级的根节点当右子节点。
#### 右旋
1. 以不平衡的点作为支点
2. 把支点向右旋转降级，变为右子节点。
3. 晋升原来的左子节点。
![[平衡二叉树右旋的情况 1]]

另一种情况：
1. 以不平衡的点作为支点
2. 把根节点的左侧往右拉
3. 原先的左子节点变成新的父节点，并把多余的右子节点让出，给已经降级的根节点当左子节点。

![[平衡二叉树右旋的情况 2]]
### 平衡二叉树需要旋转的四种情况
1. 左左：当根节点左子树的左子树有节点插入，导致二叉树不平衡。只需要一次右旋就能达到平衡。
2. 左右：当根节点左子树的右子树有节点插入，导致二叉树不平衡。一次右旋还不能达到平衡，首先需要局部左旋，然后整体右旋。
	 ![[平衡二叉树左右需旋转两次的情况]]
3. 右右：当根节点右子树的右子树有节点插入，导致二叉树不平衡。只需要一次左旋就能达到平衡。
	![[平衡二叉树右右需要旋转一次的情况]]
4. 右左：当根节点右子树的左子树有节点插入，导致二叉树不平衡。需要局部右旋，然后整体左旋。
	![[平衡二叉树右左需要旋转两次的情况]]
## 红黑树
- 红黑树是一种自平衡的二叉查找树，是一种数据结构。
- 是一种特殊的二叉查找树，红黑树的每一个结点上都有表示结点颜色的属性。
- 每一个节点可以是红或者黑；红黑树**不是高度平衡**的，它的**平衡通过“红黑规则” 进行实现**。
### 红黑树与平衡二叉树的区别
平衡二叉树：高度平衡 & 当左右子树高度差超过 1 时，通过旋转保持平衡。
红黑树：二叉查找树 & 但是高度不平衡 & 条件：特有的红黑规则。

### 红黑规则
1. 每一个结点或者是红色，或者是黑色的。
2. 根节点必须是黑色的。
3. 如果一个结点没有子结点或者父节点，则该结点指针属性值为 Nil，这些 Nil 视为叶节点，每个叶节点是黑色的。
4. 如果某个结点是红色的，那么它的子结点必须是黑色的。
5. 对每一个结点，从该结点到其所有后代节点的简单路径上，均包含相同数目的黑色结点。

### 红黑树添加节点的规则
添加节点默认是红色的，因为效率高。

# 字典树
