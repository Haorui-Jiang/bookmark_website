# Bookmark Manager 📚

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

基于Python构建的浏览器书签目录管理工具，支持书签的分类管理、实时搜索和网页浏览功能，可轻松将浏览器书签转换为可共享的在线资源库。

[版本更新日志](changelog.md)

## 功能特点

- **书签分类**：自动解析书签存储路径，支持手动调整书签类别
- **网页图标**：自动读取书签对应网页图标，支持手动修改图标链接
- **实时搜索**：基于书签标题、网页链接等信息进行快速检索
- **网页浏览**：将书签信息转换为网页，便于查看与分享

## 技术栈

- **核心框架**：Python 3.8+
- **书签提取**：[Pintree Bookmarks Exporter](https://www.pintree.io/zh)
- **数据处理**：json + Pandas
- **网页生成**：Jinja2 + Bootstrap 5

## 使用说明

### 文件结构

```python
project/
├── pintree.json		# 浏览器书签 json 文件
├── json2excel.py		# json 解析脚本
├── bookmarks.xlsx      # 解析脚本生成的 Excel 数据文件
├── template.html     	# 网页模板
├── generate_website.py # 生成网页脚本
└── bookmarks.html      # 生成的网页
```

### Excel 数据结构

| 列名           | 说明                       |
| -------------- | -------------------------- |
| title          | 浏览器书签标题             |
| url            | 书签对应网页链接           |
| icon           | 书签对应网页图标           |
| remark         | 书签详细信息备注（自定义） |
| Level 1、2、…… | 书签存储路径第1、2、……层级 |

### 运行流程

1. 浏览器安装 Pintree Bookmarks Exporter 插件：
   - [Chrome Web Store](https://chromewebstore.google.com/detail/pintree-bookmarks-exporte/mjcglnkikjidokobpfdcdmcnfdicojce)
   - [Microsoft Edge Store](https://microsoftedge.microsoft.com/addons/detail/pintree-bookmarks-exporte/binmofchlenaimbnocogbpebiodjlgkm)
2. 使用该插件选择需要导出的书签，生成浏览器书签 json 文件 `pintree.json`，该文件中包含各书签的名称、网页链接、图标链接等信息。
3. 安装 Python 及相关模块，运行 `json2excel.py` 文件，将 json 文件中的书签转换为 Excel 表格。在表格中可以自定义书签备注以及重新调整书签层级路径等信息。
4. 运行 `generate_website.py` 文件，打开生成的 `bookmarks.html`，查看书签目录网页信息。

### 注意事项

- 网页图标链接为插件自动获取，如存在问题可自行查找对应网页源代码，将其图标链接复制到 Excel 表格对应位置进行替换后，再重新运行 `generate_website.py` 文件，生成书签目录网页。

- 本项目生成的代码仅限于个人使用，如需创建可盈利的公共目录网站可基于 [pintree](https://www.pintree.io/zh) 的项目进行创建。

- 本程序代码参考自 [Kimi](https://kimi.moonshot.cn/)、[DeepSeek](https://www.deepseek.com/)（[腾讯元宝](https://yuanbao.tencent.com/)）等国产大模型，衷心感谢这些人工智能研究团队的技术支持。

  
