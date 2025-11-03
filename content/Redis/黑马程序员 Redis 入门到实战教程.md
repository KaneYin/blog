# Redis 快速入门
## 认识 Redis
### 认识 NoSQL
- SQL：关系型数据库。
	- 结构化（Structured）
	- 关联的（Relational）
	- SQL 查询
	- 事务满足 ACID
- NoSQL：非关系型数据库。
	- 非结构化
		- 键值类型（Redis）
		- 文档类型（MongoDB）
		- 列表型（HBase）
		- Graph 类型（Neo4j）
	- 非关联的
	- 非 SQL 查询
	- 事务满足 BASE

### 认识 Redis

特征：
- 键值型，value 支持多种不同的数据结构，功能丰富。
- 命令处理是单线程的，每个命令具备原子性。
- 低延迟，速度快（基于内存、IO 多路复用、良好的编码）
- 支持数据持久化
- 支持主从集群，分片集群
- 支持多语言客户端
### 安装 Redis


## Redis 常见命令

### 5 种常见数据结构

### 通用命令

### 不同数据结构的操作命令
## Redis 的 Java 客户端

### Jedis 客户端

### SpringDataRedis 客户端

