通过上一部分，我们了解到互联网是如何运作的，Java 早已经为我们封装好了相应的 API 接口，我们只需要直接使用就可以轻松实现网络通信。

# Socket 技术
我们可以通过 Socket 技术（它是计算机之间进行**通信**的**一种约定**或一种方式），实现两台计算机之间的通信，是操作系统底层提供的一套通信技术，支持 TCP 和 UDP。Java 就对 Socket 底层进行了一套完整的封装，我们可以通过 Java 来轻松实现 Socket 通信。

要实现 Socket 通信，我们先要创建一个数据发送者和一个数据接受者，也就是客户端和服务端，我们需要提前启动服务端，来等待客户端的连接，而客户端只需要随时启动去连接服务端就可以，它们默认使用的是 TCP 协议进行连接。

首先编写服务端，服务端使用 ServerSocket 对象来实现，它代表我们的 Socket 服务端。 我们之前说过每个应用程序都需要一个端口来进行 TCP 通信，我们可以为其绑定一个用于通信的端口以便客户端可以进行连接：
```java
// 参数为绑定的端口，之后一律使用这个端口进行通信
ServerSocket serverSocket = new ServerSocket(8080)
```
创建成功以后，由于服务端会一直占用资源，我们在使用完成以后也需要对其资源进行释放，和之前 IO 一样，这里使用 try-with-resource 语法来编写：
```java

```

接着，可以调用 accept() 方法监听客户端连接，如果没有客户端连接，程序会阻塞在 这个位置等待连接：

```java

```

当客户端连接到达以后，accept() 方法会返回 Socket 对象作为结果，它代表一个客户端 Socket 连接，我们可以打印看到客户端连接的相关信息：
```java
Socket accept = serverSocket.accept();  
// 获取 Socket 连接的相关地址（这里是 IP 地址和端口号）
System.out.println("接受来自客户端的连接："+accept.getRemoteSocketAddress() + ":" + accept.getPort());
```
接着就是编写客户端了，我们可以直接使用 Socket 对象来完成，其中的参数分别是服务端地址和端口，这里因为我们是本地启动的服务端，相当于连接自己，所以直接使用我们本机的 IP 即可：
```java
public class Client {  
    public static void main(String[] args) {  
        // 创建一个客户端 socket 对象，参数制定的是客户端 IP 地址以及客户端端口号  
        try(Socket socket = new Socket("localhost",8080)){  
            System.out.println("已经连接到服务器");  
        }  
        catch (IOException e){  
            e.printStackTrace();  
        }  
    }  
}
```

可以尝试一下输入 ipconfig 命令查看网络列表，这里解释一下localhost、192.168.x.x、127.0.0.1 的区别：
> 所有计算机都有一个特殊的网络和 IP 地址，127.0.0.1 它被称为是本地环回地址，我们访问这个 IP 地址等于访问这台电脑自己，这个地址主要用于本地主机和本地服务之间的通信，所以说如果我们要访问自己电脑上的服务端，填写这个 IP 地址就可以。
> 
> 那这个和我们从路由器得到的 IP 地址有什么区别呢？路由器得到的 192.168.x.x 是路由器为我们分配的一个局域网地址，使用自己的地址同样可以代表这台计算机本身，但是当我们切换网络的时候，局域网地址可能出现变化，所以说它不适合作为本地连接的 IP 地址使用。
> 
> localhost 实际上是一个域名，但是它等价于 127.0.0.1 ，操作系统自带的域名解析（通过本地主机 hosts 文件实现）可以自动将 localhost 解析到 127.0.0.1 上，所以很多时候我们使用 localhost 也可以代表本地主机。但是注意，我们以后在学习 JavaWeb 的时候，浏览器会将它们认为是两个不同的站点。

当 Socket 对象创建的时候，就会自动进行连接了：
![[本机建立 Socket 连接.png]]
几点注意事项：
> - 应该先启动服务端程序，可以看到服务端程序启动以后不会结束，而是阻塞着等待客户端程序连接到服务端。
> - 在客户端程序启动以后，两个程序才会继续运行，随后结束。
> - 服务端打印的信息其实是客户端的 IP 地址以及客户端的端口号，为什么客户端的 IP 地址和服务端的 IP 地址一样，这是因为客户端和服务端都部署在本机上，使用的是同一个 IP 地址，如果是两个不同的设备进行 Socket 编程通信的话，部署服务端的计算机将会打印出客户端的 IP 地址；至于端口号则是客户端随机分配得到的一个端口号，因为客户端并不是一直在使用的，所以不同指定一个特定的端口号，而服务端是需要一直运行提供服务的，所以需要一个特定的端口号。

