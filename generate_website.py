import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os


# 从 Excel 文件中读取书签
def read_bookmarks_from_xlsx(file_path):
    df = pd.read_excel(file_path)
    bookmarks = []

    # 动态查找所有层级列
    category_columns = []
    for col in df.columns:
        if col.startswith("Level"):
            category_columns.append(col)

    for i, row in df.iterrows():
        title = row["title"]
        url = row["url"]
        icon = row["icon"]
        remark = row["remark"]

        categories = []
        for cat_col in category_columns:
            cat = row.get(cat_col, "")
            if pd.isna(cat):
                break  # 如果遇到空层级列，停止后续层级列的读取
            categories.append(cat)

        bookmark = {
            "title": title,
            "url": url,
            "icon": icon,
            "remark": remark,
            "categories": categories,
        }
        bookmarks.append(bookmark)
    return bookmarks


# 使用 Jinja2 生成 HTML 模板
def generate_html(bookmarks, template_path):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    html_output = template.render(bookmarks=bookmarks)
    return html_output


if __name__ == "__main__":
    excel_file = "bookmarks.xlsx"  # Excel 文件路径
    template_file = "template.html"  # HTML 模板文件路径
    output_file = "bookmarks.html"  # 输出的 HTML 文件路径

    bookmarks = read_bookmarks_from_xlsx(excel_file)  # 读取书签数据
    html_content = generate_html(bookmarks, template_file)  # 生成 HTML 内容

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML 文件 {output_file} 已生成！")
