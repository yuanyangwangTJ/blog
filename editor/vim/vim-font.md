# vim中文字体优化
## 问题
在使用vim或者gvim时，因为其发行版本中并不支持非等宽字体的显示，所以适合vim编程的中文就比较缺乏，如果使用vim编辑`markdown`等文档时，中文字体对界面还是很有影响的。现在，结合近期自己的探索，分享一些解决方式。

## 解决方式
在`windows`下面，微软雅黑应该是喜闻乐见的字体，但是很遗憾的是，微软雅黑并不是等宽字体，在vim中的设置并不会生效，因此，我们接下来的解决方式正是基于展现微软雅黑级别的中文字体显示效果。

1. **自定义vim**

    正应该是最为高级的方式，既然发行版不可以，那就自己编写一个vim版本可以实现所有字体的显示，事实上，十多年前就已经有人完成了这种编写，具体修改vim源代码的方式可以自己搜索，因为这种方式要求对软件运行等知识有一定要求，有能力者可以考虑。或者可以直接下载已经修改过得发行版vim。

2. **修改字体**

    修改vim源代码对于新手可能有点困难，或者大多数也不愿意放弃官方版或者已经安装好的vim版本，所以这里提供第二条思路，**修改字体**。

    这里提供两条思路，也是从网上看到的答案：一、**修改注册表**，二、**修改字体本身**。第一种方式在此只是提供一种思路，并不作为推荐，因为我也没有实践成功，而且从理论上理解微软雅黑仍旧是非等宽字体，无法在vim显示。而第二种方式则是将微软雅黑修改为**等宽字体**，这可能需要借助字体软件的帮助，当然，如果能够直接获得修改完成的字体也没有问题。

3. **更换字体**
    
    上面的两种方式虽然可以，但是却很麻烦，起码需要一定时间的搜索实践，因此，这里，仅从个人角度推荐一种方式，**更换字体**。

    如果微软雅黑不可以，那有没有等宽的中文字体呢，当然，~~幼圆字体，宋体，楷体~~，但是，这些字体的显示效果并不理想，我在这里推荐一款字体，也是gvim的默认字体`Fixedsys`，可以使用vim命令：
    `:set guifontwide=Fixedsys:h12`观察效果，推荐使用比较大的字号，显示效果比较好。这种方式很简单，而且`Fixedsys`字体和微软雅黑比较相像，应该说是不错的显示效果，下面是我的Gvim中文显示：

[![vim-font.png](https://i.postimg.cc/BbH5J9Dw/vim-font.png)](https://postimg.cc/2LjLxt04)

## 总结
三种方式都可以去尝试，最为推荐第三种方式，剩余两种方式也值得去尝试。也可以留言发表自己的看法与理解，欢迎指教！