## 使用 Socket 进行数据传输
前面我们介绍了如何使用 Socket 建立网络连接，接下来就需要了解如何使用 Socket 进行数据传输。

要进行数据传输非常简单，我们可以通过 Socket 直接获得一个输入流和一个输出流，这和我们之前在 JavaSE 中学习到的用法是完全一样的，所以学习起来比较简单：

首先在服务端部署一下输入流：
```java
package Socket;  
  
import java.io.IOException;  
import java.io.InputStream;  
import java.net.ServerSocket;  
import java.net.Socket;  
  
public class Server {  
    public static void main(String[] args) {  
        // 创建一个端口号为 8080 的服务端，在本机进行服务端测试的时候，一般端口号都是 8080        try(ServerSocket serverSocket = new ServerSocket(8080)){  
            // 等待客户端连接  
            Socket accept = serverSocket.accept();  
            System.out.println("接受来自客户端的连接："+accept.getInetAddress() + ":" + accept.getPort());  
            // 获取一个输入流信息，输入到服务端的信息，自然就是客户端发送的  
            InputStream inputStream = accept.getInputStream();  
            // 然后就是从输入流中读取数据  
            int len = 0;  
            byte[] buffer = new byte[1024];  
            // 当客户端没有数据要发送的时候，read 处于阻塞状态  
            while((len = inputStream.read(buffer)) > -1){  
                System.out.println("接收到客户端数据：" + new String(buffer, 0, len));  
            }  
        }  
        catch(IOException e){  
            e.printStackTrace();  
        }  
    }  
}
```
客户端这边我们就不断读取控制台输入内容，不断向服务端发送数据：
```java
package Socket;  
  
import java.io.IOException;  
import java.io.OutputStream;  
import java.net.Socket;  
import java.util.Scanner;  
  
public class Client {  
    public static void main(String[] args) {  
        // 创建一个客户端 socket 对象，参数制定的是客户端 IP 地址以及客户端端口号  
        try(Socket socket = new Socket("127.0.0.1",8080);  
            Scanner scanner = new Scanner(System.in);){  
            System.out.println("已经连接到服务器");  
            // 客户端向服务端发送数据，所以客户端使用的是输出流  
            OutputStream outputStream = socket.getOutputStream();  
  
            while(true){  
                // 首先读取到客户端程序运行时输入的数据  
                String msg = scanner.nextLine();  
                // 然后将这些输入的数据发送到服务端程序上  
                outputStream.write(msg.getBytes());  
            }  
        }  
        catch (IOException e){  
            e.printStackTrace();  
        }  
    }  
}
```
和之前建立客户端和服务端连接的时候一样，首先启动服务端，然后等待客户端连接，客户端运行以后不断向服务端发送消息：

![[Socket 进行数据传输.png]]

这样我们就成功实现了向服务端发送数据，现在我们让服务端向客户端发送数据，比如客户端发送完数据以后，服务端会给客户端一个回复，说收到了数据，现在可以这样编写服务端代码：
```java
public static void main(String[] args) {  
    // 创建一个端口号为 8080 的服务端，在本机进行服务端测试的时候，一般端口号都是 8080    try(ServerSocket serverSocket = new ServerSocket(8080)){  
        // 等待客户端连接  
        Socket accept = serverSocket.accept();  
        System.out.println("接受来自客户端的连接："+accept.getInetAddress() + ":" + accept.getPort());  
        // 获取一个输入流信息，输入到服务端的信息，自然就是客户端发送的  
        InputStream inputStream = accept.getInputStream();  
        // 客户端需要向服务端发送确认接收的消息，所以需要使用输出流  
        OutputStream outputStream = accept.getOutputStream();  
        // 然后就是从输入流中读取数据  
        int len = 0;  
        byte[] buffer = new byte[1024];  
        String str = "我已经收到信息";  
        // 当客户端没有数据要发送的时候，read 处于阻塞状态  
        while((len = inputStream.read(buffer)) > -1){  
            System.out.println("接收到客户端数据：" + new String(buffer, 0, len));  
            // 每次接收到客户端数据以后，都给服务端发送一个回复信息，表示我已收到  
            outputStream.write(str.getBytes());  
        }  
    }  
    catch(IOException e){  
        e.printStackTrace();  
    }  
}
```

