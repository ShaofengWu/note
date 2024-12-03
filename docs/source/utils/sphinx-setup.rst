使用 Sphinx 构建文档
========================

本文主要参考知乎链接：`Sphinx Read the Docs 从懵逼到入门 <https://zhuanlan.zhihu.com/p/264647009>`_

进阶参考： `My Secure Shell <https://github.com/mysecureshell/mysecureshell>`_

简介
------
Sphinx 是 Python 语言下的一个文档生成工具，它可以从 reStructuredText 格式的文档源文件中自动生成多种格式的文档，包括 HTML、PDF、EPUB 等。LLVM项目采用的Sphnix生成其项目文档，因此后续考虑采用Sphnix作为项目文档的生成工具。

本文主要描述Sphnix工程的构建过程和所需工具，供编写文档时参考。

首先安装Sphinx及相关工具,基础Sphinx和myst-parser安装请参考LLVM文档编译指南。

额外需要安装主题和自动构建发布工具，如果不在本机发布，则只需要安装 ``sphinx-rtd-theme`` 主题即可。

.. code-block:: bash

    pip install sphinx-rtd-theme myst-parser sphinx-autobuild

外网安装只需要一条命令搞定。

VSCode 编写环境搭建
-------------------

安装插件包

* restructuredtext: lextudio.restructuredtext.vsix
* esbonio: swyddfa.esbonio.vsix

进入Sphinx文档目录，目录结构为::

    docs/
    ├── build/
    ├── source/
    │   ├── _static/
    │   ├── _templates/
    │   ├── conf.py
    │   ├── index.rst
    ├── Makefile 

在包含Makefile的目录下使用 ``make html`` 编译生成HTML文档。