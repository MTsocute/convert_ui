# README
---
> [!note]
>
> - 这个工具用于转换 Qt 的 `* .ui` 文件为 `*.py `文件
> - 对于没有使用 Vscode 插件的用户，还是一个不错的脚本
> - 如果没有指定 `-p` 参数，那么生成的文件会在当前目录下生成一个 `ui_files` 文件夹

<br>

## 安装方法

```shell
# 使用 pip  安装
pip install --upgrade build
# 使用 uv 可以这样子
uv pip install --upgrade build

# 构建我们的包
python -m build 
# uv build
uv run -m build
```

> 成功后，本地应该会有下面的文件结构

```shell
dist/
 ├─ convert_ui-0.3.2-py3-none-any.whl
 └─ convert_ui-0.3.2.tar.gz
```

> 本地安装测试

```shell
pip install dist/convert_ui-0.3.2-py3-none-any.whl
```

> 测试命令是否可以使用了

```shell
convert_ui -h
```



## 使用方法

```shell
# 使用说明
convert_ui -h 

# 转换当前目录下所有的文件为py文件
convert_ui

# 批量转换指定目录下的文件为py文件
convert_ui -t ./demo1.ui ./demo2.ui

# 指定输出目录
convert_ui -t ./demo1.ui -p ./demo_py
```