同理，客户端代码也只需要简单编写即可，在原来代码的基础上加上获取输入流的对象，读取服务端发来的信息：

```java
public static void main(String[] args) {  
    // 创建一个客户端 socket 对象，参数制定的是客户端 IP 地址以及客户端端口号  
    try(Socket socket = new Socket("127.0.0.1",8080);  
        Scanner scanner = new Scanner(System.in);){  
        System.out.println("已经连接到服务器");  
        // 客户端向服务端发送数据，所以客户端使用的是输出流  
        OutputStream outputStream = socket.getOutputStream();  
  
        InputStream inputStream = socket.getInputStream();  
        while(true){  
            // 首先读取到客户端程序运行时输入的数据  
            String msg = scanner.nextLine();  
            // 然后将这些输入的数据发送到服务端程序上  
            outputStream.write(msg.getBytes());  
            byte[] buffer = new byte[1024];  
            int len = inputStream.read(buffer);  
            // 客户端每次发送完一次数据，都要看是否服务端接收到了  
            System.out.println(new String(buffer,0,len));  
        }  
    }  
    catch (IOException e){  
        e.printStackTrace();  
    }  
}
```

![[经过完善的 Socket 数据通信.png]]

## Socket 实现 UDP 连接

前面使用 Socket 技术实现数据传输的时候，都是使用的 TCP 协议，现在我们尝试使用 UDP 协议实现 Socket 连接。
Java 为我们提供了一种 DatagramSocket API，它是一种 UDP Socket，用于发送和接收 UDP 数据报。由于 UDP 不像 TCP 那样需要提前建立连接，所以只需要建立一个 Socket 等待数据到来即可：
```java
import java.net.DatagramPacket;  
import java.net.DatagramSocket;  
  
public class Server {  
    public static void main(String[] args) {  
        // 服务端绑定 8080 端口  
        try(DatagramSocket socket = new DatagramSocket(8080)) {  
            // 接下来我们可以连续读取客户端发来的数据  
            while(true) {  
                // UDP 数据包，类似于数据缓冲区，数据会被先放到缓存里面  
                DatagramPacket packet = new DatagramPacket(new byte[1024], 1024);  
                // 把 socket 接受到的数据放到 packet 缓冲区里面  
                socket.receive(packet);  
                System.out.println("接收到来自：" + packet.getAddress() + ":" + packet.getPort() + "的信息：" +  new String(packet.getData(),packet.getOffset(),packet.getLength()));  
            }  
        }  
        catch(Exception e) {  
            e.printStackTrace();  
        }  
    }  
}
```
客户端这边由于不需要预先建立连接，所以我们直接创建一个UDP 数据包，并在数据包中指定发送的 IP 地址和端口等内容，发送后就可以到达：
```java
import java.io.IOException;  
import java.net.DatagramPacket;  
import java.net.DatagramSocket;  
import java.net.InetAddress;  
import java.util.Scanner;  
  
public class Client {  
    public static void main(String[] args) {  
        try(DatagramSocket socket = new DatagramSocket()){  
            Scanner scanner = new Scanner(System.in);  
            while(true){  
                String msg = scanner.nextLine();  
                byte[] data = msg.getBytes();  
                InetAddress address = InetAddress.getByName("127.0.0.1");  
                // 由于 UDP 是不事先建立连接的协议，所以在数据报中要确定发往的 IP 地址以及端口  
                /**  
                 * 参数解释：  
                 * data 待传输信息的字节数组  
                 * data.length 待传输信息的长度  
                 * addresss InetAddress 类型的对象，通过域名/IP 地址解析出的地址信息  
                 */  
                DatagramPacket packet = new DatagramPacket(data,data.length,address,8080);  
                socket.send(packet);  
            }  
  
        }catch (IOException e){  
            e.printStackTrace();  
        }  
    }  
}
```

```java

```

![[使用 Socket 编程实现 UDP 通信.png]]