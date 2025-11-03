# 顶层目录树
```
gem5/                              # 仓库根目录
├── SConstruct                     # SCons 构建入口脚本
├── build_opts/                    # 预定义构建选项（ISA 列表等）
├── docs/                          # 文档源（reStructuredText, Makefile, conf.py）
├── site_scons/                    # 定制化 SCons 模块和初始化逻辑
├── configs/                       # 仿真示例脚本和参数配置
├── ext/                           # 第三方外部依赖包源码
├── src/                           # 核心源代码（C++ 内核 + Python 接口）
│   ├── SConscript                 # 模块化构建说明
│   ├── Kconfig                    # 构建时选项定义
│   ├── python/                    # Python 同步包装和用户 API
│   └── …                          # 其他 C++/头文件
├── tests/                         # 回归测试脚本和数据
├── build_tools/                   # 构建辅助工具脚本
├── include/                       # 对外公共头文件
├── system/                        # 模拟系统软件（固件、内核示例）
└── util/                          # 实用程序（benchmarks、脚本等）
```

# 目录用途详解
1. SConstruct
   作用：整个项目的构建入口
   工作流程：
	1. 解析命令行参数
	2. 加载 site_scons/site_init.py，注册自定义的 SCons 构建器
	3. 遍历 build_opts/ 选项，生成对应的构建目标
	4. 包含并执行各子目录的 Sconscript 文件
2. build_opts/
   内容：正对不同 ISA（ARM、X86、RISCV 等）的预定义配置文件
   用法示例：
	1. `scons build/All/gem5.opt` 构建所有的 ISA 优化版 gem5
	2. `scons build/RISCV/gem5.opt` 仅构建 RISC-V ISA 
3. 