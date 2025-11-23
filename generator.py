import os
import yaml

ROOT = "curso_kubernetes_cep"  # folder containing your markdown files

def prettify_title(filename: str) -> str:
    title = os.path.splitext(filename)[0]
    title = title.replace("_", " ").replace("-", " ").title()
    return title

def build_nav(path: str):
    items = []
    for entry in sorted(os.listdir(path)):
        full_path = os.path.join(path, entry)

        # Markdown file
        if entry.endswith(".md"):
            title = "Home" if entry == "index.md" else prettify_title(entry)
            items.append({title: os.path.relpath(full_path, ROOT)})

        # Folder (recurse)
        elif os.path.isdir(full_path):
            sub_nav = build_nav(full_path)
            if sub_nav:
                items.append({prettify_title(entry): sub_nav})

    return items


if __name__ == "__main__":
    nav = build_nav(ROOT)

    mkdocs_config = {
        "site_name": "My Course Portal",
        "nav": nav,
        "theme": {"name": "material"},
    }

    with open("mkdocs.yml", "w", encoding="utf-8") as f:
        yaml.dump(
            mkdocs_config,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
        )

    print("Generated mkdocs.yml successfully!")
