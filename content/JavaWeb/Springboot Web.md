# Springboot Web 示例程序
需求：使用 SpringBoot 框架开发一个 Web 应用，浏览器发起 /hello 后，给浏览器返回字符串 “Hello World”
**开发步骤**
1. 创建 springboot 工程，并且勾选 Web 开发相关依赖。![[Springboot 项目搭建.png]]
2. 定义 HelloController 类，添加方法 hello，并添加注解。
```java
@RestController  
public class HelloController {  
    @RequestMapping("/hello")  
    public String hello(){  
        System.out.println("hello world !");  
        return "hello world !";  
    }  
}
```
3. 运行测试![[Pasted image 20250614184452.png]]
同时，IDEA 控制台也会输出 “hello world  !” 内容。
# HTTP 协议
- 一种超文本传输协议，规定了浏览器与服务器之间数据传输的规则。
- 特点：
	- 基于 TCP 协议：面向连接的安全协议
	- 基于请求-响应模型的：一次请求对应一次响应
	- HTTP 协议是无状态的协议：对于事务处理没有记忆能力。每次请求-响应都是独立的。
		- 缺点：多次请求之间不能共享数据。
		- 优点：速度快。
## HTTP 请求协议
也就是请求数据的格式。由三部分组成：
- 请求行。请求数据格式的第一行（包含请求方式、资源路径、协议）。
- 请求头。格式 key：value。

常见请求头代表的含义：

|      Host       |               请求的主机名                |
| :-------------: | :---------------------------------: |
|   User-Agent    | 浏览器版本，例如 Chrome 浏览器的标识类似 Mozila/5.0 |
|     Accept      |           标识浏览器能够接收的资源类型            |
| Accept-Language |     表示浏览器偏好的语言，服务器可以据此返回不同语言的网页     |
| Accept-Encoding |           表示浏览器可以支持的压缩类型            |
|  Content-Type   |              请求主体的数据类型              |
| Content-Length  |           请求主体的大小（单位：字节）            |
比如，Springboot 入门程序中浏览器的请求数据：
![[HTTP 响应数据格式]]
- 请求体（不一定有）：POST 请求，存放请求参数。请求体和请求头之间存在空行分隔。
 
### GET 请求和 POST 请求的区别
- GET 请求：请求参数在请求行中，没有请求体。如 /brand/findAll? name=oppo&tatus=1。GET 请求大小是有限制的。
- POST 请求：请求参数在请求体中，POST 请求大小是没有限制的。

这里用一个 HTML 表单页面展示 GET 请求和 POST 请求之间的区别：
```HTML
<body>  
    <form action="" method="get">  
        姓名：<input type="text" name="name"><br>  
        密码：<input type="password" name="password"><br>  
        <input type="submit" value="提交表单GET"><br>  
    </form>    <br><br><br>    <form action="" method="post">  
        姓名：<input type="text" name="name"><br>  
        密码：<input type="password" name="password"><br>  
        <input type="submit" value="提交表单POST"><br>  
    </form></body>
```
![[HTTP GET 请求.png]]
> 可以看到，通过 GET 请求提交数据的时候，请求路径之后通过 `?key=value & key=value` 的形式将表单数据进行提交，这部分数据最终的提现形式就是在请求行中体现出来的。

![[HTTP POST 请求.png]]
> POST 请求提交 Form 表单的时候，请求参数不会体现在请求路径中，而是体现在请求体中。Chrome 浏览器查看请求体的时候，要在 ”Payload“ 模块下面查找。
## HTTP 响应格式
响应数据的格式和请求数据格式非常相似，主要由以下几部分组成：
- 响应行：响应数据的第一行（协议、状态码、描述）
- 响应头：从第二行开始，格式`key=value`
- 响应体：最后一部分，存放响应数据。和响应头之间使用空行隔开。

### 响应状态码

| 状态码 | 含义                                                 |
| --- | -------------------------------------------------- |
| 1xx | **响应中**，临时状态码，表示请求已经接收，告诉客户端应该继续请求或者它已经完成则忽略它      |
| 2xx | **成功**-表示请求已经被成功接收，处理已经完成。                         |
| 3xx | **重定向**-重定向到其他地方；让客户端再发起一次请求以完成整个处理。               |
| 4xx | **客户端错误**-处理发生错误，责任在客户端。如：请求了不存在的资源、客户端未被授权、禁止访问等。 |
| 5xx | **服务器错误**-处理发生错误，责任在服务端。如：程序抛出异常。                  |

- [ ] 重定向的定义以及图解
- [ ] 常见的响应状态码
### 常见响应头

| key              | 含义                                        |
| ---------------- | ----------------------------------------- |
| Content-Type     | 表示该响应内容的类型，例如 text/html, application/json |
| Content-Length   | 表示该响应内容的长度（字节数）                           |
| Content-Encoding | 表示该响应压缩算法，例如 gzip                         |
| Cache-Control    | 指示客户端应该如何缓存，例如 max-age=300 表示最多缓存 300 秒   |
| Set-Cookie       | 告诉浏览器为当前页面所在的域设置 cookie                   |
## HTTP 协议解析
# Tomcat 服务器
- Web 服务器是一个软件程序，对 HTTP 协议的操作进行封装，使得程序员不必直接对协议进行操作，让 Web 开发更加便捷。主要功能是 ”提供网上信息浏览服务“。
- 是一个开源免费的轻量级 Web 服务器，支持 Servlet/JSP 少量 JavaEE 规范。
- JavaEE：Java 企业版。指 Java 企业级开发技术规范的总和。包含 13 项技术规范：JDBC、JNDI、EJB、RMI、JSP、Servlet、XML、JMS、Java IDL、JTS、JTA、JavaMail、JAF。
- Tomcat 也被称为 Web 容器，Servlet 容器。Servlet 程序需要依赖于 Tomcat 才能运行。
## 基本使用
1. 下载。
2. 安装。
3. 卸载。
4. 启动。
5. 关闭。
# 请求响应详解

## 请求
### 接口测试工具 Postman
当前最主流的开发模式：前后端分离。在这种开发模式下，后端程序员并不知道前端页面样式，根据接口文档编写的后端程序如果需要测试则需要打开浏览器测试，在测试 POST 请求的时候甚至需要自己编写一个简单前端页面发送 POST 请求，这对于后端程序员开发是很不方便的。所以我们需要使用 Postman 接口测试工具。
Postman 是一款功能强大的网页调试与发送网页 HTTP 请求的工具。
作用：常用于进行接口测试。
![[Postman 进行接口测试示例]]
### 简单参数的接收
- 原始方式：在原始的 Web 程序中，获取请求参数，需要通过 HttpServletRequest 对象手动获取。
```java
// 原始方式  
// 缺点：比较繁琐，手动进行类型转换  
@RequestMapping("/simpleParam")  
public String simpleParam(HttpServletRequest request) {  
    // 获取请求参数  
    String name = request.getParameter("name");  
    String ageStr = request.getParameter("age");  
  
    int age = Integer.parseInt(ageStr);  
    System.out.println(name + ":" + age);  
    return "ok";  
}
```
- Springboot 方式：==参数名与形参变量名相同，定义形参即可接收参数==。
	- 如果参数对应不上，服务端接收不到参数，但是不会报错。这个时候可以使用 @RequestParam 完成映射。
	- 该注解的 required 属性默认是 true，代表请求参数必须传递。
