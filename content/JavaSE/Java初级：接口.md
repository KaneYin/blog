接口比抽象类更加抽象，只代表某个确切的功能。也就是只能包含方法的定义，甚至不是一个类。
接口一般只代表某些功能的抽象，接口包含了一些方法的定义，类可以实现这个接口，表示类支持接口代表的功能。

实际上，接口的目标就是将类所具有的某些行为抽象出来。

在实际编码过程中，由于接口内只能编写公共的抽象方法，所以定义方法的时候可以省去 `public abstract` 的关键字。


[[在JavaSE中，继承类和实现接口的关系]]


比如：
```java
public class Person {  
    public String name;  
    public int age;  
  
    public Person(){  
    }  
    public Person(String name, int age){  
        this.name = name;  
        this.age = age;  
    }  
}
```

```java

public class Student extends Person implements study {  
    public Student(){}  
    public Student(String name,int age){  
        super(name,age);  
    }  
    public void study(){  
        System.out.println("作为一名学生，我正在学习");  
    }  
}
```

```java
public class Teacher extends Person implements study{  
    public Teacher(){};  
    public Teacher(String name,int age){  
        super(name,age);  
    }  
    public void study(){  
        System.out.println("作为一名老师，我正在学习");  
    }  
}
```

**接口的定义如下：**
```java
package Intereface;  
  
public interface study {  
    void study();  
}
```

```java
  
public class InterfaceTest {  
    public static void main(String[] args) {  
        Student s1 = new Student();  
        Teacher t1 = new Teacher();  
        s1.study();  
        t1.study();  
    }  
}
```

接口不同于继承，接口可以同时实现很多个。

```java
public class Student extends Person implements Study,A {

}
```

接口其实不是Java中的多继承，而是相当于一个类的功能列表，作为附加功能存在，一个类可以附加很多个功能，只能是多继承的一种替代方案。

接口就和抽象类一样，不能直接创建对象，但是可以将接口实现的类的对象以接口的形式去使用：
```java

public class InterfaceTest {  
    public static void main(String[] args) {  
        study study = new Student();  
        study.study(); //作为一名学生，我正在学习  
    }  
}
```
当做接口使用的时候，只有接口中定义的方法和Object类的方法，无法使用类本身的方法和父类的方法。

接口同样支持向下转型：
```java
public static void main(String[] args){
	Study study = new Teacher();
	if(study instanceof Teacher){
		Teacher teacher = (Teacher) study;
		teacher.study();
	}
}
```

从Java8开始，接口中可以使用`default` 关键字提供默认实现。如果实现接口的类不实现接口提供的方法，那么调用方法的时候将会调用默认实现的方法。

但是如果类对默认实现的方法进行了重写，并且在重写的方法体中需要调用接口里面的方法，需要使用这样的语法规则：
`接口名.super.默认实现的方法名();`

并且，重写的方法名前面需要加上 `@override` 注解

接口不同于类，接口中**不允许**存在**成员变量和成员方法**，但是可以存在静态变量和静态方法，在接口中定义的变量只能是：

```java
public interface study {  
    // 接口中定义的变量只能是 public static final 的  
    static final String NAME = "Zhang san";  
  
    //接口中定义的方法只能是 public static 的  
    public static void test(){  
        System.out.println(NAME);  
    }  
  
    // 这是接口提供的方法的默认实现  
    default void sayHello() {  
        System.out.println(NAME);  
    }  
      
    // 这是一般的接口中的方法  
    void study();  
}
```

接口是可以继承其他接口的：


接口可以继承自多个接口，也就是可以实现多继承：


如果子接口出现了和父接口相同定义的方法，那么这个方法只是对父接口中的方法的覆盖：
