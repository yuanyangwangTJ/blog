sublime 是一款轻量级的编辑器，用来编译运行python环境还是非常合适的，接下来，文章介绍一下如何在sublime中配置**交互式python环境**.

这里不再做关于sublime安装插件的介绍，网上教程还是有很多可以做参考，只是将相关的插件以及配置列举说明.

我们需要安装两款插件：**Terminus和Anaconda**，用户可以自行安装，下面对插件功能做出相关的说明：
# 1. Terminus以及python编译
Terminus插件提供了类似于终端的功能。通常情况之下，也是网上的大多数教程，使用sublime设置完成python的编译环境之后，为了弥补无法进行交互式的python操作的遗憾，都是选择安装一款REL插件，但是该插件无法让python在底栏也就是panel中显示输出，用户体验并不优秀，而Terminus这款插件却提供了panel中的交互，甚至可以为自己的panel设置主题，所以推荐使用，安装完成之后，通过`Tool->Build System`打开自己的python环境，将配置修改，下面是我的编译设置：
```json
"target": "terminus_exec",
"cancel": "terminus_save_build",
"focus": true,
"cmd": ["D:/Python/python39/python.exe", "-u", "$file"],
"file_regex":"^[ ]*File \"(...*?)\", line ([0-9]*)",
"selector":"source.python",
"encoding": "utf-8",
"env": { "PYTHONIOENCODING": "utf8" },
"working_dir": "$file_path"
```
如果你想要快速体验python，只需要将`cmd`中的第一项修改为自己系统的python环境就可以了，便可以通过<kbd>Ctrl</kbd>+<kbd>B</kbd>体验极致的python运行了，下面对相关设置做简单解释：
前三项设置是将Terminus插件与sublime的编译系统连接，将Terminus的运行结果通过sublime显示，`cmd`为运行命令，接下来为正则表达式，然后是关于语言环境的设置，可以防止输出出现乱码，最后是`working_dir`即工作目录选项，通过此设置设定为python文件所在目录，也与日常工作相符.

# 2. Anaconda 安装设置
为了更好的体验python，我们还需要一些代码的提示功能，而Anaconda插件便可以满足此要求，初闻其名，你或许以为这是python的科学数据计算的conda，但，这只是名字相同而已.

安装完成之后，你便可以看到Anaconda的提示界面，你可以按照说明访问官网，也可以直接选择下面的设置来配置自己的python环境，设置如下：
```json
"python_interpreter": "D:/Python/python39/python.exe",
"anaconda_linter_phantoms": true, // Display lint errors inline
"anaconda_linting": false,
"pep257": true,	// code format
"suppress_word_completions": true,
// "suppress_explict_completions": true,
// "complete_parameters": true,
"use_pylint": true,
"validate_imports": true
```
第一项是计算机python环境，可以自行设置，其余便是有关python代码提示以及代码规范的设置了，你可以根据自己的选择设置.

# 3. 配置完成以及说明
完成之后，便可以体验到非常舒适的python编译环境了，下面便是运行的结果：
![](https://raw.githubusercontent.com/yuanyangwangTJ/Picture/master/img/20210417200611.png)

代码与结果同屏显示，且在底栏不影响视野，还可以进行**交互式**体验，应该可以满足大多数python脚本用户需求.
本篇教程所采用的**Terminus插件**应该属于少数派，但是其效果确实值得sublime用户去安装体验，有问题可以留言提出，祝python愉快！