```java
// Springboot 方式传递简单参数，相比之下代码量小很多。  
@RequestMapping("/simpleParamSpringboot")  
public String simpleParam2(String name, Integer age) {  
    System.out.println(name + ":" + age);  
    return "ok";  
}
```
![[简单参数的传递]]
### 实体参数
- 简单实体对象：请求参数名与形参对象属性名相同，定义 POJO 接收即可。
```java
// 2. 使用实体参数接收请求  
@RequestMapping("/simplePojo")  
public String simplePojo(User user){  
    System.out.println(user);  
    return "ok";  
}
```
- 复杂实体对象：**请求参数名与形参对象属性名相同，按照对象层次结构关系可接收嵌套 Pojo 属性参数**。 
```java
// 3. 使用复杂实体参数接收请求  
@RequestMapping("/complexPojo")  
public String complexPojo(Admin admin){  
    System.out.println(admin);  
    return "ok";  
}
```
![[复杂实体对象的传递]]
### 数组集合参数
- 数组参数：请求参数名与形参数组名称相同且请求参数为多个，定义数组类型形参即可接收参数。
```java
@RequestMapping("/arrayParam")  
public String arrayParam(String[] hobby){  
    System.out.println(Arrays.toString(hobby));  
    return "ok";  
}
```
- 集合参数：请求参数名与形参集合名称相同且请求参数为多个，@RequestParam 绑定参数关系。
```java
// 4.1 使用集合参数接收请求  
@RequestMapping("/listParam")  
public String listParam(@RequestParam ArrayList<String> hobby){  
    System.out.println(hobby);  
    return "ok";  
}
```

### 日期参数
- 日期参数：使用 @DataTimeFormat 注解完成日期参数格式转换
```java
// 日期参数  
@RequestMapping("/dateParam")  
public String dateParam(@DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss") LocalDateTime updateTime){  
    System.out.println(updateTime);  
    return "ok";  
}
```
### Json 参数
- Json 参数：Json 数据键名和形参对象属性名相同，定义 Pojo 类型形参即可接收参数，需要使用 @RequestBody 标识。
```java
// 6. JSON 参数  
@RequestMapping("/jsonParam")
// 需要通过 @RequestBody 注解将 JSON 格式的数据封装到实体类中，并且需要保证 JSON 数据中的键名和实体类中的属性名保持一致，就能自动封装成功。
public String jsonParam(@RequestBody User user){  
    System.out.println(user);  
    return "ok";  
}
```
![[JSON 请求参数]]
### 路径参数
- 路径参数：通过请求 URL 直接传递参数，使用 {...} 来标识该路径参数，需要使用 @PathVariable 获取路径参数。
```java
// 7. 接收路径参数，然后绑定给方法形参  
@RequestMapping("/path/{id}")  
public String pathParam(@PathVariable Integer id){  
    System.out.println(id);  
    return "ok";  
}
```
![[请求路径参数]]
> 这里演示的是传递一个路径参数的情况，实际上可以传递多个路径参数。只需要在请求路径中使用 `/` 将请求参数分开，最后在 Controller 方法中接收第二个路径参数即可。


## 响应
### @ResponseBody 注解的作用
**@ResponseBody 注解：**
- 类型：方法注解、类注解
- 位置：Controller 方法上，类上
- 作用：将方法返回值直接响应，如果返回类型是 实体对象/集合，将会转换为 JSON 格式响应。
- 说明： @RestController=@Controller + @ResponseBody

```java
@RestController  
public class ResponseController {
	// 直接将字符串作为响应体的内容响应回来
    @RequestMapping("/responseString")  
    public String hello(){  
        return "hello";  
    }
    // 将 Json 数据作为响应体的内容响应
    @RequestMapping("/responsePojo")  
    public Address address(){  
        Address address = new Address();  
        address.setProvince("beijing");  
        address.setCity("beijing");  
        return address;  
    }
    // 将集合对象转换为 Json 格式的数组
    @RequestMapping("/responseList")  
    public List<Address> addressList(){  
        List<Address> addressList = new ArrayList<>();  
        Address address = new Address();  
        address.setProvince("beijing");  
        address.setCity("beijing");  
        addressList.add(address);  
  
        Address address1 = new Address();  
        address1.setProvince("hubei");  
        address1.setCity("wuhan");  
        addressList.add(address1);  
        return addressList;  
    }  
}
```


后端给前端返回的数据格式比较混乱，会增大前端解析数据的成本，所以在后端返回数据之前，一般都会使用一个类封装好需要返回的数据，从而统一返回数据的格式。
### 统一响应结果
```java
public class Result{
	
	private Integer code;
	private String msg;
	private Object data;
}
```
现在有了统一响应结果以后可以对上面的 Controller 方法进行改写：
```java
@RestController  
public class ResponseController {  
    @RequestMapping("/responseString")  
    public Result hello(){  
        return new Result(1,"success","hello world");  
    }  
    @RequestMapping("/responsePojo")  
    public Result address(){  
        Address address = new Address();  
        address.setProvince("beijing");  
        address.setCity("beijing");  
        return Result.success(address);  
    }  
    @RequestMapping("/responseList")  
    public Result addressList(){  
        List<Address> addressList = new ArrayList<>();  
        Address address = new Address();  
        address.setProvince("beijing");  
        address.setCity("beijing");  
        addressList.add(address);  
  
        Address address1 = new Address();  
        address1.setProvince("hubei");  
        address1.setCity("wuhan");  
        addressList.add(address1);  
        return Result.success(addressList);  
    }  
}
```
现在再使用 Postman 测试响应数据格式如下，响应数据相比没有封装返回结果的时候可解析性高了很多：
![[封装响应结果]]
### 案例
现在编写一个从 emp.xml 文件中获取员工数据，返回统一响应结果的 Demo，在页面渲染展示。具体步骤如下：
- 在 pom.xml 文件中引入 dom4j 依赖，用于解析 XML 文件。
- 引入解析 XML 的工具类 XML Parser Utils、对应的实体类 Emp、XML  文件 emp.xml
- 引入静态页面文件，放在 resources 下的 static 目录下
- 编写 Controller 文件，处理请求，响应数据。

> Springboot 项目的静态资源（html, css, js 等前端资源）默认存放目录为：classpath:/static, classpath:/public, classpath:/resources

```java  
@RestController  
public class EmpController {  
    @RequestMapping("/listEmp")  
    public Result list(){  
        // 1. 加载并解析 xml 文件  
        String file = this.getClass().getClassLoader().getResource("emp.xml").getFile();  
        List<Emp> empList = XmlParserUtils.parse(file, Emp.class);  
  
        // 2. 数据进行转换处理  
        empList.forEach(emp ->{  
            String gender = emp.getGender();  
            if("1".equals(gender)){  
                emp.setGender("男");  
            }else if("2".equals(gender)){  
                emp.setGender("女");  
            }  
            String job = emp.getJob();  
            if("1".equals(job)){  
                emp.setJob("讲师");  
            }else if("2".equals(job)){  
                emp.setJob("班主任");  
            }else if("3".equals(job)){  
                emp.setJob("就业指导");  
            }  
  
        });  
        // 3. 响应数据  
        return Result.success(empList);  
    }  
}
```

# 分层解耦
可以看到 Controller 中的代码比较混乱，因为既有数据访问部分的代码，也存在逻辑处理的代码，最后才是接收请求以及响应数据。但是在软件设计过程中，应该遵循单一职责原则，既每个接口或方法只完成一个功能。所以基于这个原则，Web 开发衍生出了三层架构。
## 三层架构
- Controller：控制层，接收前端发送的请求，对请求进行处理，并响应数据。
- Service：业务逻辑层，处理具体的业务逻辑。
- dao：数据访问层（又叫持久层），负责数据访问操作，包括数据的增、删、改、查。
将程序按照三层架构的思想进行升级：

## 分层解耦
- 内聚：软件中各个功能模块内部的功能联系。
- 耦合：衡量软件中各个层/模块之间的依赖，关联程度。
- 软件设计原则：高内聚、低耦合。

