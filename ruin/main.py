import os
import shutil
from dataclasses import dataclass
from pathlib import Path

import sass
from jinja2 import Environment, FileSystemLoader, select_autoescape


@dataclass
class Project:
    root: Path

    @property
    def template_path(self):
        return self.root / "_templates"

    @property
    def static_path(self):
        return self.root / "_static"

    @property
    def sass_path(self):
        return self.root / "_sass"

    @property
    def docs_path(self):
        return self.root / "docs"

    @property
    def docs_static_path(self):
        return self.root / "docs/static"


def is_page_template(name: str) -> bool:
    """ Distinguish the template "name" should be build or not
    """
    return not os.path.basename(name).startswith("_")


def build_templates(project: Project):
    env = Environment(
        loader=FileSystemLoader(project.template_path),
        autoescape=select_autoescape(["html", "xml"]),
    )
    for template_name in env.list_templates():
        if not is_page_template(template_name):
            continue
        html_path = project.docs_path / template_name
        html_path.parent.mkdir(exist_ok=True, parents=True)

        template = env.get_template(template_name)

        with html_path.open(mode="w") as f:
            template.stream().dump(f)


def copy_static(project: Project):
    shutil.copytree(
        str(project.static_path), str(project.docs_static_path), dirs_exist_ok=True
    )


def build_sass(project: Project):
    sass.compile(
        dirname=(str(project.sass_path), str(project.docs_static_path / "css")),
        output_style="compressed",
    )


def main():
    project = Project(Path("."))
    copy_static(project)
    build_sass(project)
    build_templates(project)
