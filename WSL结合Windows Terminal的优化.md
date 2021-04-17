windows下面使用Linux命令，对于如今的工作人员已经不再是遥不可及的梦想，这得益于**WSL** (Windows subsystem for Linux) 的出现，不仅如此，windows系统还推出了**windows terminal**，对于终端的使用更是锦上添花，为了更好利用**terminal**以及**WSL**，下面，我们对这两者进行优化设置，主要是主题以及字体的优化.

# Windows Terminal

## 安装

对于**Windows Terminal**的安装，最简便的方式莫过于在微软商店下载安装，此种方式的优点是可以保持新版本的更新。当然，你也可以选择**GitHub**下载源代码编译安装，甚至可以向官方提出更好的Terminal建议.

## 配置

**Windows Terminal**的配置是通**.json**文件进行配置，你可以在terminal程序中打开它，并且通过文本编辑器修改设置即可生效，关于**json**文件中的变量设置等问题，可以参照微软的官方文档[Microsoft Docs](https://docs.microsoft.com/zh-cn/windows/terminal/)查看配置，当然，下面的美化内容也会涉及到其中的内容.

----

# WSL

## 安装

* **命令行模式安装**

  使用**管理员身份**打开**PowerShell**窗口（如果你已经安装Terminal，可以直接打开），运行下面的命令：

  ```shell
  Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
  ```

  完成之后需要重启电脑.

重启完成之后，便可以安装WSL的系统了，在**微软商店**中搜索**WSL**，选择你想要安装的Linux系统（比如ubuntu），下载安装即可。默认情况下，完成之后，**Windows Terminal**中也应该自动添加了**WSL**的终端.

## WSL美化

下面是文章的核心，具体是关于如何美化WSL终端的设置，当然，这些建立在**Windows Terminal**基础之上.

### 安装oh-my-zsh

**oh-my-zsh**是一款强大的Linux以及MacOS终端的shell，支持一些主题以及插件的安装，提供较于默认的**bash**更为强大的功能，可以使命令行更为简洁方便，安装如下：

* 官方安装方式[Here](https://ohmyz.sh/#install)

* 手动安装

  可能因为各种原因，官网的安装命令运行失败，你可以尝试手动安装的方式去尝试如下：

  ```shell
  $ git clone https://gitee.com/mirrors/oh-...~/.oh-my-zsh
  $ cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
  ```

安装完成之后，便是更改环境shell，相关的命令如下：

* 查看当前环境shell

    ```shell
    echo $SHELL
    ```

* 查看系统有哪些shell

    ```bash
    cat /etc/shells
    ```
* 将**zsh**设置为默认shell

    ```bash
    chsh -s /usr/bin/zsh
    ```

### 主题设置

界面良好的终端自然是需要良好的主题作为支撑，**oh-my-zsh**本身提供了很多的主题，相关的主题名称以及展示可以在这里查看[Here](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)，选择你喜欢的主题设置即可，这里我们以**agnoster**主题设置为例：

* 打开配置文件

  ```shell
  vi ~/.zshrc
  ```

  通过vim配置编辑，设置主题

  ```shell
  ZSH_THEME="agnoster" #直接修改即可
  ```

  保存退出，运行下面的命令使配置生效：

  ```shell
  source ~/.zshrc
  ```

#### 字体

你可能会很吃惊，因为并没有达到官网展示效果，这是因为没有使用**powerline**字体的原因，这里推荐一款不错的字体，**Cascadia Code**，这款字体是由微软开发的编程等宽字体，包含连字以及**powerline**字体（这款字体在微软编辑器中使用还会有意想不到的效果），附下载地址[Here]([Releases · microsoft/cascadia-code · GitHub](https://github.com/microsoft/cascadia-code/releases))，下载完成后只安装**Cascadia Code PL**字体便可以了.

字体安装完成后，设置即可。还记得**Windows Terminal**的配置文件吗？打开文件设置你的终端配置便可以了，这里附上个人的终端设置：

```json
{
    "hidden": false,
    "name": "Ubuntu-20.04",
    "source": "Windows.Terminal.Wsl",
    "suppressApplicationTitle": true,
    "tabTitle": "ubuntu",
    "colorScheme": "Campbell",
    "fontFace": "Cascadia Code PL",
    "fontSize": 11,
    "fontWeight": "normal",
    "cursorShape": "filledBox"
}
```

完成这些就可以呈现不错的**powerline**效果了.

#### 配色

若是不满足于默认的配色，可以寻求更多的配色主题来完成**Windows Terminal**的设置，除了官网本身的主题之外，下面提供一些其他配色方案的**terminal**的**json**格式.

* 这里是配色的图案显示[Here](https://iterm2colorschemes.com/)

* 这里是配色的文件[Here](https://github.com/mbadolato/iTerm2-Color-Schemes/tree/master/windowsterminal)

两者对照即可选出你心仪的主题，当然，也可以**DIY**自己的专属，设置主题便是上面的`colorScheme`选项，后面接上主题`name`，保存后就可以显示了.

### 插件安装

使用**oh-my-zsh**，自然要体验一下插件的功能，下面推荐两个插件，分别是**语法高亮**和**自动提示补全**插件，安装命令如下：

* git下载

    ```shell
    # git下载 zsh-syntax-highlighting
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

    # git下载 zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    ```
* 配置文件修改

    ```shell
    # 首先用vim进入.zshrc配置文件
    vim ~/.zshrc

    # 之后利用vim编辑文件为
    plugins=(
            zsh-syntax-highlighting
            zsh-autosuggestions
            )
    ```

* 运行配置

    ```shell
    source $ZSH/oh-my-zsh.sh
    source $ZSH_CUSTOM/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
    source $ZSH_CUSTOM/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
    ```

以上便是一些终端的优化操作，附上我的WSL终端图：

![image-20210404154419167](C:\Users\86152\AppData\Roaming\Typora\typora-user-images\image-20210404154419167.png)



有问题可以留言.