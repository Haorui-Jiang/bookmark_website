import json
import pandas as pd


def extract_links(data):
    results = list()

    def traverse(node, path):
        if node["type"] == "folder":
            current_path = path + [node["title"]]
            for child in node.get("children", []):
                traverse(child, current_path)
        elif node["type"] == "link":
            results.append(
                {
                    "title": node["title"],
                    "url": node["url"],
                    "icon": node["icon"],
                    "remark": "",
                    "path": "/".join(path),
                }
            )

    for root in data:
        traverse(root, [])

    return results


# 读取并解析JSON文件
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


data = load_json("pintree.json")  # 替换为实际文件路径

# 执行解析并输出结果
links = extract_links(data)

# 转换为DataFrame并处理层级路径
df = pd.DataFrame(links)

# 拆分路径为多列
path_split = df["path"].str.split("/", expand=True)
path_split = path_split.fillna("")  # 将NaN替换为空字符串
path_split.columns = [f"Level {i + 1}" for i in range(path_split.shape[1])]

# 合并层级列到主表
df = pd.concat([df.drop("path", axis=1), path_split], axis=1)
excel_file = "bookmarks.xlsx"
df.to_excel(excel_file, index=False)
print(f"Excel 文件 {excel_file} 已生成！")