- 控制反转：IOC，对象的控制权由程序自身转移到外部（容器），这种思路称为控制反转
- 依赖注入：DI，容器为应用程序提供运行时所依赖的资源，称为依赖注入。
- Bean 对象：IOC 容器中创建、管理的对象。
### 控制反转 IOC 详解
Bean 的声明：

| 注解          | 说明               | 位置                             |
| ----------- | ---------------- | ------------------------------ |
| @Component  | 声明 bean 的基础注解    | 不属于以下三类的时候，使用此注解               |
| @Controller | @Component 的衍生注解 | 标注在控制器上                        |
| @Service    | @Component 的衍生注解 | 标注在业务类上                        |
| @Repository | @Component 的衍生注解 | 标注在数据访问类上（由于与 MyBatis 整合，用的很少） |
# Mybatis
Mybatis 是一款优秀的持久层（也就是 Dao 层）框架，用于简化 JDBC 的开发。
## 快速入门
### 快速入门程序
需求：使用 Mybatis 查询所有用户数据。
具体步骤如下：
1. 准备工作（创建 Springboot 工程，数据库表 User，实体类 User）
2. 引入 Mybatis 的相关依赖，配置 Mybatis
3. 编写 SQL 语句
### JDBC
Java Database Connectivity，就是使用 java 语言操作关系型数据库的一套 API。
**本质：**
- sun 公司官方定义的一套操作所有关系型数据库的规范，既接口。
- 各个数据库厂商实现这套接口，提供数据库驱动 jar 包。
- 我们可以使用这套接口编程，真正执行的是驱动 jar 包中的实现类。
![[JDBC 驱动与数据库服务器之间的关系]]
### 数据库连接池
- 数据库连接池是个容器，负责分配、管理数据库连接
- 它允许应用程序重复的使用一个现有的数据库连接，而不是重新建立一个
- 释放空闲时间超过最大空闲时间的连接，避免因为没有释放连接而引起的数据库连接遗漏
- 标准接口：Datasource
	-  官方提供的数据库连接池接口，由第三方组织实现此接口。
	- 功能：获取连接。`Connection getConnection() throws SQLException;`
- 数据库连接池产品
    - HikariCP
        - 目前性能最高的轻量级连接池，Spring Boot 默认集成。
    - Apache Commons DBCP
	    - Apache 老牌连接池，稳定但性能中等。

