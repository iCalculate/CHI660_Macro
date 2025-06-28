# CHI660_Macro

[English](README_en.md) | [中文](README_zh.md)

`CHI660_Macro` 是一个用于自动生成 CHI660e 工作站宏脚本的 Python 工具集，方便进行循环测试和参数扫描等批量实验。本指南简要介绍宏命令基础及脚本生成器的使用方法。

## 1. CHI 工作站宏命令简介
在软件菜单选择 `Control -> Macro Command` 可进入宏命令界面。与 Windows 批处理或 Linux Shell 脚本类似，宏可以顺序执行多条命令，比 `Repetitive Runs` 更加灵活。

### 常用功能
- **Save**：保存当前宏脚本至文件，系统会弹出保存对话框以确认文件名。
- **Run Macro**：执行编辑框中的宏命令，系统会在执行前检查参数范围是否正确。
- **Macro Command Editor**：编辑框中每一行对应一条命令，不区分大小写，参数与命令之间可使用 `:` 或 `=` 分隔。

![CHI-macro-window](https://pic2.zhimg.com/v2-21baf99afe18cdac6c59cf977294a9ce_r.jpg?source=1940ef5c)

## 2. CHI660e_Macro 脚本生成器
仓库提供 `CHI660e` 类，通过少量函数即可生成灵活的控制脚本，支持同时输出可编辑的 `TXT` 文件及可直接导入软件的 `MCR` 文件。

### 快速开始
以下示例展示了如何批量生成一组循环伏安测试宏命令：

```python
file = open('output.txt', 'w+')  # 创建读写文本文件
chi = CHI660e()                  # 初始化类
chi.init_output_txt(file)        # 写入文件头信息
scan_rates = (0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5)
for rate in scan_rates:
    chi.init_cv_tech(ei=-0.15, eh=-0.25, el=-0.15, v=rate)
    chi.run_cv(file, f'CV-{rate}', add_note=True)
chi.gene_mcr_file(file)          # 生成 MCR 文件
```

生成的 `output.txt` 与 `output.mcr` 可直接在 CHI 软件中加载执行，从而实现长时间的自动化实验。
