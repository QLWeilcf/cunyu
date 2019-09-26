
纲领：用好一个工具，让工具更顺手。


### 安装插件
```shell
pip install jupyter_contrib_nbextensions
```
推荐的插件：
- ExecuteTime 展示跑代码的时刻，用的时间
- Table of Contents (2)，根据markdown的标题栏自动生成目录
- Collapsible Headings，可以根据headings折叠区域
- Hinterland，自动补全代码
(jupyter contrib nbextension install --user --skip-running-check )
### 设置自己喜欢的主题

有一个第三方库 [jupyter-themes](https://github.com/dunovank/jupyter-themes),

安装该库：`pip install jupyterthemes`，展示有哪些主题可以用：`jt -l`，用一个主题`jt -t oceans16`，恢复默认`jt -r`，
可以再设置参数，具体可以看官网，参数序列：
```
jt  [-h] [-l] [-t THEME] [-f MONOFONT] [-fs MONOSIZE] [-nf NBFONT]
    [-nfs NBFONTSIZE] [-tf TCFONT] [-tfs TCFONTSIZE] [-dfs DFFONTSIZE]
    [-m MARGINS] [-cursw CURSORWIDTH] [-cursc CURSORCOLOR] [-vim]
    [-cellw CELLWIDTH] [-lineh LINEHEIGHT] [-altp] [-altmd] [-altout]
    [-P] [-T] [-N] [-r] [-dfonts]
```
### 魔法命令

jupyter里的魔法命令都以%或%%开头，**行魔法命令是以** **%** **开头，而单元魔法命令则是** **%%** **开头**。

%run xxx.py   %matplotlib inline

 %%time 魔法操作符，一旦当前格子执行完成，它将会输出执行的耗时。 %time 为单次运行计时，或用%timeit 进行多次计时，然后得到平均值和标准差。

%% HTML

然后就可以在这个cell写html了

%% latex就可以写LaTeX了

### 快捷键
pass


### 导出PDF并支持中文
 - [https://mp.weixin.qq.com/s/-0nt0viV8LmNalmYSCx1Kw](https://mp.weixin.qq.com/s/-0nt0viV8LmNalmYSCx1Kw)
 - [https://www.jianshu.com/p/6b84a9631f8a](https://www.jianshu.com/p/6b84a9631f8a)
 
 
 ### 在jupyter中跑r：

```bash
conda install -c r r-essentials
```

```text
conda create -n my-r-env -c r r-essentials
```

new的时候就可以new一个r环境；
 
### 数据格式（数据组织）
- [Jupyter Notebook数据格式解析](https://mp.weixin.qq.com/s/24B1TSmMPYphXI-0ij3fJQ)
 