**如何切换不同的连接池，以 druid 连接池为例：[druid](https://github.com/alibaba/druid/wiki/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)
### Lombok
Lombok 是一个实用的 Java 类库，能通过注解的形式自动生成构造器，getter/setter, equals, hashcode, toString 等方法，并可以自动化生成日志变量，简化 java 开发、提高效率。

| 注解                         | 作用                                                                                                                          |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `@Getter/@Setter`          | 自动生成所有字段的 getter/setter 方法                                                                                                  |
| `@ToString`                | 生成 `toString()` 方法，包含所有字段（可排除特定字段）                                                                                          |
| `@EqualsAndHashCode`       | 生成 `equals()` 和 `hashCode()` 方法                                                                                             |
| `@NoArgsConstructor`       | 生成无参构造方法                                                                                                                    |
| `@AllArgsConstructor`      | 生成全参构造方法                                                                                                                    |
| `@RequiredArgsConstructor` | 生成包含 `final` 或 `@NonNull` 字段的构造方法                                                                                           |
| `@Data`                    | **复合注解** = `@Getter + @Setter + @ToString + @EqualsAndHashCode + @RequiredArgsConstructor` 需要注意的是，Data 注解不包括无参构造和全参构造的两个注解。 |
| `@Builder`                 | 生成链式构造器（建造者模式）                                                                                                              |
| `@Slf4j`                   | 自动注入日志对象（如 `private static final Logger log = ...`）                                                                         |
| `@Value`                   | 生成不可变类（所有字段为 `final`，只生成 getter）                                                                                            |
使用 Lombok 之前需要引入相关的依赖：
```xml
<dependency>  
    <groupId>org.projectlombok</groupId>  
    <artifactId>lombok</artifactId>  
    <version>1.18.38</version>  
</dependency>
```
注意：
Lombok 在编译时，会自动生成对应的 java 代码，我们在使用 Lombok 的时候，还需要安装一个 Lombok 的插件（IDEA 自带）。
## Mybatis 基础操作
### 准备工作
1. 准备数据库表 emp
2. 创建一个新的 springboot 工程，选择引入对应的起步依赖（mybatis, mysql 驱动, Lombok）
3. application.properties 中引入数据库连接信息
4. 创建对应的实体类 Emp
5. 准备 Mapper 接口 EmpMapper


### CRUD
#### 根据主键删除

**注意：**
如果 mapper 接口方法形参只有一个普通类型的参数，`#{...}` 里面的参数可以随便写，如：`#{id}, #{value}`。

#### 日志输出
可以在 application.properties 中，打开 mybatis 的日志，并指定输出到控制台。
```
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```
配置好日志信息以后，和没有配置前相比，控制台多了执行单元测试相关的 sql 语句：
```
==>  Preparing: delete from emp where id = ?
==> Parameters: 16(Integer)
<==    Updates: 0
```
上面控制台显示的 sql 语句就是一条**预编译 SQL** 。采用预编译 SQL 有以下优势：
- 性能更高。
- 更安全（防止 SQL 注入）。
	- SQL 注入是通过操作输入的数据来修改事先定义好的 SQL 语句，以达到执行代码对服务器进行攻击的方法。
#### 参数占位符
- `#{...}`
	- 执行 SQL 的时候，会将其替换为？，生成预编译 SQL，会自动设置参数值。
	- 使用时机：参数传递，都使用 `#{...}`
- `${...}`
	- 拼接 SQL。直接将参数拼接在 SQL 语句中，存在 SQL 注入问题。
	- 使用时机：如果对表名、列表进行动态设置的时候使用。
#### 新增员工

#### 查询员工

**Mybatis 数据封装**
- 实体类属性名和数据库表查询返回的字段名一致，Mybatis 会自动封装。
- 如果实体类属性名和数据库表查询返回的字段名不一致，不能自动封装。
下面介绍几种解决不能自动封装问题的办法：
1. 给数据库表中的字段取别名，让别名与实体类属性名一致，能够完成查询操作。
2. 手动结果映射：通过 @Result 及 @Results 进行手动结果映射。
3. 开启驼峰命名自动转换：如果字段名与属性名符合驼峰命名规范，Mybatis 会自动通过驼峰命名规则映射。
#### 查询员工（条件查询）


## XML 映射文件
- XML 映射文件的名称与 Mapper 接口名称一致，并且将 XML 映射文件和 Mapper 接口放置在相同的包下（同包同名）
- XML 映射文件的 namespace 属性与 Mapper 接口全限定名一致
- XML 映射文件中 sql 语句的 id 与 Mapper 接口中的方法名一致，并保持返回类型一致
![[Mybatis 中 XML 映射文件如何和 Mapper 接口对应]]
对应的代码如下：
```java
// Mapper 接口中的方法
// 条件查询  
//    @Select("select * from emp where name like '%${name}%' and gender = #{gender} and" +  
//            " entrydate between #{begin} and #{end} order by update_time desc")  
    public List<Emp> list(String name, Short gender, LocalDate begin, LocalDate end);
```
XML 映射文件：
```xml
<?xml version="1.0" encoding="UTF-8" ?>  
<!DOCTYPE mapper  
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"  
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">  
<mapper namespace="com.example.springbootwebmybatisapplication.mapper.EmpMapper">  
    <select id="list" resultType="com.example.springbootwebmybatisapplication.pojo.Emp">  
        select * from emp where name like '%${name}%' and gender = #{gender} and 
		entrydate between #{begin} and #{end} order by update_time desc
	</select>  
</mapper>
```
运行单元测试代码，传入参数如下：
```java
// 测试条件查询  
@Test  
public void testList(){  
    empMapper.list("张",(short) 1,LocalDate.of(2010,1,1),LocalDate.of(2020,1,1));
}
```
运行以后得到运行日志如下：
```
==>  Preparing: select * from emp where name like '%张%' and gender = ? and entrydate between ? and ? order by update_time desc
==> Parameters: 1(Short), 2010-01-01(LocalDate), 2020-01-01(LocalDate)
<==    Columns: id, username, password, name, gender, image, job, entrydate, dept_id, create_time, update_time
<==        Row: 2, zhangwuji, 123456, 张无忌, 1, 2.jpg, 2, 2015-01-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==      Total: 1
```
#### 比较使用注解操作 Mybatis 以及使用 XML 映射文件操作 Mybatis
使用注解奶映射简单语句会使代码更加简洁，但是对于稍微复杂一点的语句，Java 注解就显得力不从心，还会使本就复杂的 SQL 语句更加混乱不堪。因此，如果需要做一些复杂的操作，最好使用 XML 映射文件。
#### IDEA 插件 MybatisX 简化 Mybatis 开发


## Mybatis 动态 SQL
前面的条件查询语句，如果我只想要查询名字中包含”张“的员工，其他查询条件都为空，期望的查询结果应该是所有名字中包含”张“的员工信息，我们实际测试一下：
```java
// 单元测试
public void testList2(){  
    empMapper.list("张",null,null,null);  
}
```
但是测试的实际结果是：
```
==>  Preparing: select * from emp where name like '%张%' and gender = ? and entrydate between ? and ? order by update_time desc
==> Parameters: null, null, null
<==      Total: 0
```
说明对于写死的 Select 查询语句，如果其他参数不传递或者传递为空，无法进行判断。所以我们需要使用动态 SQL 进行判断：
动态 sql：随着用户的输入或者外部条件变化而变化的 SQL 语句，称为动态 sql。

### 条件判断标签
- `<if>`：用于判断条件是否成立。使用 test 属性进行条件判断，如果条件为 true，则拼接 SQL。test 属性中写条件判断语句。
使用 `<if>` 标签改造 XML 映射文件中的 SQL 语句：
```xml
<select id="list" resultType="com.example.springbootwebmybatisapplication.pojo.Emp">  
    select *  
    from emp
    where
		<if test="name != null">  
            name like '%${name}%'  
        </if>  
        <if test="gender != null">  
            and gender = #{gender}  
        </if>  
        <if test="begin != null and end != null">  
            and entrydate between #{begin} and #{end}  
        </if>  
    order by update_time desc  
</select>
```
然后再次执行单元测试方法，得到输出结果如下：
```
==>  Preparing: select * from emp where name like '%张%' order by update_time desc
==> Parameters: 
<==    Columns: id, username, password, name, gender, image, job, entrydate, dept_id, create_time, update_time
<==        Row: 2, zhangwuji, 123456, 张无忌, 1, 2.jpg, 2, 2015-01-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 14, zhangsanfeng, 123456, 张三丰, 1, 14.jpg, 2, 2002-08-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==      Total: 2
```
执行的 SQL 语句只拼接了姓名字段，符合预期结果。
但是这样改后的 SQL 语句还是有一点问题，比如在查询的时候只想要根据性别查询，是否能够成功查询呢？编写一个单元测试方法测试一下：
```java
@Test  
public void testList3(){  
    empMapper.list(null,(short)1,null,null);  
}
```
可以看到运行报错了，原因是，SQL 语法错误，因为在拼接 SQL 的过程中，如果第一个 name 不传递，第二个 gender 传递，就会导致多出了一个 and 关键字；同样如果传递的全部参数都为 null 也会报错，因为这时候会多出一个 where 关键字。

```
Preparing: select * from emp where and gender = ? order by update_time desc
==> Parameters: 1(Short)
Closing non transactional SqlSession [org.apache.ibatis.session.defaults.DefaultSqlSession@5927f904]

org.springframework.jdbc.BadSqlGrammarException: 
### Error querying database.  Cause: java.sql.SQLSyntaxErrorException: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'and gender = 1
```
解决办法就是使用一个 `<where>` 标签，能够自动判断是否存在多余的 and/or 关键字，以及 where 关键字是否多余：
```xml
<select id="list" resultType="com.example.springbootwebmybatisapplication.pojo.Emp">  
    select *  
    from emp    <where>  
        <if test="name != null">  
            name like '%${name}%'  
        </if>  
        <if test="gender != null">  
            and gender = #{gender}  
        </if>  
        <if test="begin != null and end != null">  
            and entrydate between #{begin} and #{end}  
        </if>  
    </where>>  
    order by update_time desc</select>
```
改造以后的 xml 映射文件如上，这时我们再运行测试方法，可以在控制台看到真确的日志输出：
```
==>  Preparing: select * from emp WHERE gender = ? order by update_time desc
==> Parameters: 1(Short)
<==    Columns: id, username, password, name, gender, image, job, entrydate, dept_id, create_time, update_time
<==        Row: 18, Tom, 123456, 汤姆, 1, 1.jpg, 1, 2002-01-01, 1, 2025-06-25 23:43:56, 2025-06-25 23:43:56
<==        Row: 1, jinyong, 123456, 金庸, 1, 1.jpg, 4, 2000-01-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 2, zhangwuji, 123456, 张无忌, 1, 2.jpg, 2, 2015-01-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 3, yangxiao, 123456, 杨逍, 1, 3.jpg, 2, 2008-05-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 4, weiyixiao, 123456, 韦一笑, 1, 4.jpg, 2, 2007-01-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 5, changyuchun, 123456, 常遇春, 1, 5.jpg, 2, 2012-12-05, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 11, luzhangke, 123456, 鹿杖客, 1, 11.jpg, 5, 2007-02-01, 3, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 12, hebiweng, 123456, 鹤笔翁, 1, 12.jpg, 5, 2008-08-18, 3, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 13, fangdongbai, 123456, 方东白, 1, 13.jpg, 5, 2012-11-01, 3, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 14, zhangsanfeng, 123456, 张三丰, 1, 14.jpg, 2, 2002-08-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==        Row: 15, yulianzhou, 123456, 俞莲舟, 1, 15.jpg, 2, 2011-05-01, 2, 2025-06-25 16:16:47, 2025-06-25 16:16:47
<==      Total: 11
```
### foreach 标签
我们先前完成了根据单个员工 id 删除员工数据的方法，现在需要完成批量删除员工的方法，首先编写对应的 sql 语句：
```sql
delete from emp where id in (1,2,3);
```
完成 sql 语句的编写以后，我们可以就在 EmpMapper 接口中定义对应的接口方法：
```java
// 批量删除员工  
public void deleteByIds(List<Integer> ids);
```
在对应的 mapper.xml 文件中定义 sql 语句。由于上面的 sql 语句是写死的，我们实际在开发过程中，需要动态的传递需要删除的员工 id，然后根据这些 id 执行对应的 sql 语句，这种需要遍历的场景，就需要使用到动态 sql 中的 foreach 标签：
```xml
<delete id="deleteByIds">  
    delete from emp where id in  
    <foreach collection="ids" item="id" separator="," open="(" close=")">  
        #{id}  
    </foreach>  
</delete>
```

foreach 标签中常见的属性有以下几个：
- collection:：集合名称
- item：集合遍历出来的元素、项
- separator：每一次遍历使用的分隔符
- open：遍历开始前拼接的 sql 片段
- close：遍历结束后拼接的 sql 片段

在单元测试中，编写测试用例：
```java
// 测试批量删除数据 
@Test  
public void testDeleteByIds(){  
    List<Integer> ids = Arrays.asList(15,18);  
    empMapper.deleteByIds(ids);  
}
```
执行结果如下：
```
==>  Preparing: delete from emp where id in ( ? , ? )
==> Parameters: 15(Integer), 18(Integer)
<==    Updates: 2
```

> 可以看到，日志中输出的 sql 语句严格按照 foreach 标签中指定的形式展示，其中的 ？ 表示一个占位符，将在调用接口方法的时候从参数传递到 sql 中，因为传入的 id 只有两个，所以拼接出来的括号中也只需要填入两个元素，这就是动态 sql 的优势。

### sql & include 标签
# Web 开发综合案例
## 准备工作
### 环境搭建
- 准备数据库表（dept, emp）
- 创建 springboot 工程，引入对应的起步依赖（web, mybatis, mysql 驱动, lombok）
- 配置文件 application.properties 中引入 mybatis 的配置信息，准备对应的实体类
- 准备对应的 Mapper，Service（接口、实现类）、Controller 基础结构

### 项目开发规范
案例基于当前主流的前后端分离模式进行开发。
#### Restful 开发规范
- Rest，表述性状态转换，是一种软件架构风格。

**传统风格 VS Rest 风格**

| 传统风格                                        |                       |
| ------------------------------------------- | --------------------- |
| https://localhost:8080/user/getById?id=1    | GET: 查询 id 为 1 的用户    |
| https://locaohost:8080/user/saveUser        | POST: 新增用户            |
| https://locaohost:8080/user/updateUser      | POST: 修改用户            |
| https://locaohost:8080/user/deleteUser?id=1 | GET: 删除 id 为 1 的用户    |
| Rest 风格                                     |                       |
| https://localhost:8080/users/1              | GET: 查询 id 为 1 的用户    |
| https://localhost:8080/users                | POST: 新增用户            |
| https://localhost:8080/users                | PUT: 修改用户             |
| https://localhost:8080/users/1              | DELETE: 删除 id 为 1 的用户 |
注意：
- REST 是风格，是约定方式，约定不是规定，可以打破。
- 描述模块功能常常使用复数形式，也就是加 s 的格式来描述，表示此类资源，而非单个资源。如：users，emps，books。
## 部门管理功能开发
**整体功能模块：**
Controller：
```java
@Slf4j
@RestController
public class DeptController{
	
}
```
**功能模块开发流程：**
明确需求  -> 阅读接口文档 -> 思路分析 -> 接口开发

### 查询部门
首先查看该功能的需求文档以及前后端接口文档，

Controller 层定义：
```java
@Autowired  
private DeptService deptService;

//@RequestMapping(value = "/depts", method = RequestMethod.GET) // 指定请求方式为 GET
@GetMapping("/depts")  
public Result list(){  
    List<Dept> list = deptService.list();  
    log.info("查询全部部门数据");  
    return Result.success(list);  
}
```

Service 层定义：
```java
public interface DeptService {  
    List<Dept> list();  
}
```

```java
@Service  
public class DeptServiceImpl implements DeptService {  
  
    @Autowired  
    private DeptMapper deptMapper;  
  
    public List<Dept> list() {  
        return deptMapper.list();  
    }  
}
```

#### Mapper 层定义：
由于查询全部部门信息的 SQL 语句比较简单，所以我们这里直接基于注解的方式定义 SQL 语句：
```java
public interface DeptMapper {  
    @Select("select * from dept")  
    List<Dept> list();  
}
```

#### 使用 Postman 测试接口功能
请求 url：http://localhost:8080/depts
返回数据格式为：
```JSON
{
    "code": 1,
    "msg": "success",
    "data": [
        {
            "id": 1,
            "name": "学工部",
            "createTime": "2025-06-29T11:59:56",
            "updateTime": "2025-06-29T11:59:56"
        },
        {
            "id": 2,
            "name": "教研部",
            "createTime": "2025-06-29T11:59:56",
            "updateTime": "2025-06-29T11:59:56"
        },
        {
            "id": 3,
            "name": "咨询部",
            "createTime": "2025-06-29T11:59:56",
            "updateTime": "2025-06-29T11:59:56"
        },
        {
            "id": 4,
            "name": "就业部",
            "createTime": "2025-06-29T11:59:56",
            "updateTime": "2025-06-29T11:59:56"
        },
        {
            "id": 5,
            "name": "人事部",
            "createTime": "2025-06-29T11:59:56",
            "updateTime": "2025-06-29T11:59:56"
        }
    ]
}
```
假如我们想要使用别的请求方式访问该请求地址，可以使用 Postman 测试一下是否能够跑通，得到返回数据如下：
```
{
    "timestamp": "2025-06-30T15:21:15.848+00:00",
    "status": 405,
    "error": "Method Not Allowed",
    "path": "/depts"
}
```
根据[[Springboot Web#响应状态码]]内容可知，这是客户端错误，原因就是因为使用了不被允许的请求方式，允许的请求方式在 Controller 中通过注解的形式给出：
```java
//@RequestMapping(value = "/depts", method = RequestMethod.GET) // 指定请求方式为 GET
@GetMapping("/depts") 
```

### 前后端联调
启动 nginx ，同时启动后端项目，使用浏览器访问地址 http://localhost:90 端口，可以查看项目前端页面：
![[Pasted image 20250701122128.png]]
前后端联调通过，说明查询部门的操作完成了。
### 删除部门
Controller:
```java
/**  
 * 删除部门数据  
 * @param id  
 * @return  
 */  
@DeleteMapping("/depts/{id}")  
public Result delete(@PathVariable Integer id){  
    log.info("根据 id 删除部门：{}",id);  
    // 调用 service 删除部门  
    deptService.delete(id);  
    return Result.success();  
}
```
Service:
```java
public void delete(Integer id) {  
    deptMapper.delete(id);  
}
```
Mapper:
```java
@Delete("delete from dept where id = #{id}")  
void delete(Integer id);
```
### 新增部门


注意：
- 一个完整的请求路径，应该是类上的 @RequestMapping 的 value 属性 + 方法上的 @RequestMapping 的 value 属性。
### 修改部门

## 员工管理功能开发
### 分页查询
要完成这部分功能开发，我们首先需要知道前端给后端传递什么参数，后端给前端返回怎样的结果：
![[分页查询员工数据前后端数据传递分析]]
再查看需求文档：

#### 功能开发
```java

```

```java

```


```java

```

#### 接口功能测试
首先测试不传递参数的情况下是否能够使用默认的分页参数，使用 Postman 通过 GET 方式请求 http://localhost:8080/emps 路径，得到返回数据如下：

```JSON
{
    "code": 1,
    "msg": "success",
    "data": {
        "total": 17,
        "rows": [
            {
                "id": 1,
                "username": "jinyong",
                "password": "123456",
                "name": "金庸",
                "gender": 1,
                "image": "1.jpg",
                "job": 4,
                "entryDate": "2000-01-01",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 2
            },
            {
                "id": 2,
                "username": "zhangwuji",
                "password": "123456",
                "name": "张无忌",
                "gender": 1,
                "image": "2.jpg",
                "job": 2,
                "entryDate": "2015-01-01",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 2
            },
            {
                "id": 3,
                "username": "yangxiao",
                "password": "123456",
                "name": "杨逍",
                "gender": 1,
                "image": "3.jpg",
                "job": 2,
                "entryDate": "2008-05-01",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 2
            },
            {
                "id": 4,
                "username": "weiyixiao",
                "password": "123456",
                "name": "韦一笑",
                "gender": 1,
                "image": "4.jpg",
                "job": 2,
                "entryDate": "2007-01-01",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 2
            },
            {
                "id": 5,
                "username": "changyuchun",
                "password": "123456",
                "name": "常遇春",
                "gender": 1,
                "image": "5.jpg",
                "job": 2,
                "entryDate": "2012-12-05",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 2
            },
            {
                "id": 6,
                "username": "xiaozhao",
                "password": "123456",
                "name": "小昭",
                "gender": 2,
                "image": "6.jpg",
                "job": 3,
                "entryDate": "2013-09-05",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            },
            {
                "id": 7,
                "username": "jixiaofu",
                "password": "123456",
                "name": "纪晓芙",
                "gender": 2,
                "image": "7.jpg",
                "job": 1,
                "entryDate": "2005-08-01",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            },
            {
                "id": 8,
                "username": "zhouzhiruo",
                "password": "123456",
                "name": "周芷若",
                "gender": 2,
                "image": "8.jpg",
                "job": 1,
                "entryDate": "2014-11-09",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            },
            {
                "id": 9,
                "username": "dingminjun",
                "password": "123456",
                "name": "丁敏君",
                "gender": 2,
                "image": "9.jpg",
                "job": 1,
                "entryDate": "2011-03-11",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            },
            {
                "id": 10,
                "username": "zhaomin",
                "password": "123456",
                "name": "赵敏",
                "gender": 2,
                "image": "10.jpg",
                "job": 1,
                "entryDate": "2013-09-05",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            }
        ]
    }
}
```
查看控制台输出的日志：
```shell
==>  Preparing: select id, username, password, name, gender, image, job, entrydate, dept_id, create_time, update_time from emp limit ?, ?
==> Parameters: 0(Integer), 10(Integer)
```
说明后端已经设置了两个参数的默认值。

测试传递参数的情况下，是否能够正确查询分页数据：
`http://localhost:8080/emps?page=2&pageSize=5`

```JSON
{
    "code": 1,
    "msg": "success",
    "data": {
        "total": 17,
        "rows": [
            {
                "id": 6,
                "username": "xiaozhao",
                "password": "123456",
                "name": "小昭",
                "gender": 2,
                "image": "6.jpg",
                "job": 3,
                "entryDate": "2013-09-05",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            },
            {
                "id": 7,
                "username": "jixiaofu",
                "password": "123456",
                "name": "纪晓芙",
                "gender": 2,
                "image": "7.jpg",
                "job": 1,
                "entryDate": "2005-08-01",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            },
            {
                "id": 8,
                "username": "zhouzhiruo",
                "password": "123456",
                "name": "周芷若",
                "gender": 2,
                "image": "8.jpg",
                "job": 1,
                "entryDate": "2014-11-09",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            },
            {
                "id": 9,
                "username": "dingminjun",
                "password": "123456",
                "name": "丁敏君",
                "gender": 2,
                "image": "9.jpg",
                "job": 1,
                "entryDate": "2011-03-11",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            },
            {
                "id": 10,
                "username": "zhaomin",
                "password": "123456",
                "name": "赵敏",
                "gender": 2,
                "image": "10.jpg",
                "job": 1,
                "entryDate": "2013-09-05",
                "createTime": "2025-06-29T11:59:56",
                "updateTime": "2025-06-29T11:59:56",
                "deptId": 1
            }
        ]
    }
}
```
#### 分页插件 PageHelper
在上面的开发过程中，不难发现，分页功能的开发还是比较繁琐并且重复的，因为只要涉及到分页查询，都需要查找总记录数，然后根据分页参数查询列表数据，所以我们介绍一款分页插件 PageHelper，减少重复的代码开发工作。

在使用 PageHelper 之前，首先需要在项目中引入依赖：
```xml
<dependency>  
    <groupId>com.github.pagehelper</groupId>  
    <artifactId>pagehelper-spring-boot-starter</artifactId>  
    <version>1.4.7</version>  
</dependency>
```
使用：
```java
// 设置分页参数
PageHelper.startPage(pageNum, pageSize);
// 查询数据
List<Emp> list = empMapper.list();
// 封装返回结果
Page<Emp> page = (Page<Emp>) list;
```
注意：所有与分页相关的操作（查询总记录数，传递分页参数）等工作都是插件辅助完成的，我们只需要在 Mapper 中执行查询操作即可。



在使用 PageHelper 改造查询代码的时候，不难发现，我们只需要更改 Service 层以及 Mapper 层对应的代码即可，对于 Controller 层的代码不需要进行任何更改！这是因为，Controller 层只负责前后端数据传递，只要前端请求的参数以及后端返回给前端的数据不发生变化，Controller 层就无需进行改变。这就是开发过程中遵守单一职责以及分层解耦带来的好处。
### 分页查询（带条件）
完成了基础的员工数据查询以后，我们就需要在这个基础上将员工分页查询功能拓展为能够根据传递的条件进行分页查询，首先阅读[[api接口文档#2.1 员工列表查询]]，根据接口文档定义后端 Controller 方法：
```java
@GetMapping  
public Result page(String name,  
                   Short gender,  
                   @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDate begin,  
                   @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDate end,  
                   @RequestParam(defaultValue = "1") Integer page,  
                   @RequestParam(defaultValue = "10") Integer pageSize) {  
    log.info("分页查询，参数：{},{},{},{},{},{}", name, gender, begin, end, page, pageSize);  
    PageBean pageBean = empService.page(name, gender, begin, end, page, pageSize);  
    return Result.success(pageBean);  
}
```
在 Controller 方法中接收路径参数需要使用 @DateTimeFormat 注解中的 pattern 字段，指定接收的日期传递格式。
然后完成 Service 层代码的编写，Service 层中使用了 PageHelper 插件完善分页条件查询的功能，所以在 Mapper 中编写操作数据库的 SQL 语句时，不需要关心分页相关的参数，只需要正常进行条件查询即可。最后将查询到的结果从 PageHelper 封住的 Page 对象中取出来即可。
```java
@Override  
public PageBean page(String name, Short gender, LocalDate begin, LocalDate end, Integer page, Integer pageSize) {  
    PageHelper.startPage(page, pageSize);  
    List<Emp> empList = empMapper.list(name,gender,begin,end);  
    Page<Emp> p = (Page<Emp>) empList;  
    return new PageBean(p.getTotal(),p.getResult());  
}
```

Mapper 层以及对应的映射文件：
```java
public List<Emp> list(String name, Short gender, LocalDate begin, LocalDate end);
```

```xml
<select id="list" resultType="com.example.springbootwebdemo.pojo.Emp">  
    select *  
    from emp
    <where>  
        <if test="name != null and name != ''">  
            name like concat('%',#{name},'%')  
        </if>  
        <if test="gender != null">  
            and gender = #{gender}  
        </if>  
        <if test="begin != null and end != null">  
            and entrydate between #{begin} and #{end}  
        </if>  
    </where>
    order by update_time desc  
</select>
```

小结：
条件分页查询需要两个步骤：动态查询 - 动态 SQL XML 映射文件；分页查询 - PageHelper 分页插件。
### 删除员工
删除员工操作的难点主要在于如何批量删除员工数据。在查看页面原型的时候，面对单独的删除操作以及批量删除操作是否需要开发两个不同的功能接口呢？其实是不用的，因为单独的删除操作可以看作是批量删除操作但是集合中只有一个 id。
明确基本需求以后，查看[[api接口文档#2.2 删除员工]] 的内容，就可以定义出和前端交互的 Controller 方法：
```java
@DeleteMapping("/{ids}")  
public Result delete(@PathVariable List<Integer> ids) {  
    log.info("批量删除员工，参数：{}",ids);  
    empService.delete(ids);  
    return Result.success();  
}
```
因为前端传递的是路径参数，所以 Controller 方法的参数也需要使用 `@PathVariable` 来使后端能够成功接收到前端传递的参数。

继续完成 Service 层的代码：
```java
@Override  
public void delete(List<Integer> ids) {  
    empMapper.delete(ids);  
}
```
Mapper 层以及对应的 xml 文件：
```java
void delete(List<Integer> ids);
```

mapper.xml：
```xml
<delete id="delete">  
    delete from emp where id in  
    <foreach collection="ids" separator="," open="(" item="id" close=")">  
        #{id}  
    </foreach>  
</delete>
```

到这里批量删除员工的功能就开发完成了，我们使用 Postman 测试一下接口功能是否正确：
```shell
http://localhost:8080/emps/1,2,3
```
返回数据：
```JSON
{
    "code": 1,
    "msg": "success",
    "data": null
}
```
然后查看数据库表，看到 emp 表中 id 为 1,2,3 的员工数据已经成功删除，说明后端功能正常。
### 新增员工
首先查看新增员工的 [[api接口文档#2.3 添加员工]]，前端请求的数据是 JSON 格式数据，使用 POST 方式发送请求。根据接口文档编写 Controller 方法如下：
```java
@PostMapping  
public Result insert(@RequestBody Emp emp) {  
    log.info("插入员工数据：{}",emp);  
    empService.insert(emp);  
    return Result.success();  
}
```
Service 层：
在 Service 层处理前要记得补全传递对象的参数，因为前端传递的 JSON 数据中不包含创建时间与更新时间。
```java
@Override  
public void insert(Emp emp) {  
    emp.setCreateTime(LocalDateTime.now());  
    emp.setUpdateTime(LocalDateTime.now());  
    empMapper.insert(emp);  
}
```
最后编写 Mapper 层代码，因为插入操作比较简单，所以直接使用注解的方式编写 SQL 语句：
```java
@Insert("insert into emp(username, name, gender, job, image, entrydate, dept_id, create_time, update_time) " +  
        "values (#{username}, #{name}, #{gender}, #{job}, #{image},#{entryDate},#{deptId}, #{createTime}, #{updateTime})")  
void insert(Emp emp);
```
编写完成以后，使用 Postman 测试接口功能：
```JSON
{
	"name":"岳不群",
	"username":"yuebuqun",
	"gender":1,
	"image":"1.jpg",
	"job":1,
	"entryDate":"2015-09-18",
	"deptId":1
}
```
得到后端返回的数据：
```JSON
{
    "code": 1,
    "msg": "success",
    "data": null
}
```
再查看数据库以及前端页面，都能够看到新增加的员工数据，说明接口功能开发无误。
### 文件上传
在上面我们完成了新增员工的基本操作，但是在上传员工头像部分只是用来简单的字符串代表上传头像文件的存储地址，现在我们介绍如何完善这部分功能。
#### 简介
- 文件上传，指的是将本地图片、视频、音频等文件上传到服务器，供其他用户浏览或下载的过程。
- 文件上传在项目中应用非常广泛。

在文件上传过程中，一旦前端请求发送，后端接收到请求数据以后，生成的临时文件就会被系统删除，所以我们需要使用本地存储或者云服务器存储的方式来保存服务端接收到的文件。
#### 本地存储
本地存储，指的是在服务端接收到上传来的文件以后，将文件存储在本地服务器的磁盘目录中。

编写 Controller 方法，用于接收前端上传来的数据：
```java
@RestController  
public class UploadController {  
    @PostMapping("/upload")  
    public Result upload(String username, Integer age, MultipartFile image) throws IOException {  
        log.info("文件上传参数：{},{},{}", username, age, image);  
        String originalFilename = image.getOriginalFilename();  
        // 将文件存储在服务器的磁盘目录中  
        image.transferTo(new File("/Users/kane/Dev/SpringbootWebDemo/src/main/resources/upload" + originalFilename));  
        return Result.success();  
    }  
}
```
Spring 中提供了一个类 MultipartFile 用于接收文件类型，该类型的对象中提供了许多方法，能够接收前端上传的文件，并且获得文件的原始文件名，然后调用对象的 transferTo 方法将文件转存到服务器的磁盘目录上。
但是在上面的程序中，还存在一定的问题，由于服务端需要接收很多个客户端的请求，所以很有可能客户端上传的文件名相同，这里我们使用 Postman 模拟一下上传的文件名相同的情况：
![[上传文件名为1.png的图片.png]]
> Postman 在使用 Post 请求上传图片的时候，注意需要在 Body 中选择 `form-data` 这个表单可以提交文件类型数据。然后在 Key 中指定名字，Value 中选择需要上传的文件。

上传成功以后，可以在项目地址的 Resources/upload 目录下找到文件，然后我们从另一个文件夹中，也同样上传一个 1.png 图片，然后再观察项目地址的同一个目录：
![[服务端如何处理文件名相同的问题]]
现在，服务端磁盘目录中已经不存在第一次上传的文件，也就是已经被后一次上传的同名文件替换了。要解决这个问题，我们需要使用 UUID 这个作为每个用户上传的独一无二的文件名。
新的 Controller 代码如下：
```java
@Slf4j  
@RestController  
public class UploadController {  
    @PostMapping("/upload")  
    public Result upload(String username, Integer age, MultipartFile image) throws IOException {  
        log.info("文件上传参数：{},{},{}", username, age, image);  
        // 获取原始文件名  
        String originalFilename = image.getOriginalFilename();  
        // 构建新的文件名  
        String newFilename = UUID.randomUUID().toString() + originalFilename.substring(originalFilename.lastIndexOf("."));  
        // 将文件存储在服务器的磁盘目录中  
        image.transferTo(new File("/Users/kane/Dev/SpringbootWebDemo/src/main/resources/upload/" + newFilename));  
        return Result.success();  
    }  
}
```

在 Springboot 中，文件上传，默认单个文件允许最大大小为 1M。如果需要上传大文件，可以进行如下配置：
```
# 配置单个文件最大上传大小  
spring.servlet.multipart.max-file-size=10MB  
# 配置单个请求最大上传大小（一次请求可以上传多个文件）  
spring.servlet.multipart.max-request-size=100MB
```
本地存储这种存储文件存储方式在实际开发中很少用到，具体原因有以下几点：
- 本地磁盘存储的文件无法使用浏览器直接访问。
- 本地存储存在磁盘容量不足、扩容难以及磁盘损坏的风险。

现在企业级应用在存储文件的时候，都会使用自搭建的服务器或者租用云服务器作为存储文件的路径：
- FastDFS、MinIO。
- 阿里云、腾讯云。
#### 阿里云 OSS
阿里云是阿里巴巴旗下全球领先的云计算公司，也是国内最大的云服务提供商。
阿里云对象存储 OSS（Object Storage Service），是一款海量、安全、低成本、高可靠的云存储服务。使用 OSS，可以通过网络随时存储和调用文本、图片、音频和视频在内的各种文件。

**使用第三方服务的基本思路**
1. 准备工作
2. 参照官方 SDK 编写入门程序
3. 项目中集成使用

**使用阿里云 OSS 集成文件上传功能：**

文件上传模块小结：
1. 文件上传介绍
2. 前端页面三要素（file 表单项、post 方式、multipart/form-data）
3. 服务端接收文件（MultipartFile）
4. 文件存储方式

### 修改员工
在查看页面原型中的需求说明时，我们可以看到在前端修改员工信息的时候，需要提前将员工信息数据返回到修改页面，也就是说，修改员工的操作包含了两个方法：首先根据要查询的员工 id 查找员工数据，然后再更新员工数据。

#### 查询回显
**Controller ：**
```java
@GetMapping("/{id}")  
public Result select(@PathVariable Integer id) {  
    Emp emp = empService.select(id);  
    return Result.success(emp);  
}
```
**Service：**
```java
@Override  
public Emp select(Integer id) {  
    Emp emp = empMapper.select(id);  
    return emp;  
}
```
**Mapper：**
```java
@Select("select * from emp where id = #{id}")  
Emp select(Integer id);
```
#### 更新数据


### 配置文件
#### 问题分析
我们在使用阿里云 OSS 服务的时候，需要配置下面几个参数：

但是实际在项目开发中，如果把所有使用到的技术涉及的参数都通过硬编码的方式写在各个不同的 Java 文件中，对于后期更新参数内容，每一次都需要重新编译生成项目的字节码文件，然后再重新运行。这样的硬编码配置参数的模式是不便于程序员后期维护的。
#### 参数配置化
所以我们可以考虑将参数配置转移到 application.properties 这个配置文件中。



```java
@Value("${aliyun.oss.endpoint}")  
private String endpoint;  
@Value("${aliyun.oss.accessKeyId}")  
private String accessKeyId;  
@Value("${aliyun.oss.accessKeySecret}")  
private String accessKeySecret;  
@Value("${aliyun.oss.bucketName}")  
private String bucketName;
```
@Value 注解通常用于外部配置的属性注入，具体用法为：`@Value("${配置文件中的 key}")`
### Yaml 配置文件
- Springboot 提供了多种属性配置方式
	- application.properties
	`server.port=8080`
	- application.yml / application.yaml

```yaml
server:
	port:8080
	address:127.0.0.1
```
## 登录功能开发
### 登录功能

```sql
select * from emp where username = 'jinyong' and password = '123456';
```


存在的问题：
即使我们实现了用户登录的功能了，当时在未登录的情况下，我们也可以直接访问部门管理、员工管理等功能。这样显然是不符合我们系统开发的要求的，所以接下来我们就介绍使用登录校验来实现用户登录状态的维护。

### 登录校验
![[登录校验]]
- 登录标记：用户登录成功以后，每一次请求中，都可以获取到该标记。（会话技术）
- 统一拦截：使用过滤器 Filter、拦截器 Interceptor。
#### 会话技术
- 会话：用户打开浏览器，访问 Web 服务器的资源，会话建立，直到有一方断开连接，会话结束。==在一次会话中可以包含多次请求和响应。==
- 会话跟踪：一种维护浏览器状态的方法，服务器需要识别多次请求是否来自于同一浏览器，以便在同一次会话的**多次请求**间共享数据。
- 会话跟踪方案：
	- 客户端会话跟踪技术：Cookie
		- 优点：HTTP 协议中支持的技术
		- 缺点：移动端 App 无法使用 Cookie；不安全、用户可以自己禁用 Cookie；Cookie 不能跨域
	- 服务端会话跟踪技术：Session
		- 优点：存储在服务器端、安全
		- 缺点：服务器集群环境下无法直接使用 Session；同样存在 Cookie 的所有缺点，因为 Session 就是基于 Cookie 实现的
	- 令牌技术
		- 优点：支持 PC 端、移动端；解决集群环境下的认证问题；减轻服务器端存储压力
		- 缺点：需要自己实现

Cookie 技术简单代码演示：
```java
@RestController  
public class SessionController {  
    @GetMapping("/c1")  
    public Result cookie1(HttpServletResponse response) {  
        response.addCookie(new Cookie("login_user", "kane"));  
        return Result.success();  
    }  
  
    @GetMapping("/c2")  
    public Result cookie2(HttpServletRequest request) {  
        Cookie[] cookies = request.getCookies();  
        for(Cookie cookie : cookies) {  
            if(cookie.getName().equals("login_user")) {  
                System.out.println(cookie.getValue());  
            }  
        }  
        return Result.success();  
    }  
}
```
#### JWT 令牌
- JWT：JSON Web Token
- 定义了一种简洁的、自包含的格式，用于在通信双方以 ==JSON 数据格式==安全的传输信息。由于==数字签名==的存在，这些信息是安全可靠的。
- （一个 JWT 令牌的格式示例图）
- JWT 令牌的组成：
	- 第一部分：Header(头)，记录令牌类型，签名算法等。例如：{"alg": "HS256", "type": "JWT"}。这部分内容是使用 BASE64 编码后存储在 JWT 令牌的第一部分的。
		- Base64：是一种基于 64 个可打印字符（A-Z a-z 0-9 + /）来表示二进制数据的编码方式。
	- 第二部分：Payload（有效载荷），携带一些自定义信息、默认信息等。例如：{"id": "1", "username": "Tom"}
	- 第三部分：Signature（签名），防止 Token 被篡改，确保安全性。将 header、payload，并加入指定密钥，通过指定签名算法计算而来。
- 场景：登录认证。
	- 登录成功以后，生成 JWT 令牌。
	- 后续每个请求，都要携带 JWT 令牌，系统在每次请求处理之前，先校验令牌，通过后，再处理请求。


##### 基于 Java 实现 JWT 令牌
首先，引入 JWT 令牌的相关依赖。
```xml
<!--        JWT 令牌-->  
        <dependency>  
            <groupId>io.jsonwebtoken</groupId>  
            <artifactId>jjwt</artifactId>  
            <version>0.9.1</version>  
        </dependency>    </dependencies>
```
编写一个测试类，测试使用工具类生成 JWT 令牌：
```java
/**  
 * 定义一个测试方法，用于生成 JWT 令牌  
 */  
@Test
public void genJWT(){  
    Map<String, Object> claims = new HashMap<>();  
    claims.put("id", "1");  
    claims.put("name", "Tom");  
    // 用于构建一个 JWT 令牌
    String jwt = Jwts.builder()  
            .signWith(SignatureAlgorithm.HS256, "kane") // 参数一是签名算法，参数二是签名密钥  
            .setClaims(claims) // 设置自定义内容（载荷部分）  
            .setExpiration(new Date(System.currentTimeMillis() + 3600 * 1000)) // 设置令牌的有效期为 1 小时  
            .compact();  
    System.out.println(jwt);  
    // eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiVG9tIiwiaWQiOiIxIiwiZXhwIjoxNzUzMTk1Nzc0fQ.-B2sog1S89bEhPmgpCGKLwsjbZKA6gFlWlV7XFTXIwA
  
}
```
编写另一个测试类，用于解析 JWT 令牌内容：
```java
@Test  
public void testParseJWT(){  
    Claims claims = Jwts.parser()  
                        .setSigningKey("kane")  
                        .parseClaimsJws("eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiVG9tIiwiaWQiOiIxIiwiZXhwIjoxNzUzMTk1Nzc0fQ.-B2sog1S89bEhPmgpCGKLwsjbZKA6gFlWlV7XFTXIwA")  
                        .getBody();  
    System.out.println(claims);
    // {name=Tom, id=1, exp=1753195774}  
}
```
注意事项：
- JWT 令牌校验时使用的签名密钥，必须和生成 JWT 令牌时使用的密钥是配套的。
- 如果 JWT 令牌解析时报错，则说明 JWT 令牌被篡改或者失效了，令牌非法。
#### 过滤器 Filter
- Filter 过滤器，是 JavaWeb 三大组件（Servlet、Filter、Listener）之一。
- 过滤器可以把对资源的请求拦截下来，从而实现一些特殊的功能。
- 过滤器一般完成一些通用的操作，比如：登录校验、统一编码处理、敏感字符处理等。

如何编写 Filter 程序：
1. 定义 Filter：定义一个类，实现 Filter 接口，并重写接口的所有方法。
2. 配置 Filter：Filter 类上加 @WebFilter 注解，配置拦截资源的路径。引导类上加 @ServletComponentScan 开启 Servlet 组件支持。
 


#### 拦截器 Interceptor


### 异常处理


